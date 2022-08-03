import cv2
import numpy as np

context = cv2.imread('D:/fwx/code/python-code/test_opencv/1.png')

#print(img.shape)
#图的加法运算就是矩阵的加法运算
img = np.ones((358,640,3),np.uint8)*10


cv2.imshow('orig',context)

result = cv2.add(context,img)

#cv2.imshow('result',result)

#减法
orig_1 = cv2.subtract(result,img)

#orig_1 = cv2.subtract(context,img)
#cv2.imshow('orig_1',orig_1)

#乘法
orig_2 = cv2.multiply(context,img)
cv2.imshow('orig_2',orig_2)
#除法
orig_3 = cv2.divide(orig_2,img)
cv2.imshow('orig_3',orig_3)

cv2.waitKey(0)