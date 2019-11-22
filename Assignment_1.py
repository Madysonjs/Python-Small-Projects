
import os
#list files in assignment folder

file_list = os.listdir(r'C:\Users\Student\Desktop\Assignment')
print("The files in the Assingment folder are listed below:\n")
print(file_list)

#join each text file to path
for file in file_list:
    if file.endswith('.txt'):
        print(os.path.join(r'C:\Users\Student\Desktop\Assignment',file))

#print time stamp
print('Test.txt time stamp is: ')
print(os.path.getmtime(r'C:\Users\Student\Desktop\Assignment\test.txt'))

print('Test2.txt time stamp is: ')
print(os.path.getmtime(r'C:\Users\Student\Desktop\Assignment\test2.txt'))




