import cv2 
import numpy as np
#Shi-Tomasi角点检测
#Shi-Tomasi角点检测API
    #goodFeaturesToTrack(img,maxCorners,...)
        #maxCorners：角点的最大数，值为0表示无限制
        #qualityLevel：小于1.0的正数，一般在0.01-0.1之间
        #minDistance：角之间最小欧式距离，忽略小于此距离的点
        #mask：感兴趣的区域
        #blockSize：检测窗口
        #useHarrisDetector：是否使用Harris算法
        #k：默认是0.04

maxCorners = 1000
ql = 0.01
minDistance = 10
img = cv2.imread("test_opencv\chess.png")

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Shi-Tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray,maxCorners,ql,minDistance)
corners = np.int0(corners)


for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)