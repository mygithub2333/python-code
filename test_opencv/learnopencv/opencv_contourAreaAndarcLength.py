#轮廓面积和周长
import cv2
import numpy as np

#contourArea(contour) 轮廓的面积
    #contour：轮廓
#arcLength(curve,closed)
    #curve：轮廓
    #closed：是否是闭合的轮廓
img = cv2.imread("D:/fwx/code/python-code/test_opencv/contours1.jpeg")

#获取灰度图片，转变成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#二值化
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#绘制轮廓
cv2.drawContours(img,contours,-1,(0,0,255),1)

#计算面积
area =cv2.contourArea(contours[2])
print("area=%d"%(area))
#计算周长
len = cv2.arcLength(contours[0],False)
print("len=%d"%(len))