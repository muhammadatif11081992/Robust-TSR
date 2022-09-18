from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
import os
import cv2

directory='/home/user/Traffic_Sign/Deep_learning/DITS/Test_data/9'

for i in [10,9,8,7,6,5,4, 3, 2, 1, 0]:
# 	if not os.path.exists("C:/Users/dell/Desktop/Test/sharp/sharp"+str(i)+"/image_2"):
# 		os.makedirs("C:/Users/dell/Desktop/Test/sharp/sharp"+str(i))
# 		os.makedirs("C:/Users/dell/Desktop/Test/sharp/sharp"+str(i)+"/image_2")
# 	else:
# 		continue
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            f=os.path.join(directory, filename)
            img = Image.open(f)
            enhancer = ImageEnhance.Sharpness(img)
            factor = i #proviamo -3.5, -2.5, -1.5
            img = enhancer.enhance(factor)
            img.save(os.path.join("/home/user/Traffic_Sign/Faulty Images/Test_data/DITS/Sharp_Images/S"+str(i)+"/9/",filename))
