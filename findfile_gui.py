
#Python Ver: 3.8

#Author: Madyson JS

#Purpose: File finder using Tkinter and Gui

from tkinter import *
import tkinter as tk

import findfile_main

def load_gui(self):
    
    self.txt_browse1 = tk.Entry(self.primary, text="", width=70)
    self.txt_browse1.grid(row=1, column=1, padx=(10,0), pady=(55,0),sticky = N+E+W)
    self.txt_browse1 = tk.Entry(self.primary, text="", width=70)
    self.txt_browse1.grid(row=2, column=1, padx=(10,0), pady=(20,0), sticky = N+E+W)
    
    self.btn_browse1 = tk.Button(self.primary, width=12, height=1, text="Browse...")
    self.btn_browse1.grid(row=1, column=0, padx=(30,0), pady=(50,0), sticky = W)

    self.btn_browse2 = tk.Button(self.primary, width=12, height=1, text="Browse...")
    self.btn_browse2.grid(row=2, column=0, padx=(30,0), pady=(15,0), sticky = W)

    self.btn_chkfiles = tk.Button(self.primary, width=12, height=2, text="Check for Files...")
    self.btn_chkfiles.grid(row=3, column=0, padx=(30,0), pady=(20,0), sticky = S+W)
    
    self.btn_closePrgm = tk.Button(self.primary, width=12, height=2, text="Close Program")
    self.btn_closePrgm.grid(row=3, column=1, padx=(30,0), pady=(20,0), sticky = S+E)


if __name__ == "__main__":
    pass
