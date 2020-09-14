# Importing all the libraries
import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter import filedialog, Text
from tkinter.font import Font
from whatsaap_main import WhatsApp
from time import time
import threading
import utils.utility_methods as util

class GUI:
    def __init__(self):
        
        self.utils = util.utility_method()
        self.whatsapp = WhatsApp()

        # Creating Window
        self.root = tk.Tk()
        self.root.title("WhatsApp Automation")
        self.root.configure(bg='#ECE5DD')
        self.root.geometry("900x500+310+150")
        self.root.iconbitmap('images/whatsapp_logo.ico')

        # For background green color
        background = tk.Label(self.root, text=' ', bg='#00bfa5', height=16, width=self.root.winfo_screenwidth())
        background.grid(row=0, column=0, sticky='nsew')
        

        # Initilizing all Font and colors
        self.title_font = Font(family="s", size= 40, weight="bold")
        self.sub_font = Font(family="Helvetica", size= 12)
        self.form_font = Font(family="Open Sans", size=10)
        self.small_font = Font(family="Helvetica", size= 8)
        self.btn_font = Font(family="Open Sans", size = 10)
        self.btn_color = '#25D366'

        # Initializing global variables
        self.frame = None
        self.login_frame = None
        self.get_msg_frame = None
        self.media_path = None
        self.groups_names = None
        self.msg_update_frame = None
        self.msg = None


    def initial_window(self):

        # wgwgw
        self.frame = tk.Frame(self.root)
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        main_text = tk.Label(self.frame, text="WhatsApp Automation", justify= 'center', font=self.title_font)
        main_text.pack(pady=(50,0))

        sub_text = tk.Label(self.frame, text="By clicking on start button, WhatsApp Web will be opened in a new browser window. After which you will have to scan the QR code",
                                justify= 'center', font=self.sub_font, wraplength=700)
        sub_text.pack(pady=(50,30))

        start_btn = tk.Button(self.frame, text="Use Chorme", fg='white', padx=10, pady=5, bg=self.btn_color, font=self.btn_font, command=self.wait_login)
        start_btn.pack()

    def wait_login(self):
        
        # Create New Frame
        self.frame.destroy()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # Minimizing window
        try:
            self.whatsapp.minimize()
        except Exception:
            pass
        
        # Title
        main_text = tk.Label(self.login_frame, text="Scan the QR Code in your Phone", justify= 'center', font=self.title_font, wraplength=700)
        main_text.pack(pady=(50,0))

        # Sub Text
        sub_text_1 = tk.Label(self.login_frame, text="A new Chrome window would have been opened. Please scan the QR code in your WhatsApp and then press the below button",
                                justify= 'center', font=self.sub_font, wraplength=700)
        sub_text_1.pack(pady=(50,30))

        # Buttons
        start_btn = tk.Button(self.login_frame, text="Scanned the QR code", fg='white',
                                padx=10, pady=5, bg=self.btn_color, font=self.btn_font, command=self.get_msg)
        start_btn.pack()

        # Sub Text
        sub_text_2 = tk.Label(self.login_frame, text="If you don't find, then the new browser would be minimized",
                                justify= 'center', font=self.small_font, wraplength=700)
        sub_text_2.pack(pady=(20,30))
        
        # Open WhatsApp Web in Chrome
        threading.Thread(target=self.whatsapp.login).start()  # Threading to not freeze window

    def get_msg(self):

        # Create New Frame
        self.login_frame.destroy()
        self.get_msg_frame = tk.Frame(self.root)
        self.get_msg_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
        #get_msg_frame.grid(row=0, column=1)

        # Title
        main_text = tk.Label(self.get_msg_frame, text="Enter what you want to send",font=self.sub_font, wraplength=700)
        main_text.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(30,0))

        sub_text = tk.Label(self.get_msg_frame, text="Note: Please enter group names as they are. They are case sensetive",
                font=self.sub_font, wraplength=700)
        sub_text.grid(row=1, column=0, columnspan=2, sticky='nsew', pady=(5,0))

        # Take Groups
        groups_label = tk.Label(self.get_msg_frame, text="Groups (Comma Seperated): ",
                                font=self.form_font, wraplength=700)
        groups_label.grid(row=2, column=0, sticky='e', pady=(30,0))
        # Groups input
        self.groups_input = tkscrolled.ScrolledText(self.get_msg_frame, wrap=tk.WORD, height=3, width=40, font=self.form_font, fg='gray')
        self.groups_input.grid(row=2, column=1, pady=(30,0), padx=(10,0), sticky='w')
        groups_input_text = 'Exact Names of the Groups'
        self.groups_input.insert(tk.INSERT, groups_input_text)
        self.groups_input.bind('<FocusIn>',
                    lambda event: self.utils.placeholder_FocusIn(event, self.groups_input, groups_input_text))
        self.groups_input.bind('<FocusOut>',
                    lambda event: self.utils.placeholder_FocusOut(event, self.groups_input, groups_input_text))

        # Take Message
        msg_label = tk.Label(self.get_msg_frame, text="Enter Message: ", font=self.form_font, wraplength=700)
        msg_label.grid(row=3, column=0, sticky='e', pady=(30,0))
        # Message input
        self.msg_input = tkscrolled.ScrolledText(self.get_msg_frame, wrap=tk.WORD, height=3, width=40, font=self.form_font, fg='gray')
        self.msg_input.grid(row=3, column=1, pady=(30,0), padx=(10,0), sticky='w')
        msg_input_text = 'Enter Message'
        self.msg_input.insert(tk.INSERT, msg_input_text)
        self.msg_input.bind('<FocusIn>', 
                    lambda event: self.utils.placeholder_FocusIn(event, self.msg_input, msg_input_text))
        self.msg_input.bind('<FocusOut>',
                    lambda event: self.utils.placeholder_FocusOut(event, self.msg_input, msg_input_text))

        # Import Media
        image_label = tk.Label(self.get_msg_frame, text="Import Image if you want: ", font=self.form_font, wraplength=700)
        image_label.grid(row=4, column=0, sticky='e', pady=(30,0))
        # Media Path
        self.utils.green_button(self.get_msg_frame, 'Brows Image', 4, 1, self.btn_font, self.utils.image_dialog)

        # Send msgs
        send_btn = tk.Button(self.get_msg_frame, text='Send', fg='white',
                bg=self.btn_color, font=('Helvetica', 12, 'bold'), width=12, heigh=1, command=self.msg_update)
        send_btn.grid(row=5, column=1, pady=(50,0), sticky='w')

        # Fillout remaining spaces inside grid
        self.get_msg_frame.columnconfigure(0, weight=1, minsize=1)
        self.get_msg_frame.columnconfigure(1, weight=1, minsize=1)

    def msg_update(self):

        self.groups_names = [x.strip() for x in self.utils.placeholder_FocusOut(tk.EventType.FocusOut,self.groups_input, '').split(',')]
        self.msg = self.utils.placeholder_FocusOut('',self.msg_input, '')
        self.media_path = self.utils.filename
        self.get_msg_frame.destroy()
        self.msg_update_frame = tk.Frame(self.root)
        self.msg_update_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        print("\nName of groups --> ",self.groups_names)
        print("\nThis is the msg --> ",self.msg.replace('\n','\\n'))

        self.long_label = tkscrolled.ScrolledText(self.msg_update_frame, font=self.form_font)
        self.long_label.grid(column=0, padx=1, pady=(20,0), columnspan=2)

        again_send_msg = tk.Button(self.msg_update_frame, text='Send more msgs', fg='white',
                bg=self.btn_color, font=('Helvetica', 12, 'bold'), command=self.get_msg)
        again_send_msg.grid(row=1, column=0, pady=(30,20))

        logout_exit = tk.Button(self.msg_update_frame, text='Logout and Exit', fg='white',
                bg=self.btn_color, font=('Helvetica', 12, 'bold'), command=self.logout_quit)
        logout_exit.grid(row=1, column=1, pady=(30,20))

        threading.Thread(target=self.printing).start()

        self.msg_update_frame.rowconfigure(0, weight=1)
        self.msg_update_frame.columnconfigure(0, weight=1)
        self.msg_update_frame.columnconfigure(1, weight=1)

    def printing(self):
        for i in range(0, len(self.groups_names)):
            sent_msg_text = self.whatsapp.send_msg(self.groups_names[i],
                    self.msg.replace('\n','\\n'), self.media_path)
            self.long_label.insert(tk.INSERT, sent_msg_text)
            print(sent_msg_text)

    def logout_quit(self):
        self.whatsapp.logout_exit()
        print("\nLogged out from WhatsApp. Quitting window now\n")
        self.root.quit()

gui = GUI()
gui.initial_window()
gui.root.resizable(True, True)
gui.root.mainloop()