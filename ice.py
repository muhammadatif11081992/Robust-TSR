


from matplotlib import pyplot as plt
from PIL import Image
import os
import cv2

directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = Image.open(f)
        img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/ice/ice1.png").convert("RGBA")
        img2 = img2.resize(img.size)
        img.paste(img2, (0,0), img2)
        img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Ice/Ice1/1",filename))
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = Image.open(f)
        img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/ice/ice2.png").convert("RGBA")
        img2 = img2.resize(img.size)
        img.paste(img2, (0,0), img2)
        img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Ice/Ice2/1",filename))
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = Image.open(f)
        img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/ice/ice3.png").convert("RGBA")
        img2 = img2.resize(img.size)
        img.paste(img2, (0,0), img2)
        img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Ice/Ice3/1",filename))
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = Image.open(f)
        img2 = Image.open("/home/user/Camera Failures/Traffic_Sign/ImageFailure/Python_Image_Failures/ice/ice4.png").convert("RGBA")
        img2 = img2.resize(img.size)
        img.paste(img2, (0,0), img2)
        img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Ice/Ice4/1",filename))




