
%Training of Alexnet
clc
clear all
%Load Already stored Training samples
load '/home/atif/FDMA/GTSRB/Deep_Learning/GTSRB_50';
%resize the images according to the input of model
 imds_combine.ReadFcn=@(loc)imresize(imread(loc),[227 227]);
% load pretrained Alexnet Model
 net = alexnet;
 inputSize = net.Layers(1).InputSize
 layersTransfer = net.Layers(1:end-3);
 numClasses = numel(categories(imds_combine.Labels))
 layers = [
     layersTransfer
     fullyConnectedLayer(numClasses,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20) %WeightLearnRateFactor and BiasLearnRateFactor can be varied
     softmaxLayer
     classificationLayer];
 options = trainingOptions('sgdm', ...%can be changed 
     'MiniBatchSize',32, ...%can be tuned
     'MaxEpochs',10, ...%can be tuned
     'InitialLearnRate',5e-6, ...%can be tuned
     'Shuffle','every-epoch', ...
     'Verbose',false, ...
     'Plots','training-progress');
%Retrain the network using transfer learning
 netTransfer= trainNetwork(imds_combine,layers,options);
%save the trained model
save('/home/user/FDMA/GTSRB/Models/Deep_Models/GTSRB_Alexnet_50', 'netTransfer','-v7.3');
% to test trained model read each failure category images one by one in this way
imdsTest = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding',...
 'IncludeSubfolders',true,'LabelSource','foldernames');
[YPred,scores] = classify(netTransfer,imdsTest);
%calculate Accuracy
Accuracy=mean(YPred==imdsTest.Labels);




