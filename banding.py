from matplotlib import pyplot as plt
from PIL import Image
import os
import cv2

directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img = Image.open(f)
		img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/banding/banding.png").convert(img.mode)
		img2 = img2.resize(img.size)
		img3 = Image.blend(img,img2,0.1)#valori per immagine banding->0.02, banding1->0.05, ice->0.2

		img3.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding/Banding1/1",filename))

for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img = Image.open(f)
		img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/banding/banding1.jpg").convert(img.mode)
		img2 = img2.resize(img.size)
		img3 = Image.blend(img,img2,0.2)#valori per immagine banding->0.02, banding1->0.05, ice->0.2

		img3.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding/Banding2/1",filename))
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img = Image.open(f)
		img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/banding/banding1.jpg").convert(img.mode)
		img2 = img2.resize(img.size)
		img3 = Image.blend(img,img2,0.3)#valori per immagine banding->0.02, banding1->0.05, ice->0.2

		img3.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding/Banding3/1",filename))

 # immagini da sovrapporre all'Originale





