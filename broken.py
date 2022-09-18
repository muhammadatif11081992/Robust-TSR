from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
import os
import cv2


directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/5'
for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            f=os.path.join(directory, filename)
            img = Image.open(f).convert('RGBA')
            for kk in range(1,16):
                img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/lensBroken/Fractured_Glass_"+str(kk)+".png").convert('RGBA')
                img = img.resize(img2.size)
                k=0
                pixels = img2.load() 
                for i in range(img2.size[0]): # for every pixel:
                    for j in range(img2.size[1]):
                        if(pixels[i,j][0]==0 and pixels[i,j][3] > 100):
                            pixels[i,j] = (pixels[i,j][0],pixels[i,j][0],pixels[i,j][0],0)
                img.paste(img2,(0,0), img2)
                img=img.resize((224,224))
                img3 = img.convert('RGB')
                img3.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Brokenlens/Brk"+str(kk)+"/5/", filename))
