import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import matplotlib.pyplot as plt


options = { 
        'model': 'cfg/tiny-yolo-voc.cfg',
        'load': 'bin/yolov2-tiny-voc.weights',
        'threshold': 0.3,
        'gpu': 0.8
        }

options1 = { 
        'model': 'cfg/tiny-yolo-voc-1c.cfg',
        'load': 2000,
        'threshold': 0.05,
        'gpu': 0.8
        }

tfnet = TFNet(options1)

count = 0
capture =cv2.VideoCapture('AC2.mp4')
colors = [tuple(255* np.random.rand(3)) for i in range(5)]
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))


while(capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)
    
    if ret:
        for color, result in zip(colors, results): # Makes a list of item of tuple one color one result
            tl = result['topleft']['x'], result['topleft']['y']
            br = result['bottomright']['x'], result['bottomright']['y']
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame,tl,br,color,7) 
            frame = cv2.putText(frame,text,tl, cv2.FONT_HERSHEY_COMPLEX, 1, color,2)  # font scale
        cv2.imshow('frame',frame)
        count = count + 1
        try:
            z = 1/ (time.time()-stime)
            print('FPS{:.1f}'.format(z))
        except ZeroDivisionError:
            z = 0    
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        if count >= length:
            break


capture.release()
cv2.destroyAllWindows()





