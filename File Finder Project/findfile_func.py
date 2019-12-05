#Python Version 3.8

#Author: Madyson JS

#Purpose: Functions for findfile_main

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os


import findfile_main
import findfile_gui

def ask_quit(self):
    warning = messasagebox.askokcancel("Exit Program", "Do you want to exit the program?")
    if warning:
        self.master.destroy()
        os._exit(0)

def browseFile(self):
    fileName = filedialog.askdirectory(title="Please select a directory.")
    self.fileinput.set(fileName)


def browseFile2(self):
    fileName2 = filedialog.askdirectory(title="Please select a directory.")
    self.fileinput2.set(fileName2)


if __name__ == "__main__":
    pass
    

    
