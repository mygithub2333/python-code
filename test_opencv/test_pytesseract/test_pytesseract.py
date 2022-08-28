import cv2
import pytesseract
from PIL import Image

#filePath = "test_opencv\\test_pytesseract\\test_pytesseract.png"
filePath = "test_opencv\\test_pytesseract\\test2.jpg"
img = Image.open(filePath)
tessdata_dir_config = '--tessdata-dir "D:\\fwx\\devTools\\tesseract-ocr\\tessdata" --psm 6'
print(pytesseract.image_to_string(img,lang="chi_sim",config=tessdata_dir_config))