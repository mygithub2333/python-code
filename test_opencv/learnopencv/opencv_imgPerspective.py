import cv2
import numpy as np

perspective = cv2.imread('D:/fwx/code/python-code/test_opencv/perspective.jpeg')
#warpPerspective(img.M.dsize,...)
    #M：变换矩阵
        #getPersectiveTransform(src,dst) 四个点（图像的四个角）
        #src：源
        #dst：目标
    #dsize：目标图像大小
    #......
perspective = cv2.resize(perspective,None,fx=0.2,fy=0.2)
src = np.float32([[10,110],[210,110],[0,400],[250,390]])*2
dst = np.float32([[0,0],[230,0],[0,300],[230,300]])*2
M = cv2.getPerspectiveTransform(src,dst)
new = cv2.warpPerspective(perspective,M,(230*2,300*2))
cv2.imshow('orgin',perspective)
cv2.imshow('new',new)
cv2.waitKey(0)