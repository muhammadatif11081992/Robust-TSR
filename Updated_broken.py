
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
import os
import cv2

directory='/home/user/Traffic_Sign/Deep_learning/GTSRB/Test_data/1'
for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            f=os.path.join(directory, filename)
            imgg = Image.open(f).convert('RGBA')
            for kk in range(1,2):
                img2 = Image.open("/home/user/Traffic_Sign/ImageFailure/Python_Image_Failures/lensBroken/Fractured_Glass_"+str(kk)+".png").convert('RGBA')
                img = imgg.resize(img2.size)
                
                
                img3 = img2.convert("RGBA")
                datas = img3.getdata()
                newData = []
                for item in datas:
                    if(item[0]==0 and item[3]>100):
                        newData.append((item[0],item[1],item[2],0))
                    else:
                        newData.append(item)
                        
                img3.putdata(newData)
                img.paste(img3,(0,0), img3)
                img=img.resize((224,224))
                img4 = img.convert('RGB')
                img4.save(os.path.join("/home/user/Traffic_Sign/Brk"+str(kk)+"/1/", filename))
                
                
                
                
                