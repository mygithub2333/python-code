#绘制轮廓API
import cv2
import numpy as np

#drawContours(img,contours,contourIDx,color,thickness ...)
    #contourIdx，-1表示绘制所有轮廓
    #color，颜色（0，0，255）
    #thickness，线宽，-1是全部填充

img = cv2.imread("D:/fwx/code/python-code/test_opencv/contours1.jpeg")

#获取灰度图片，转变成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#二值化
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#绘制轮廓
cv2.drawContours(img,contours,-1,(0,0,255),1)

cv2.imshow('img',img)
cv2.waitKey(0)