import cv2
from cv2 import cvtColor
from cv2 import Algorithm
import numpy as np

#图像查找
    #特征匹配+单应性矩阵

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



if len(good) >=4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

    #获取单应性矩阵
    H,_ = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5.0)
    h,w = img1.shape[:2]
    pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,H)

    cv2.polylines(img2,[np.int32(dst)],True,(0,0,255))
else:
    print("the number of good is less than 4.")
    exit()
ret = cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)
cv2.imshow('result',ret)
cv2.waitKey(0)