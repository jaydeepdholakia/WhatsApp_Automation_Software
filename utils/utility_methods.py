# Importing all the libraries
import tkinter as tk
from tkinter import filedialog
import os.path as ospath

class utility_method():
    def __init__(self):
        self.master_root = None
        self.filename = None
        self.file_extensions = (('JPEG', '*jpg'), ('PNG', '*.png'), ('GIF', '*.gif'),
            ('MP4', '*.mp4'), ('All Files', '*.*'))

    def placeholder_FocusIn(self, event, input_name, text):
        if input_name.get('1.0', 'end-1c') == text:
                input_name.delete(1.0, tk.END)
                input_name.config(fg='black')
                #input_name.unbind('<FocusIn>')
        else:
            pass

    def placeholder_FocusOut(self, event, input_name, text):
        if input_name.get('1.0', 'end-1c') == '':
            input_name.insert(tk.INSERT, text)
            input_name.config(fg='gray')
        else:
            return input_name.get('1.0', 'end-1c')

    def normal_button(self, master, btn_txt, row_size, col_size, font_family, command):
        button = tk.Button(master, text= btn_txt, command= command,font=font_family)
        button.grid(row=row_size , column=col_size, sticky='w', padx=(10,0), pady=(30,0))

    def green_button(self, master, btn_txt, row_size, col_size, font_family, command):
        self.master_root = master # storing the frame so that it could be later used in image browsing
        self.button = tk.Button(master, text= btn_txt, command=command, font=font_family, fg='white', bg='#25D366')
        self.button.grid(row=row_size , column=col_size, sticky='w', padx=(10,0), pady=(30,0))

    def image_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title="Select Image/Video", filetype=self.file_extensions)
        print("Media Path: ",self.filename) # Print filepath
        if self.filename !='':
            temp_label = tk.Label(self.master_root, text='')
            temp_label.grid(row=3, column=1, pady=(30,0))
            temp_label.configure(text= ospath.basename(self.filename))