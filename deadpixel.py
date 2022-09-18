import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from random import seed
from random import randint
import os
# seed random number generator
seed(1)
directory='/home/user/Traffic_Sign/Deep_learning/DITS/Test_data/9'


for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		f=os.path.join(directory, filename)
		img1 = cv2.imread(f)
		img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
		h, w, _ = img1.shape

		h1=randint(1,h-1)
		w1=randint(1,w-1)
		img1[h1,w1] = (0,0,0)
		img1 = Image.fromarray(img1) # esempio conversione
		img1.save(os.path.join("/home/user/Traffic_Sign/Faulty Images/Test_data/DITS/Dead Pixcels/DP1/9",filename))

#ok
