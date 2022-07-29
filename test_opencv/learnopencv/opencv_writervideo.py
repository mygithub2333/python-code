import cv2
from cv2 import VideoCapture

#创建VideoWriter为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#vw = cv2.VideoWriter('./33.avi',fourcc,30,(1280, 720))

#创建窗口
#cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow('video',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('video',640,480)
cap = cv2.VideoCapture(0)
hegiht = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
vw = cv2.VideoWriter('./33.avi',fourcc,25,(640, 480))
#判断摄像头是否为打开状态
while cap.isOpened():
    #从摄像头读取视频帧
    ret, frame = cap.read()
    if ret ==True:
        #将视频帧在窗口显示
        cv2.imshow('video',frame)

        #写数据到多媒体文件
        vw.write(frame)

        #等待键盘事件，如果为q,退出
        key = cv2.waitKey(1)
        if(key & 0xFF == ord('q')):
            break
    else:
        break

#释放videoCapture
cap.release()

#释放videoWriter
vw.release()

cv2.destroyAllWindows()
