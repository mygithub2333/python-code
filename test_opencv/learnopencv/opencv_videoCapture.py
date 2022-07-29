from asyncore import read
from tkinter.tix import Tree
from typing import Tuple
import cv2
from cv2 import VideoCapture

#创建窗口
#cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
cap = cv2.VideoCapture(0)

while True:
    #从摄像头读取视频帧
    ret, frame = cap.read()

    #将视频帧在窗口显示
    cv2.imshow('video',frame)

    #等待键盘事件，如果为q,退出
    key = cv2.waitKey(1)
    if(key & 0xFF == ord('q')):
        break

#释放videoCapture
cap.release()
cv2.destroyAllWindows()
