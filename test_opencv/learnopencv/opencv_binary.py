import cv2
import numpy as np



#threshold(img,thresh,maxVal,type)
    #img：图像，最好是灰度图
    #thresh：阈值
    #maxVal：超过阈值，替换成maxVal
    #type:
        #转换成二值化图
        #THRESH_BINARY和THRESH_BINARY_INV
        #下面不是二值化图
        #THRESH_TRUNC
        #THRESH_TOZERO和THRESH_TOZERO_INV
#img = cv2.imread("D:/fwx/code/python-code/test_opencv/cat.jpeg")
img = cv2.imread("D:/fwx/code/python-code/test_opencv/perspective.jpeg")
perspective = cv2.resize(img,None,fx=0.2,fy=0.2)
img1 = cv2.cvtColor(perspective,cv2.COLOR_BGR2GRAY)

ret,dst = cv2.threshold(img1,180,255,cv2.THRESH_BINARY)

cv2.imshow('img',perspective)
cv2.imshow('gray',img1)
cv2.imshow('dst',dst)
cv2.waitKey(0)