from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class WhatsApp:
    def __init__(self):
        pass

    def login(self):
        try:
            self.bot = webdriver.Chrome("drivers/chromedriver_ver_83.exe")
        except Exception:
            try:
                self.bot = webdriver.Chrome("drivers/chromedriver_ver_85.exe")
            except Exception as e:
                print("\nException in ChromeDriver\nMessage: ",e,"\n\n")

        # Open Web WhatsApp
        self.bot.get('https://web.whatsapp.com/')

        #input("Press Enter once done")
        #sleep(5)

        print("\nWhatsApp Opened\n")

    def minimize(self):
        self.bot.minimize_window()

    def get_group(self, group_name):
        try:
            open_group = self.bot.find_element_by_xpath('//span[@title = "{}"]'.format(group_name))
            open_group.click()
        except Exception as e:
            try:
                search_box = self.bot.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                search_box.send_keys(group_name)
                sleep(3)
                open_group = self.bot.find_element_by_xpath('//span[@title = "{}"]'.format(group_name))
                open_group.click()
            except Exception as e:
                print("\n\nException in Finiding Groups.\nException Message: ", e)

    def get_msg_box(self):
        try:
            msg_box = self.bot.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            return msg_box
        except Exception as e:
            print("\n\nException in Getting msg box.\nException Message: ", e)

    def click_send_with_media(self):
        try:
            send_btn = self.bot.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
            send_btn.click()
        except Exception as e:
            print("\n\nException in Clicking on send.\nException Message: ", e)

    def click_send_without_media(self):
        try:
            send_btn = self.bot.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            send_btn.click()
        except Exception as e:
            print("\n\nException in Clicking on send.\nException Message: ", e)

    def send_msg(self, group_name, msg, media_path):
        bot = self.bot

        # Open Group
        self.get_group(group_name)

        sleep(1)

        # Add caption
        msg_box = bot.find_element_by_xpath('//div[@data-tab="1"]')
        for single_line_msg in msg.split('\\n'):
            msg_box.send_keys(single_line_msg)
            ActionChains(bot).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            sleep(0.5)

        sleep(1)

        if media_path == '' or media_path == None:
            # Click on send
            self.click_send_without_media()
        else:
            # Attach Media
            self.attach_btn = bot.find_element_by_xpath('//div[@title="Attach"]')
            self.attach_btn.click()
            self.image_box = bot.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            self.image_box.send_keys(media_path)
            sleep(2)
            # Click on send
            self.click_send_with_media()


        if media_path =='':
            msg = msg.replace('\\n','\n')
            return f"Message sent to --> {group_name}\nMessage is -->\n{msg}\n\n"
        else:
            msg = msg.replace('\\n','\n')
            return f"Message sent to --> {group_name}\nMessage is -->\n{msg}\nImage --> {media_path}\n\n"
        #print("\n\nMessage sent to: ",group_name[i],"\nMessage is: ",msg,"\n\n")

    def logout_exit(self):
        bot = self.bot

        # Logout from WhatsApp
        bot.find_element_by_xpath('//div[@title="Menu"]').click()
        sleep(1)
        bot.find_element_by_xpath('//div[@title="Log out"]').click()
        sleep(0.5)

        # Close Chrome
        bot.quit()

if __name__ == "__main__":
    driver = WhatsApp()
    while True:
        group_name = input("Enter group names: ").split(',')
        group_name = [x.strip() for x in group_name]
        media_path = input("If you want to send image, give it's path: ")
        msg = str(input("Enter your message:"))
        driver.send_msg(group_name, msg, media_path)
        
        do_again = input("Want more msgs to send? ")
        if do_again == "Yes" or do_again == "yes":
            pass
        elif do_again == "No" or do_again == "no":
            driver.logout_exit()
            break