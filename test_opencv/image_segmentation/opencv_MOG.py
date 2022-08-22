#MOG去背景
    #混用高斯模型为基础的前景/背景分割算法
    #createBackgroundSubtractorMOG(history,//默认200
    #                               nmixtures,//高斯范围值，默认5
    #                               backgroundRatio,//背景比率，默认0.7
    #                               noiseSigma//默认0，自动降噪)
#MOG2去背景
    #createBackgroundSubtractorMOG2(history,//200毫秒
    #                                   ...
    #                                   detectShadows//是否检测阴影，True)
#GMG去背景
    #静态背景图像估计和每个像素的贝叶斯分割，抗噪性更强
    #createBackgroundSubtractorGMG(initializationFrames,//初始帧数，120,...)
import cv2
import numpy as np

cap = cv2.VideoCapture("test_opencv/vtest.avi")
#mog = cv2.bgsegm.createBackgroundSubtractorMOG()
#好处可以检测出阴影部分
#缺点会产生很多噪点
#mog2 = cv2.createBackgroundSubtractorMOG2()
#好处可以算出阴影部分，同时减少了噪点
#缺点是采用默认值的话，则在很长时间没任何信息，解决方法，调整初始帧数
gmg = cv2.bgsegm.createBackgroundSubtractorGMG(10)
while(True):
    ret,frame = cap.read()
    fgmask = gmg.apply(frame)

    cv2.imshow('img',fgmask)
    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()