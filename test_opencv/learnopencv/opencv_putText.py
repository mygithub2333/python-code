import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#画文本
cv2.putText(img,"hello world",(22,400),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,0,255))
cv2.imshow('img',img)

cv2.waitKey(0)