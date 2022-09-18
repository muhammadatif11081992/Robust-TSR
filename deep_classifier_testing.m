clc
clear all
load '/home/user/FDANew/BTS/Deep_Models/BTS_Alexnet_50.mat';%%%%change classifier name and dataset
imds = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Test_data/BelgiumTSC/Clean_data', ...%%%%change dataset name
    'IncludeSubfolders',true, ...
    'LabelSource','foldernames');


imds.ReadFcn=@(loc)imresize(imread(loc), [227 227]);
[Pred_labels,scores] = classify(net,imds);
accuracy=mean(imds.Labels==Pred_labels)
A=imds.Labels==Pred_labels;
idx=A==0;
Number_of_misclassifications=sum(idx(:))