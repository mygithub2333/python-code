#Haar人脸识别API
#        detectMultiScale(img,
#                        double scaleFactor = 1.1,
#                       int minNeighbors = 3,
#                       ...)

import cv2
import numpy as np

#第一步，创建Haar级联器
facer = cv2.CascadeClassifier('test_opencv\haarcascades\haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('test_opencv\haarcascades\haarcascade_eye.xml')
mouth = cv2.CascadeClassifier('test_opencv\haarcascades\haarcascade_mcs_mouth.xml')
nose = cv2.CascadeClassifier('test_opencv\haarcascades\haarcascade_mcs_nose.xml')
#第二步，导入人脸识别的图片进行灰度化
img = cv2.imread('test_opencv\p3.png')
#只能对正面人脸识别 侧着识别不到
#img = cv2.imread('test_opencv\\face.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#第三步，进行人脸识别
#[[x,y,w,h]]
faces = facer.detectMultiScale(gray,1.1,3)
i = 0
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_img = img[y:y+h,x:x+w]
    eyes = eye.detectMultiScale(gray,1.1,3)
    for(x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    i = i+1
    winname = 'face'+str(i)
    cv2.imshow(winname,roi_img)

# mouths = mouth.detectMultiScale(gray,1.1,3)

# for(x,y,w,h) in mouths:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# noses = nose.detectMultiScale(gray,1.1,3)

# for(x,y,w,h) in noses:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)