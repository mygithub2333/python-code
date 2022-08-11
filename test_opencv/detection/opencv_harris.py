#Harris角点检测API
#cornerHarris(img,dst,blockSize,ksize,k)
    #blockSize：检测窗口大小
    #ksize：Sobel的卷积核
    #k：权重系数，经验值，一般取0.02~0.04之间
import cv2 
import numpy as np

blockSize = 2
ksize = 3
k = 0.04
img = cv2.imread("test_opencv\chess.png")

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#harris角点检测
dst = cv2.cornerHarris(gray,blockSize,ksize,k)

#harris角点的展示
img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('img',img)
cv2.waitKey(0)