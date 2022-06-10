import cv2
import numpy as np
import time

from sympy import exp
def Delay() -> bool:
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        return False
    return True


experimentNum = 1
capture = cv2.VideoCapture(1)
alpha = True
try:
    while Delay():
        ret, img = capture.read()
        FullCropped = img[370:470,230:330]
        scale_percent = 400 # percent of original size
        width = int(FullCropped.shape[1] * scale_percent / 100)
        height = int(FullCropped.shape[0] * scale_percent / 100)
        dim = (width, height)
        FullCropped = cv2.resize(FullCropped, dim, interpolation = cv2.INTER_AREA)
        for layerNum in range(1,5):
            start_point = (0,(layerNum)*100)
            end_point = (400,layerNum*100)
            color = (0,0,0)
            thickness = 3
            FullCropped = cv2.line(FullCropped, start_point, end_point, color, thickness)
            
            cv2.imshow('count',FullCropped)
            path = "V2"+str(experimentNum)+"f.jpg"

            cv2.imwrite(path,FullCropped)
        alpha = 0 
        while not (cv2.waitKey(1) & 0xFF == ord('n')):
            alpha+=1
        experimentNum+=1 
        print(experimentNum)
finally:
    capture.release()
    cv2.destroyAllWindows()