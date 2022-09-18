clc
clear all
%Selection of Visual Camera Failure Samples from each dataset
percentage=0.5;

%Reading of each category faulty train data and splitting it
imds_Chromatic = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Chromatic',...
 'IncludeSubfolders',true,'LabelSource','foldernames');
 [imd_Train_Chromatic, temp_Chromatic] = splitEachLabel (imds, percentage, 'randomized');
 %Reading of each category faulty train data and splitting it
imds_Gray_Images = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Gray_Images',...
 'IncludeSubfolders',true,'LabelSource','foldernames');
 [imd_Train_Gray_Images, temp_Gray_Images] = splitEachLabel (imds, percentage, 'randomized');
%This way Combining multiple camera failure train data of each category
imds_Chromatic_Grayimages = imageDatastore(cat(1,imd_Train_Chromatic.Files,imd_Train_Gray_Images.Files));
imds_Chromatic_Grayimages.Labels = cat(1,imd_Train_Chromatic.Labels,imd_Train_Gray_Images.Labels);
save('/home/user/FDMA/GTSRB/Deep_Learning/GTSRB_50', 'imds_Chromatic_Grayimages','-v7.3');
%Reading of clean training data
 imd_Train_clean = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Deep_learning/GTSRB/Train_data',...
'IncludeSubfolders',true,'LabelSource','foldernames');
 %combine clean data with failures samples from each category and save the
 %full training set that will be used to train a classifier
save('/home/user/FDMA/GTSRB/Deep_Learning/GTSRB_30', 'imds_combine','-v7.3');