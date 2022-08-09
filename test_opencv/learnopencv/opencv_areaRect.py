#最小外接矩形，最大外接矩形
import cv2
from cv2 import boundingRect
import numpy as np

#minAreaRect(points) 最小外接矩形
    #points：轮廓
    #返回值：RotatedRect
        #x,y 起始点
        #width,height 宽高
        #angle 角度
#boundingRect(array) 最大外接矩形
    #array：轮廓
    #返回值：Rect 
        #x,y 起始点
        #width，height 宽高

img = cv2.imread('D:/fwx/code/python-code/test_opencv/hello.jpeg')

#获取灰度图片，转变成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#二值化
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#最小外接矩形
r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
#最大外接矩形
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)