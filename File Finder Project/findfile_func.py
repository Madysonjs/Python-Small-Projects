#Python Version 3.8

#Author: Madyson JS

#Purpose: Functions for findfile_main

#have to import specific funtion
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os, shutil
import sqlite3


import findfile_main
import findfile_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Do you want to exit the program?"):
        self.master.destroy()
        os._exit(0)

def browseFile(self):
    fileName = filedialog.askdirectory(title="Please select a directory.")
    self.sourcefile.set(fileName)


def browseFile2(self):
    fileName2 = filedialog.askdirectory(title="Please select a directory.")
    self.destinationfile.set(fileName2)

def checkFile(self):
    ogdir = self.sourcefile.get()
    newdir = self.destinationfile.get()
    dlist = os.listdir(ogdir)
    for file in dlist:
        if file.endswith('.txt'):
            abPath = os.path.join(ogdir,file)
            modTime = os.path.getmtime(abPath)
            #Create table and insert .txt files with timestamps
            conn = sqlite3.connect('FindFile.db')
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_filename TEXT, \
                    col_timestamp TEXT)")
                cur.execute("INSERT INTO tbl_files(col_filename, col_timestamp) VALUES(?,?)", \
                            (abPath, modTime))
                conn.commit()
                #Pull .txt files
                cur.execute("SELECT * FROM tbl_files")
                varFile = cur.fetchall()
                for column in varFile:
                    msg = 'Below are your text files: {} {}'.format(column[1],column[2])
                    print(msg)
                conn.commit()
            #move file to other directory
            shutil.move(abPath, newdir)

                
                                    
            

if __name__ == "__main__":
    pass
    

    
