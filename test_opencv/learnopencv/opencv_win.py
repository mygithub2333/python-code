import cv2

#新建一个窗口
cv2.namedWindow('new',cv2.WINDOW_NORMAL)
#设置窗口大小
cv2.resizeWindow('new', 640,480)
#展示图片
cv2.imshow("new",0)

key = cv2.waitKey(0)

if(key == 'q'):
    exit()
#清除所有窗口资源
cv2.destroyAllWindows()