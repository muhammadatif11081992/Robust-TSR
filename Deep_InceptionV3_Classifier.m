%inceptionV3 Training
clc
clear all
load '/home/atif/FDMA/GTSRB/Deep_Learning/GTSRB_50';
imds_combine.ReadFcn=@(loc)imresize(imread(loc),[299 299]);
net = inceptionv3;
lgraph = layerGraph(net);
inputSize = net.Layers(1).InputSize;
lgraph = removeLayers(lgraph,{'predictions', 'predictions_softmax', 'ClassificationLayer_predictions'});
  
 numClasses = numel(categories(imds_combine.Labels));
 newLayers = [
               fullyConnectedLayer(numClasses,'Name','fc','weightLearnRateFactor',20,'BiasLearnRateFactor',20)
               softmaxLayer('Name','softmax')
               classificationLayer('Name','classoutput')];
 lgraph = addLayers(lgraph,newLayers);


  lgraph = connectLayers(lgraph,'avg_pool','fc');
  layers = lgraph.Layers;
  connections = lgraph.Connections;  
  layers(1:10) = freezeWeights(layers(1:10));
  lgraph = createLgraphUsingConnections(layers,connections);
  options = trainingOptions('sgdm', ...
     'MiniBatchSize',32, ...
     'MaxEpochs',10, ...
     'InitialLearnRate',5e-4, ...
     'Verbose',false ,...
     'Plots','training-progress');
%Retrain the network using transfer learning
 netTransfer= trainNetwork(imds_combine,layers,options);
%save the trained model
save('/home/user/FDMA/GTSRB/Models/Deep_Models/GTSRB_Alexnet_50', 'netTransfer','-v7.3');
% To test trained model read each failure category images one by one in this way
imdsTest = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding',...
 'IncludeSubfolders',true,'LabelSource','foldernames');
[YPred,scores] = classify(netTransfer,imdsTest);
%calculate Accuracy
Accuracy=mean(YPred==imdsTest.Labels);
  