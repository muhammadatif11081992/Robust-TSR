import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os
from random import seed
from random import randint
# seed random number generator
seed(1)
directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img1 = cv2.imread(f)
		img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

		h, w, _ = img1.shape

		for z in range (0,500):
			h1=randint(1,h-1)
			w1=randint(1,w-1)
			img1[h1,w1] = (0, 0, 0) #black pixel random number

		img1 = Image.fromarray(img1) # esempio conversione
		img1.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Dead Pixcels/DP500/1",filename))

