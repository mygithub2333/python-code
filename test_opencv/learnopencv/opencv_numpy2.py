import numpy as np
import cv2

img = np.zeros((480,640,3),np.uint8)

print(img[100,100])
count = 0

while count<200:
    #img[count,100,1] = 255
    img[count,100] = [255,22,255]
    count = count +1
cv2.imshow("img",img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows