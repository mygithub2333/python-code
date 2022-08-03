import cv2
import numpy as np

cat = cv2.imread('D:/fwx/code/python-code/test_opencv/cat.jpeg')

#warpAffine(src,M,dsize,flags,mode,value)
#M：变换矩阵
    #getRotationMatrix2D(center,angle,scale)
        #center：中心点 （x,y）
        #angle：角度  旋转的角度为逆时针
        #scale：缩放比例
    #getAffineTransform(src[],dst[]) 可以通过三个点确定变换的位置
        #src[]：源坐标点
        #dst[]：目标坐标点
#dsize：输出尺寸大小
#flags：与resize中的插值算法一致
#mode：边界外推法标志
#value：填充边界的值

#平移矩阵
#M = np.float32([[1,0,300],[0,1,0]])
h,w,ch = cat.shape
#M = cv2.getRotationMatrix2D((w/2,h/2),15,0.3)
src = np.float32([[400,300],[500,300],[400,1000]])
dst = np.float32([[200,400],[300,500],[150,1100]])
M = cv2.getAffineTransform(src,dst)
#如果想改变新图的尺寸，需要改动dsize
new = cv2.warpAffine(cat,M,(w,h))

cv2.imshow('cat',cat)
cv2.imshow('new',new)

cv2.waitKey(0)