from tkinter.tix import Tree
import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)

#画多边形
pts = np.array([(300,10),(150,100),(450,100)],np.int32)
cv2.polylines(img,[pts],True,(0,0,255))
cv2.fillPoly(img,[pts],(255,0,255))
cv2.imshow('img',img)
cv2.waitKey(0)