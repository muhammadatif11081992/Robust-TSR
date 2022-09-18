from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
import os
import cv2


directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/3'
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img = Image.open(f)
		for i in range(1, 37):
			img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/lensDirt/LensDirt-"+str(i)+".png").convert(img.mode)
			img2 = img2.resize(img.size)
			img3 = Image.blend(img,img2,0.5)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
			enhancer = ImageEnhance.Brightness(img3)
			factor = 1.6 #aggiungo luminosità
			img3 = enhancer.enhance(factor)

# 			if not os.path.exists("C:/Users/dell/Desktop/Test/dirt/dirt"+str(i)):
# 				os.makedirs("C:/Users/dell/Desktop/Test/dirt/dirt"+str(i))
			img3.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Dirt/Dirt"+str(i)+"/3/",filename))
