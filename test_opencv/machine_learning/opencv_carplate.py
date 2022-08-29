import cv2
import numpy as np
import pytesseract


#第一步，创建Haar级联器
plate = cv2.CascadeClassifier('test_opencv\haarcascades\haarcascade_russian_plate_number.xml')
#第二步，导入带车牌图片
img = cv2.imread('test_opencv\chinacar.jpeg')
#车牌定位
#进行灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#检测车牌的位置
plates = plate.detectMultiScale(gray,1.1,3)
for(x,y,w,h) in plates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#对获取到的车牌进行预处理
roi = gray[y:y+h,x:x+w]
ret,roi_bin = cv2.threshold(roi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(pytesseract.image_to_string(roi,lang='chi_sim+eng',config='--psm 8 --oem 3'))
cv2.imshow('roi_bin',roi_bin)
cv2.imshow('img',img)
cv2.waitKey(0)