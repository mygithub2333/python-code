import cv2
import numpy as np

context = cv2.imread('D:/fwx/code/python-code/test_opencv/1.png')

#print(img.shape)
#图的加法运算就是矩阵的加法运算
img = np.ones((358,640,3),np.uint8)*100

cv2.imshow('orig',context)

result = cv2.add(context,img)

cv2.imshow('result',result)

cv2.waitKey(0)