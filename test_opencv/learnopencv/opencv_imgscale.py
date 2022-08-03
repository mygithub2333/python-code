import cv2
import numpy as np

cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')

print(cat.shape)
new = cv2.resize(cat,(240,135))
#缩放算法：
#INTER_NEAREST：邻近插值，速度快，效果差
#INTER_LINEAR：双线性插值，原图中的4个点（默认是这个算法）
#INTER_CUBIC：三次插值，原图中的16个点，速度慢一点
#INTER_AREA：效果最好，也最慢
new = cv2.resize(new,None,fx=3,fy=3,interpolation=cv2.INTER_NEAREST)

cv2.imshow('cat',cat)
cv2.imshow('new',new)

cv2.waitKey(0)