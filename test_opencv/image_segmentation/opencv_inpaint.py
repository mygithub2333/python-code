#图片修复
#inpaint API
    #inpaint(img,
    #           mask,
    #           inpaintRadius,//每个点的圆形领域半径
    #           flags)//INPAINT_NS,INPAINT_TELEA

import cv2
import numpy as np

img = cv2.imread('test_opencv\inpaint.png')
mask = cv2.imread('test_opencv\inpaint_mask.png',0)

dst = cv2.inpaint(img,mask,5,cv2.INPAINT_TELEA)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)