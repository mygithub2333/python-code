import cv2
import numpy as np


img = np.zeros((480,640,3),np.uint8)

#画矩形
#cv2.rectangle(img,(220,190),(420,290),(0,0,255))
#画圆
cv2.circle(img,(320,240),100,(0,0,255))
cv2.circle(img,(320,240),5,(0,0,255),-1)
#画椭圆
#度是按顺时针计算的
#0度是从右侧开始的
#cv2.ellipse(img,(110,60),(100,50),0,0,360,(0,0,255),-1)
cv2.ellipse(img,(320,240),(100,50),60,0,360,(0,0,255))
cv2.imshow('draw',img)

cv2.waitKey(0)