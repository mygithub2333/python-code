import cv2
import numpy as np

img = cv2.imread('D:/fwx/code/python-code/test_opencv/j.png')

#kernel = np.ones((5,5),np.uint8)

#腐蚀api
#erode(img,kernel,iterations)
    #kernel：卷积核
    #interations：迭代次数
#获取卷积核
#getStructuringElement(type,size)
#type：卷积核类型
    #MORPH_RECT：矩形
    #MORPH_ELLIPSE：椭圆形
    #MORPH_CROSS：交叉（十字架形）
#Size值为：（3，3）、（5，5）......
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

print(kernel)

dst = cv2.erode(img,kernel,iterations=1)

cv2.imshow('img',img)
cv2.imshow('dst',dst)

cv2.waitKey(0)