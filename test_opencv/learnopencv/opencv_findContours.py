#轮廓查找的API
import cv2
import numpy as np

#findContours(img,mode,approximationMode...)
    #两个返回值，contours(所有轮廓列表)和hierarchy(是否有层级，前后关系)
    #mode
        #RETR_EXTERNAL=0,表示只检测外轮廓
        #RETR_LIST=1,检测的轮廓不建立等级关系
        #RETR_CCOMP=2,每层最多两级
        #RETR_TREE=3,按树形存储轮廓
    #ApproximationMode
        #CHAIN_APPROX_NONE，保存所有轮廓上的点
        #CHAIN_APPROX_SIMPLE，只保存角点

img = cv2.imread("D:/fwx/code/python-code/test_opencv/contours1.jpeg")

#获取灰度图片，转变成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#二值化
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)
cv2.imshow('img',img)
cv2.waitKey(0)