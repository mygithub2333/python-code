import cv2

#读取图片
img = cv2.imread("D:\\fwx\\pic\\1.png")

#展示图片
cv2.imshow('img',img)
 
cv2.waitKey(0)
