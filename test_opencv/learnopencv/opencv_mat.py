import cv2
from cv2 import WINDOW_NORMAL 
import numpy as np 
img= cv2.imread("./45.jpg")

#浅拷贝
img2= img

#深拷贝
img3 = img.copy()
img[10:100,10:100] = [0,0,255]

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',(480,640))
cv2.imshow("img",img)

cv2.namedWindow('img2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img2',(480,640))
cv2.imshow("img2",img2)

cv2.namedWindow('img3',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img3',(480,640))
cv2.imshow("img3",img3)
cv2.waitKey(0)