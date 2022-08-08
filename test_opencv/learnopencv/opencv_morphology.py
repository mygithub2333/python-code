#开闭运算，形态学梯度，顶帽和黑帽
#morphologyEx(img,MORPH_OPEN,kernel)

import cv2
from cv2 import MORPH_OPEN
from cv2 import MORPH_TOPHAT
from cv2 import MORPH_BLACKHAT
import numpy as np

#img = cv2.imread('D:/fwx/code/python-code/test_opencv/j.png')
#img = cv2.imread('D:/fwx/code/python-code/test_opencv/tophat.png')
img = cv2.imread('D:/fwx/code/python-code/test_opencv/dotinj.png')
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(19,19))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
#dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
#MORPH_OPEN 开运算 （先腐蚀后膨胀）去除大图形外的小图形 
#MORPH_CLOSE 闭运算 （先膨胀后腐蚀）去除大图形内的小图形 
#MORPH_GRADIENT 形态学梯度 梯度=原图-腐蚀 求图形的边缘
#MORPH_TOPHAT 顶帽 = 原图-开运算 得到大图形外的小图形
#MORPH_BLACKHAT 黑帽 = 原图-闭运算 得到大图形内的小图形
#dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
#dst = cv2.morphologyEx(img,MORPH_TOPHAT,kernel)
dst = cv2.morphologyEx(img,MORPH_BLACKHAT,kernel)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)