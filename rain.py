from matplotlib import pyplot as plt
from PIL import Image
import os
import cv2
directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for filename in os.listdir(directory):
 	if filename.endswith(".jpg"):
         f=os.path.join(directory, filename)
         img = Image.open(f)
         img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/rain/rain1.png").convert("RGBA")
         img2=img2.resize(img.size)
         img.paste(img2, (0, 0), img2)
         img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Rain/Rain1/1",filename))


for filename in os.listdir(directory):
 	if filename.endswith(".jpg"):
         f=os.path.join(directory, filename)
         img = Image.open(f)
		# img2 = Image.open("ice/ice2.png").convert(img.mode)
		# img2 = img2.resize(img.size)
		# img3 = Image.blend(img,img2,1)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
         img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/rain/rain2.png").convert("RGBA")
         img2=img2.resize(img.size)

         img.paste(img2, (0, 0), img2)
         img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Rain/Rain2/1",filename))



for filename in os.listdir(directory):
 	if filename.endswith(".jpg"):
         f=os.path.join(directory, filename)
         img = Image.open(f)
		# img2 = Image.open("ice/ice2.png").convert(img.mode)
		# img2 = img2.resize(img.size)
		# img3 = Image.blend(img,img2,1)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
         img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/rain/rain3.png").convert("RGBA")
         img2.resize(img.size)

         img.paste(img2, (0, 0), img2)
         img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Rain/Rain3/1",filename))



for filename in os.listdir(directory):
 	if filename.endswith(".jpg"):
         f=os.path.join(directory, filename)
         img = Image.open(f)
         size=224,224
		# img2 = Image.open("ice/ice2.png").convert(img.mode)
		# img2 = img2.resize(img.size)
		# img3 = Image.blend(img,img2,1)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
         img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/rain/rain4.png")
         img2=img2.resize(size)
         img2=img2.convert("RGBA")
         img2=img2.crop((0, 0, 224,224))
 	#	img2= img2.resize(img.size)
         img.paste(img2, (0, 0), img2)
         img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Rain/Rain4/1",filename))

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = Image.open(f)
		# img2 = Image.open("ice/ice2.png").convert(img.mode)
		# img2 = img2.resize(img.size)
		# img3 = Image.blend(img,img2,1)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
        img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/rain/rain5.png").convert("RGBA")
        img2=img2.resize(img.size)		
        img.paste(img2, (0, 0), img2)
        img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Rain/Rain5/1",filename))




