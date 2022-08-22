import cv2
from cv2 import pyrMeanShiftFiltering
import numpy as np

#meanshiftAPI （基于色彩进行分割）
    #pyrMeanShiftFiltering(img,double sp,double sr,maxLevel = 1,termcrit = TermCriteria...)
        #sp:半径
        #sr:色彩幅值
img = cv2.imread("test_opencv\\key.png")

mean_img = cv2.pyrMeanShiftFiltering(img,20,30)
canny_img = cv2.Canny(mean_img,150,300)

contours,_ = cv2.findContours(canny_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),2)

cv2.imshow('img',img)
cv2.imshow('mean_img',mean_img)
cv2.imshow('canny_img',canny_img)
cv2.waitKey(0)