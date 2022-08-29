#DNN使用步骤
    #读取模型，并得到深度神经网络
        #readNetFromTensorflow(model,config)/readNetFromCaffe(config,model)/readNetDarknet,YOLO(config,model)/readNet(model,[config,[framework]])
    #读取图片/视频
    #将图片转成张量，送入深度神经网络
        #blobFromImage(image,scalefactor = 1.0,size = Size(),mean = Scalar(),swapRB = false,crop = false...)
            #将图像转成张量
        #将张量送入网络并执行
            #net.setInput(blob)
            #net.forward()
    #进行分析，并得到结果
import cv2
from cv2 import dnn
from matplotlib.ft2font import BOLD
import numpy as np

#导入模型，创建神经网络
config = "test_opencv\model\bvlc_googlenet.prototxt"
model = "test_opencv\model\opencv_face_detector_fp16.caffemodel"
net = dnn.readNetFromCaffe(config,model)

#读图片，转成张量
img = cv2.imread("test_opencv\smallcat.jpeg")
blob = dnn.blobFromImage(img,
                        1.0,#缩放因子
                        (224,224),
                        (104,117.123))
#将张量送入网络并进行预测
net.setInput(blob)
r = net.forward()

#读入类目
classes = []
path = "test_opencv\model\synset_words.txt"
with open(path,"rt") as f:
    classes = [x [x.find(" ")+1:]for x in f]
order = sorted(r[0],reverse=True)
z = list(range(3))
for i in range(0,3):
    z[i] = np.where(r[0]==order[i])[0][0]
    print("第",i+1+"项，匹配：",classes[z[i]],end="")
    print("类所在行：",z[i]+1,"","可能性",order[i])
