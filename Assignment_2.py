

#import database

import sqlite3

#connect to the database

conn = sqlite3.connect('Assignment_2.db')

#create the table
def createTable():
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT)")
        conn.commit()
    

#insert .txt files into table
def instTable():
    fileList = ['information.docx','Hello.txt','myImage.png','myMovie.mpg',\
                            'World.txt', 'data.pdf', 'myPhoto.jpg']
    for file in fileList:
        if file.endswith('.txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_filename) VALUES(?)", \
                            (file,))
                conn.commit()


#pull files that end in .txt and print them

def findFiles():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_files")
        varFile = cur.fetchall()
        for column in varFile:
            msg = 'Below are your text files: {} {}'.format(column[0],  column[1])
            print(msg)

createTable()
instTable()
findFiles()
