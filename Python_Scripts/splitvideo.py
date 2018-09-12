import cv2
import numpy as np
import os

count = 0
# number of frames to skip
numFrameToSave = 9
# Playing video from file:
cap = cv2.VideoCapture('training.mp4')
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if count < length:
        if (currentFrame % numFrameToSave ==0):
        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        # To stop duplicate images
        currentFrame += 1
        #quit Application
        if cv2.waitKey(1) & 0xFF ==ord('q'):                     
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()