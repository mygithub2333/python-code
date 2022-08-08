import cv2
import numpy as np

img = cv2.imread("D:/fwx/code/python-code/test_opencv/perspective.jpeg")

perspective = cv2.resize(img,None,fx=0.2,fy=0.2)

img1 = cv2.cvtColor(perspective,cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,0)
#adaptiveThreshold(img,maxVal,adaptiveMethod,type,blockSize,C)
    #adaptiveMethod：计算阈值的方法
        #ADAPTIVE_THRESH_MEAN_C：计算邻近区域的平均值
        #ADAPTIVE_THRESH_GAUSSIAN_C：高斯窗口加权平均值
    #type：
        #THRESH_BINARY
        #THRESH_BINARY_INV
    #blockSize：邻近区域的大小
    #C：常量，应计算出的平均值或加权平均值中减去

cv2.imshow('img',perspective)

cv2.imshow('gray',img1)
cv2.imshow('bin',dst)

cv2.waitKey(0)