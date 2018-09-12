###################################
#Created by :  R Kanjee
#Description
###########################################
import os
from xml.etree import ElementTree

names = []
fileindex = []
XMLfolder = [folder for folder in os.listdir('.') if 'Armoured' in folder]

for folder in XMLfolder:
    root = ElementTree.parse(folder)
    classes = root.findall('size/height')
    filenames = root.findall('filename')
    for child in classes:
        #print (child.text)
        if child.text == '0':
           for son in filenames:
               fileindex.append(son.text)
               #print (son.text) 
               names.append(son.text)

     
myset = list(names)
print(myset)
#print (myset.index('0'))

print (len(myset))