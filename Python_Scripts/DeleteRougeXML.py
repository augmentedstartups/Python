##########################################
#Created by :  R Kanjee
#Description:  LabelNet forgets to record the resolutions on some images
#               This scripts fills in the blanks of the missing resolutions
###########################################
import os
from xml.etree import ElementTree
from PIL import Image
import glob

names = []
xmlarray = []
fileindex = []
new_width = []
new_height = []
##IDENTIFY#FILES#WITH#MISSING#DATA############################################################
xml_path = ("C:/Users/OSS_FPGA/Documents/YOLO/darkflow-master/new_model_data/CNN_Armed_people/Annotations/")
file_array = [f for f in os.listdir(xml_path) if f.endswith('.xml')]
file_array.sort() # file is sorted list
file_array = [os.path.join(xml_path, name) for name in file_array]

for filename in file_array:
     root = ElementTree.parse(filename)
     classes = root.findall('size/width')
     filenames = root.findall('filename')
     for child in classes:
         if child.text == '0':
             for son in filenames:
                 fileindex.append(son.text)
                 names.append(son.text)
 
myxmllist = list(names)
myxmllist = sorted(myxmllist)
print(myxmllist)

#DELETE#XML####################################################################
for file in myxmllist:
    xmlarray.append(file.replace("jpg","xml"))


delete_array = [os.path.join(xml_path, name) for name in xmlarray]
print(delete_array)

for filename in delete_array:
    os.remove(filename)
