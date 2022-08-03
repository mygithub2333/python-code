import cv2
import numpy as np

cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')
#filp(img,filpCode)
#filpCode == 0 ，上下翻转
#filpCode > 0 ，左右翻转
#filpCode < 0 ，上下+左右翻转
new = cv2.flip(cat,0)

cv2.imshow('cat',cat)
cv2.imshow('new',new)

cv2.waitKey(0)