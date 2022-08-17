import cv2
from cv2 import drawKeypoints
from cv2 import cvtColor 
import numpy as np

#暴力特征匹配原理
    #它使用第一组中的每个特征的描述子与第二组中的所有特征描述子进行匹配，计算他们之间的差距，然后将最接近一个匹配返回
#OpenCV特征匹配步骤
    #创建匹配器，BFMatcher(normType,crossCheck)
        #normType：NORM_L1，NORM_L2，HAMMING1...
            #NORM_L1：取绝对值进行加法运算
            #NORM_L2：取平方和求开方，欧式距离
            #HAMMING1：通过二进制位对比
        #crossCheck：是否进行交叉匹配，默认是false
    #进行特征匹配，bf.mathc(des1,des2)
        #参数为SIFT,SURF,ORB等计算的描述子
    #绘制匹配点，cv2.drawMatches(img1,kp1,img2,k2...)
        #搜索img，kp
        #匹配图img，kp
        #match()方法返回的匹配结果

img1 = cv2.imread("test_opencv\opencv_search.png")

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2 = cv2.imread("test_opencv\opencv_orig.png")

gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#创建sift对象
sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(gray1,None)

kp2,des2 = sift.detectAndCompute(gray2,None)

bf = cv2.BFMatcher(cv2.NORM_L1)

match = bf.match(des1,des2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,match,None)

cv2.imshow('img3',img3)
cv2.waitKey(0)