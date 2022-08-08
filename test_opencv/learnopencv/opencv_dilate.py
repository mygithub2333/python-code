#膨胀
import cv2
import numpy as np

img = cv2.imread('D:/fwx/code/python-code/test_opencv/j.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

dst1 = cv2.erode(img,kernel,iterations=1)

dst = cv2.dilate(dst1,kernel,iterations=1)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)