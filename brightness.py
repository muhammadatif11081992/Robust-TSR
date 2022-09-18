from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
import os
import cv2

'''
Brightness: This class can be used to control the
brightness of an image. An enhancement
factor of 0.0 gives a black image.
A factor of 1.0 gives the original image.
'''
directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'
#0 is black
for i in [0.1, 0.3, 0.6, 1.5, 6, 7.5, 10, 15]:
# 	if not os.path.exists("C:/Users/dell/Desktop/Test/brightness/brigh"+str(i)+"/image_2"):
# 		os.makedirs("C:/Users/dell/Desktop/Test/brightness/brigh"+str(i))
# 		os.makedirs("C:/Users/dell/Desktop/Test/brightness/brigh"+str(i)+"/image_2")
# 	else:
# 		continue
	for filename in os.listdir(directory):
		if filename.endswith(".jpg"):
			f=os.path.join(directory, filename)
			img = Image.open(f)
			#An enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
			enhancer = ImageEnhance.Brightness(img)
			factor = i #proviamo brightness 1.5, 3, 4.5
			img = enhancer.enhance(factor)

			img.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Brightness/Br"+str(i)+"/1/",filename))




#ok


