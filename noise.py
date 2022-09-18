from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
import os
import cv2
import numpy as np

directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'


for i in [0.4, 0.6, 0.8, 1, 1.5, 2, 3, 4, 5]:
# 	if not os.path.exists("C:/Users/dell/Desktop/Test/noise/noise"+str(i)+"/image_2"):
# 		os.makedirs("C:/Users/dell/Desktop/Test/noise/noise"+str(i))
# 		os.makedirs("C:/Users/dell/Desktop/Test/noise/noise"+str(i)+"/image_2")
# 	else:
# 		continue
	for filename in os.listdir(directory):
		if filename.endswith(".jpg"):
			f=os.path.join(directory, filename)
			img = Image.open(f)
			img = cv2.imread(f)
			#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			#Speckle Noise
			gauss = np.random.normal(0,i,img.size)
			gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
			noise = img + img * gauss
			cv2.imwrite(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Noise/Noise"+str(i)+"/1/",filename), noise)



