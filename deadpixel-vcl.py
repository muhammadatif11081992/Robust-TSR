#set a vertical black line in the middle of the figure
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from random import seed
from random import randint
import os
# seed random number generator
seed(1)

directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'


for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img1 = cv2.imread(f)
		img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
		h, w, _ = img1.shape

		w1=int(w/2)
		img1[:,w1] = (0,0,0)

		img1 = Image.fromarray(img1) # esempio conversione
		img1.save(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Dead Pixcels/DPvcl/1",filename))

