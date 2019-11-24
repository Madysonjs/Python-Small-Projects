import os
#list files in assignment folder

file_list = os.listdir(r'C:\Users\Student\Desktop\Assignment')
print("The files in the Assingment folder are listed below:\n")
print(file_list)

#join each text file to path
for file in file_list:
    if file.endswith('.txt'):
        abPath = os.path.join(r'C:\Users\Student\Desktop\Assignment',file)
        modTime = os.path.getmtime(abPath)
        print(modTime,file)




