import cv2
import numpy as np
import time
def Delay() -> bool:
    time.sleep(0.07)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        return False
    return True



capture = cv2.VideoCapture(1)
alpha = True
try:
    while Delay():
        ret, img = capture.read()
        FullCropped = img[370:470,230:330]
        main  = cv2.cvtColor(FullCropped, cv2.COLOR_BGR2GRAY)
        main = cv2.medianBlur(main,5)
        for layerNum in range(1,5):
            layer = main[(100-layerNum*20-20):100,0:100]
            scale_percent = 400 # percent of original size
            width = int(layer.shape[1] * scale_percent / 100)
            height = int(layer.shape[0] * scale_percent / 100)
            dim = (width, height)
  
            layer = cv2.resize(layer, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(str(layerNum)+'file.jpg',layer)
            cv2.imshow('video',layer)
            molecules = cv2.HoughCircles(layer,cv2.HOUGH_GRADIENT,1,2,param1=50,param2=20,minRadius=0,maxRadius=100)
            if molecules is not None:
                detected = len(np.around(molecules)[0])
            else:
                detected = 0
            print("layer"+str(layerNum)+": "+str(detected))
            Delay()

        
finally:
    capture.release()
    cv2.destroyAllWindows()