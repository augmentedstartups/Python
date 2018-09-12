##########################################
#Created by :  R Kanjee
#Description:  LabelNet forgets to record the resolutions on some images
#               This scripts fills in the blanks of the missing resolutions
###########################################
import os
from xml.etree import ElementTree
from PIL import Image

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

#GET#RESOLUTION#FROM#JPEG####################################################################
JPEG_path = ("C:/Users/OSS_FPGA/Documents/YOLO/darkflow-master/new_model_data/CNN_Armed_people/JPEG/")
jpeg_array = [f for f in os.listdir(JPEG_path) if f.endswith('.jpg')]
jpeg_array.sort() # file is sorted list
jpeg_array = [os.path.join(JPEG_path, name) for name in myxmllist]

for filename in jpeg_array: 
    im = Image.open(filename)    
    width, height = im.size
    new_width.append(width);
    new_height.append(height);
    print (width,height,im.filename)

#REPLACE##XML#MISSING#DATA###################################################################  
for file in myxmllist:
    xmlarray.append(file.replace("jpg","xml"))

xml_sorted_array = [os.path.join(xml_path, name) for name in xmlarray]

hx=0
wx=0
for filename in xml_sorted_array:
     root = ElementTree.parse(filename)
     xml_height = root.findall('size/height')
     xml_width = root.findall('size/width')
     for child in xml_height:
         child.text = str(new_height[hx])
         hx += 1
     for child in xml_width:
         child.text = str(new_width[wx])
         wx += 1    
     root.write(filename)    



