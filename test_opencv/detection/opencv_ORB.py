import cv2
from cv2 import drawKeypoints 
import numpy as np

#ORB优势
    #ORB可以做到实时检测
    #ORB = Oriented FAST +Rotated BRIEF
    #FAST 可以做到特征点的实时检测
    #BRIEF BRIEF是对已检测到的特征点进行描述，它加快了特征描述符建立的速度，同时也极大的降低了特征匹配的时间
#使用ORB的步骤
    #orb = cv2.ORB_create()
    #kp,des = orb.detectAndCompute(img,mask)
img = cv2.imread("test_opencv\chess.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#创建ORB对象

orb =  cv2.ORB_create()

#进行检测
kp,des = orb.detectAndCompute(gray,None)

cv2,drawKeypoints(gray,kp,img)

cv2.imshow('img',img)
cv2.waitKey(0)