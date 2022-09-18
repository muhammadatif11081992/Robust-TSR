import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import os

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        f=os.path.join(directory, filename)
        img = mpimg.imread(f)
        gray = rgb2gray(img)
# in alcuni casi .convert('LA') potrebbe non funzionare e l'altra conversione
# che ho utilizzato è .convert('L')

        plt.imsave(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/GrayImages/1/" ,filename),gray)


#ok

