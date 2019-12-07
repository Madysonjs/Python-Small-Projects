# Python 3.8.0

#Author: Madyson JS

#Purpose: Tech Academy Drill using Tkinter and GUI

from tkinter import *
import tkinter as tk

import findfile_gui
import findfile_func
import sqlite3


class mainWindow(Frame):
    def __init__(self, primary, *args, **kwargs):
        Frame.__init__(self, primary, *args, **kwargs)
        #define size of primary window
        self.sourcefile = StringVar()
        self.destinationfile = StringVar()
        self.primary = primary
        self.primary.minsize(600,200)
        self.primary.maxsize(600,200)

        self.primary.title("Check files")
        self.primary.configure(bg="#F0F0F0")
        
        findfile_gui.load_gui(self)
       


if __name__=="__main__":
    conn = sqlite3.connect('FindFile.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_timestamp TEXT)")
    conn.commit()
    root = tk.Tk() #Represents the Tk.() root frame (window) into being
    App = mainWindow(root) #Represents our own class as an App object
    
    
        
