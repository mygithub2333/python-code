#大作业，添加水印
#1.引入一副图片
#2.要有一个logo，需要自己创建
#3.计算图片在什么地方添加，在添加的地方变成黑色
#4.利用add，将logo与图片叠加到一起
import cv2
import numpy as np

#导入图片
cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')
#创建logo
logo = np.zeros((200,200,3),np.uint8)
mask = np.zeros((200,200),np.uint8)

#绘制logo
logo[20:120,20:120] = [0,0,255]
logo[80:180,80:180] = [0,255,0]

mask[20:120,20:120] = 255
mask[80:180,80:180] = 255
cv2.imshow('logo',logo)
cv2.imshow('mask',mask)
#对mask按位求反
m = cv2.bitwise_not(mask)
cv2.imshow('m',m)
#选择cat添加logo的位置
roi = cat[0:200,0:200]
#与m进行与操作
tmp = cv2.bitwise_and(roi,roi,mask = m)
cv2.imshow('tmp',tmp)
dst = cv2.add(tmp,logo)
cv2.imshow('dst',dst)
cat[0:200,0:200] = dst

cv2.imshow('cat',cat)



cv2.waitKey(0)