import cv2
from cv2 import cvtColor
from cv2 import Algorithm
import numpy as np

#FLANN优缺点
    #在进行批量特征匹配时，FLANN速度更快
    #由于它使用的是邻近近似值，所以精度较差
#FLANN特征匹配的步骤
    #创建FLANN匹配器，FlannBasedMatcher(...)
        #参数：
            #index_params字典：匹配算法，KDTREE,LSH
                #index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
            #search_params字典：指定KDTREE算法中遍历树的次数
                #search_params = dict(checks = 50)
    #进行特征匹配，flann.match/knnMatch(...)
        #参数：
            #参数为SIFT,SURF,ORB等计算的描述子
            #k,表示取欧式距离最近的前k个关键点
            #返回的是匹配的结果DMatch对象
                #distance,描述子之间的距离，值越低越好
                #queryIdx,第一个图像的描述子索引值
                #trainIdx,第二个图的描述子索引值
                #imgIdx,第二个图的索引值
    #绘制匹配点，cv2.drawMatches/drawMatchesKnn(...)
        #参数：
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

#创建匹配器
index_params = dict(algorithm=1,trees=5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params,search_params)

matchs = flann.knnMatch(des1,des2,k=2)
good = []
for i,(m,n) in enumerate(matchs):
    if m.distance<0.7*n.distance:
        good.append(m)

ret = cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)
cv2.imshow('result',ret)
cv2.waitKey(0)