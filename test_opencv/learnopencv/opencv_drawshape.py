#基本功能：
#可以通过鼠标进行基本图形的绘制
#可以画线：当用户按下l键，即选择了画线，此时，滑动鼠标即可画线。
#可以画圆：当用户按下c键，即选择了画圆，此时，滑动鼠标即可画圆。
#可以画矩形：当用户按下r键，即选择了画矩形，此时，滑动鼠标即可矩形。
#......
import cv2
import numpy as np
#curshape：0-drawline,1-drawrectangle,2-drawcircle
curshape = 0
startpos = (0,0)

img = np.zeros((480,640,3),np.uint8)

def mouse_callback(event,x,y,flags,userdata):
    global curshape,startpos
    #print(event,x,y,flags,userdata)
    if(event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x,y)
    elif(event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if(curshape==0):
            cv2.line(img,startpos,(x,y),(0,0,255))
        elif (curshape == 1):
            cv2.rectangle(img,startpos,(x,y),(0,0,255))
        elif(curshape == 2):
            a=(x-startpos[0])
            b=(y-startpos[1])
            r=int((a**2+b**2)**0.5)
            cv2.circle(img,startpos,r,(0,0,255))

cv2.namedWindow('drawshape',cv2.WINDOW_NORMAL)

img = np.zeros((480,640,3),np.uint8)

cv2.setMouseCallback('drawshape',mouse_callback)

while True:
    cv2.imshow('drawshape',img)
    key = cv2.waitKey(1) & 0xFF
    if key ==ord('q'):
        break
    elif key == ord("l"):
        curshape = 0
    elif key == ord("r"):
        curshape = 1
    elif key ==ord("c"):
        curshape = 2

cv2.destroyAllWindows

