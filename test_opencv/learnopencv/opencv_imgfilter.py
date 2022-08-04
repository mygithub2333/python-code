#图的卷积
#低通滤波
import cv2
from cv2 import boxFilter
import numpy as np

#img= cv2.imread("D:/fwx/code/python-code/test_opencv/cat.jpeg")
#img= cv2.imread("D:/fwx/code/python-code/test_opencv/gaussian.png")
#img= cv2.imread("D:/fwx/code/python-code/test_opencv/papper.png")
img= cv2.imread("D:/fwx/code/python-code/test_opencv/lena.png")
#kernal = np.ones((5,5),np.float32)/25

#dst = cv2.filter2D(img,-1,kernal)
#方盒滤波
#boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
#均值滤波
#blur(src,ksize,anchor,borderType)
#dst = cv2.blur(img,(5,5))
#高斯滤波
#GaussianBlur(src,kernel,sigmaX,sigmaY,...)
#dst = cv2.GaussianBlur(img,(5,5),sigmaX=1)
#中值滤波 可以解决胡椒噪音
#medianBlur(img,ksize)
#dst = cv2.medianBlur(img,5)
#双边滤波
#bilateralFilter(img,d,sigmaColor,sigmaSpace,...)
#sigmaColor和sigmaSpace可以参见lec14_bilateral_4up.pdf
dst = cv2.bilateralFilter(img,7 ,20,50)
cv2.imshow('dst',dst)
cv2.imshow('img',img)
cv2.waitKey(0)