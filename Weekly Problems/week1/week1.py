#!Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png 
# all the way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats. For example:

"""sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png"""

import os

files = os.listdir('Weekly Problems\week1')

i = 1
#! Renaming all file which type is .png to the number starting from 1 using OS module. 

for file in files:
    if file.endswith('.png'):
        print(file)
        os.rename(f'Weekly Problems\week1\{file}', f'Weekly Problems\week1\{i}.png') #! Don't forget to include extension of the file while renaming to avoid loss of the file. 
        i += 1


#! Renaming all file which type if .jpg to the strings listed in the below list (nameList). 

nameList = ['Mercury', 'Venus', 'Earth']
i = 0
for file in files:
    if file.endswith('.jpg'):
        os.rename(f'Weekly Problems\week1\{file}', f'Weekly Problems\week1\{nameList[i]}.jpg') #! Don't forget to include extension of the file while renaming to avoid loss of the file. 
        i += 1