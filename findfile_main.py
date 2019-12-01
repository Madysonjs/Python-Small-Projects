# Python 3.8.1

#Author: Madyson JS

#Purpose: Tech Academy Drill using Tkinter and GUI

from tkinter import *
import tkinter as tk

import findfile_gui

class mainWindow(Frame):
    def __init__(self, primary, *args, **kwargs):
        Frame.__init__(self, primary, *args, **kwargs)
        #define size of primary window
        self.primary = primary
        self.primary.minsize(600,200)
        self.primary.maxsize(600,200)

        self.primary.title("Check files")
        self.primary.configure(bg="#F0F0F0")

        findfile_gui.load_gui(self)


if __name__=="__main__":
    root = tk.Tk() #Represents the Tk.() root frame (window) into being
    App = mainWindow(root) #Represents our own class as an App object
    root=mainWindow() #Ensures that the class object, in this case our window, keeps looping
    
        
