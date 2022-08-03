import cv2
import numpy as np

cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')
#rotate(img,rotateCode)
#ROTATE_90_CLOCKWISE
#ROTATE_180
#ROTATE_90_COUNTERCLOCKWISE

new = cv2.rotate(cat,cv2.ROTATE_180)

cv2.imshow('cat',cat)
cv2.imshow('new',new)

cv2.waitKey(0)