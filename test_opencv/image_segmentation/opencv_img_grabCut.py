import cv2
import numpy as np
#GrabCut API
    #grabCut(img,mask,rect,bgdModel,fgbModel,5(//iterator),mode)
        #mask，生产的掩码
            #BGD:背景，0
            #FGD:前景，1
            #PR_BGD:可能是背景，2
            #PR_FGB:可能是前景，3
        #model:
            #bgdModel,np.float64 type zero arrays of size (1,65)
            #fgdModel,同上
        #mode:
            #GC_INIT_WITH_RECT
            #GC_INIT_WITH_MASK

class App:

    startX = 0
    startY = 0
    rect = (0,0,0,0)
    flag_rect = False

    def onmouse(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
        elif event == cv2.EVENT_LBUTTONUP:
            self.flag_rect = False
            cv2.rectangle(self.img,
                            (self.startX,self.startY),
                            (x,y),
                            (0,0,255),
                            3)
            self.rect = (min(self.startX,x),min(self.startY,y),abs(self.startX-x),abs(self.startY-y))
            print(self.rect)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect == True:
                self.img = self.img2.copy()
                cv2.rectangle(self.img,
                                (self.startX,self.startY),
                                (x,y),
                                (255,0,0),
                                3)
    
    def run(self):
        print("run...")

        cv2.namedWindow('input')
        cv2.setMouseCallback('input',self.onmouse)
        self.img = cv2.imread("test_opencv\lena.png")
        self.img2 = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2],dtype=np.uint8)
        self.output = np.zeros(self.img.shape,np.uint8)
        while(1):
            cv2.imshow('input',self.img)
            cv2.imshow('output',self.output)
            k = cv2.waitKey(100)
            if k ==27:
                break
            if k == ord('g'):
                bgdModel=np.zeros((1,65),np.float64)
                fgdModel=np.zeros((1,65),np.float64)
                cv2.grabCut(self.img2,
                            self.mask,
                            self.rect,
                            bgdModel,fgdModel,
                            1,
                            cv2.GC_INIT_WITH_RECT)
            mask2 = np.where((self.mask == 1)|(self.mask==3),255,0).astype('uint8')
            self.output = cv2.bitwise_and(self.img2,self.img,mask = mask2)

App().run()