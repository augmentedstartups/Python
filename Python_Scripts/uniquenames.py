###################################
#Created by :  R Kanjee
#Description
#Script will cycle thru all xml files and only add unique names to list
#The purpose of this scipt is to get all the classes annotated for VOC dataset.
###########################################
import os
from xml.etree import ElementTree

names = []
XMLfolder = [folder for folder in os.listdir('.') if 'Armoured' in folder]

for folder in XMLfolder:
    root = ElementTree.parse(folder)
    classes = root.findall('object/name')
    for child in classes:
        names.append(child.text)
    
    
myset = list(set(names))
print (myset)
         