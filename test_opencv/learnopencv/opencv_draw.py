import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)

#画线，坐标点为（x,y）
#图像，起点坐标，终点坐标，颜色，线的粗细，线型锯齿（越大越平滑,4,8,16）
cv2.line(img,(10,20),(300,400),(0,0,255),5)
cv2.imshow("img",img)
cv2.waitKey(0)