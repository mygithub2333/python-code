#基本功能：
#可以通过鼠标进行基本图形的绘制
#可以画线：当用户按下l键，即选择了画线，此时，滑动鼠标即可画线。
#可以画圆：当用户按下c键，即选择了画圆，此时，滑动鼠标即可画圆。
#可以画矩形：当用户按下r键，即选择了画矩形，此时，滑动鼠标即可矩形。
#......
import cv2
import numpy as np


cv2.namedWindow('drawshape',cv2.WINDOW_NORMAL)