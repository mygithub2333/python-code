#图的卷积
#高通滤波 边缘检测
    #Sobel（索贝尔）（高斯） 
    #Scharr（沙尔）
        #与Sobel类似，只不过使用的kernel值不同
        #Scharr只能求x方向或y方向的边缘
    #Laplacian（拉普拉斯）
        #可以同时求两个方向的边缘
        #对噪音敏感，一般需要先进行去噪再调用拉普拉斯
#Canny
    #使用5x5高斯滤波消除噪声
    #计算图像梯度的方向（0°/45°/90°/135°）
    #取局部极大值
    #阈值计算
import cv2
import numpy as np
#img = cv2.imread("D:/fwx/code/python-code/test_opencv/chess.png")

img = cv2.imread("D:/fwx/code/python-code/test_opencv/lena.png")
#Sobel API
#Sobel(src,ddepth,dx,dy,ksize=3,scale=1,delta=0,borderType=BORDER_DEFAULT) 当ksize = -1 等于使用Scharr
#Scharr(src,ddepth,dx,dy,scale=1,delta=0,borderType=BORDER_DEFAULT)
#Laplacian(img,ddepth,ksize=3,scale=1,borderType=BORDER_DEFAULT)
#索贝尔算子y方向边缘
#d1 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#沙尔算子y方向边缘
#d1 = cv2.Scharr(img,cv2.CV_64F,1,0)
#索贝尔算子x方向边缘
#d2 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
#沙尔算子x方向边缘
#d2 = cv2.Scharr(img,cv2.CV_64F,0,1)
#相加
#dst = d1+d2
#dst = cv2.add(d1,d2)

#拉普拉斯
#ldst = cv2.Laplacian(img,cv2.CV_64F,ksize=5)
#Canny
#Canny(img,minVal,maxVal,...)
dst = cv2.Canny(img,100,200)
cv2.imshow('img',img)
#cv2.imshow('d1',d1)
#cv2.imshow('d2',d2)
cv2.imshow('dst',dst)
#cv2.imshow('ldst',ldst)
cv2.waitKey(0)
