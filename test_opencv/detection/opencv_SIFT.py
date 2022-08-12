from cgi import print_directory
import cv2
from cv2 import drawKeypoints 
import numpy as np
#SIFT(Scale-Invariant Feature Transform)
#使用SIFT的步骤
    #创建SIFT对象 cv2.xfeatures2d.SIFT_create()
    #进行检测，kp = sift.detect(img,...)
    #绘制关键点，drawKeypoints(gray,kp,img)
#计算描述子
    #kp,des = sift.compute(img,kp)
    #其作用是进行特征匹配
#同时计算关键点和描述
    #kp,des = sift.detectAndCompute(img,...)
    #mask：指明对img中哪个区域进行计算
img = cv2.imread("test_opencv\chess.png")

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
#进行检测
kp,des = sift.detectAndCompute(gray,None)
#kp = sift.detect(gray,None)

print(des[0])
cv2.drawKeypoints(gray,kp,img)
cv2.imshow('img',img)
cv2.waitKey(0)