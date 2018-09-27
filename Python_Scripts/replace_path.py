##########################################
#Created by :  R Kanjee
#Description:  Replace Path
###########################################
import os
from xml.etree import ElementTree
from PIL import Image

names = []
xmlarray = []
NewXMLPath = []
newfile = []
##IDENTIFY#FILES#WITH#MISSING#DATA############################################################
xml_path = ("C:/Users/OSS_FPGA/Documents/YOLO/darkflow-master/new_model_data/CNN_Armed_people/Annotations/")
file_array = [f for f in os.listdir(xml_path) if f.endswith('.xml')]
file_array.sort() # file is sorted list
file_array = [os.path.join(xml_path, name) for name in file_array]

JPEG_path = ("C:/Users/OSS_FPGA/Documents/YOLO/darkflow-master/new_model_data/CNN_Armed_people/JPEG/")
jpeg_array = [f for f in os.listdir(JPEG_path) if f.endswith('.jpg')]
jpeg_array.sort() # file is sorted list
jpeg_array = [os.path.join(JPEG_path, name) for name in jpeg_array]
hx=0
for filename in file_array:
     root = ElementTree.parse(filename)
     new_xml_path = root.findall('path')
     for child in new_xml_path:
         names.append(child.text)
         

myxmllist = list(names)
myxmllist = sorted(myxmllist)


for file in myxmllist:
    xmlarray.append(file.replace("E:\\Nhlakanipho\\CSIR\\CNN Armed people recognition\\CNN_Armed_people","C:\\Users\\OSS_FPGA\\Documents\\YOLO\\darkflow-master\\new_model_data\\CNN_Armed_people\\JPEG"))

hx=0  
     #root.write(filename)    
for filename in file_array:
     root = ElementTree.parse(filename)
     new_xml_path = root.findall('path')

     for child in new_xml_path:
         child.text = (xmlarray[hx])
         print(xmlarray[hx])
         hx += 1
     root.write(filename) 
         
