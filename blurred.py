import cv2
import os
from matplotlib import pyplot as plt
directory='/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data/1'

for i in range(25,36):
# 	if (i ==0):#no blur correction; does nothing
# 		continue
# 	if not os.path.exists("/home/user/Traffic_Sign/Faulty Images/Test_data/GTSRB/blur/blur"+str(i)+str(i)+"/image_2"):
# 		os.makedirs("/home/user/Traffic_Sign/Faulty Images/Test_data/GTSRB/blur/blur"+str(i)+str(i))
# 		os.makedirs("/home/user/Traffic_Sign/Faulty Images/Test_data/GTSRB/blur/blur"+str(i)+str(i)+"/image_2")
# 	else:
# 		continue
	for filename in os.listdir(directory):
		if filename.endswith(".jpg"):
			f=os.path.join(directory, filename)
			img = cv2.imread(f)
			blur = cv2.blur(img,(i,i))#(1,1),  (2, 2) etc 
			cv2.imwrite(os.path.join("/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Blurred Images/B"+str(i)+"/1/",filename), blur)
#ok


