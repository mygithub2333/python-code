import cv2
import numpy as np

back = cv2.imread('D:/fwx/code/python-code/test_opencv/back2.jpeg')
cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')


#图像溶合
result = cv2.addWeighted(cat,0.7,back,0.3,0)
cv2.imshow('add2',result)
cv2.waitKey(0)