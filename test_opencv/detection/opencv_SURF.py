#使用SURF的步骤
    #surf = cv2.xfeatures2d.SURF_create()
    #kp,des = surf.detectAndCompute(img,mask) 
import cv2
import numpy as np


#读文件
img = cv2.imread("test_opencv\chess.png")

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#创建SURF对象
surf = cv2.xfeatures2d.SURF_create()

#进行检测
kp,des = surf.detectAndCompute(gray,None)

#绘制keypoints
cv2.drawKeypoints(gray,kp,img)

cv2.imshow('img',img)
cv2.waitKey(0)