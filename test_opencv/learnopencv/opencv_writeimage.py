import cv2


cv2.namedWindow('img',cv2.WINDOW_NORMAL)

img = cv2.imread("./1.png")
while True:
    cv2.imshow('img',img);
    key = cv2.waitKey(0)
    if(key & 0xFF == ord('q')):
        print(123)
        break
    elif(key & 0xFF == ord('s')):
        print('sss')
        cv2.imwrite("D:\\fwx\\pic\\3.jpg",img)
    else:
        print(key)
cv2.destroyAllWindows() 