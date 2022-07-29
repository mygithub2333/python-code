import cv2
from cv2 import imshow
import numpy as np

img = np.zeros((480,640,3),np.uint8)


#分割图片获取到b,g,r
b,g,r = cv2.split(img)

b[10:100,10:100] = 255
g[10:100,10:100] = 255

#合并b,g,r
img2 = cv2.merge((b,g,r))

cv2,imshow('img',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('img2',img2)
cv2.waitKey(0)