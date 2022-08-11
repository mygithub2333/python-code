import cv2
from cv2 import drawKeypoints 
import numpy as np
#SIFT(Scale-Invariant Feature Transform)
#使用SIFT的步骤
    #创建SIFT对象 cv2.xfeatures2d.SIFT_create()
    #进行检测，kp = sift.detect(img,...)
    #绘制关键点，drawKeypoints(gray,kp,img)
img = cv2.imread("test_opencv\chess.png")

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

cv2.drawKeypoints(gray,kp,img)
cv2.imshow('img',img)
cv2.waitKey(0)