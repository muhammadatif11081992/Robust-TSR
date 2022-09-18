%Training of MobilenetV2
clc
clear all
load '/home/user/FDMA/GTSRB/Deep_Learning/GTSRB_50';
imds_combine.ReadFcn=@(loc)imresize(imread(loc),[224 224]);
net = mobilenetv2;
inputSize = net.Layers (1) .InputSize;
lgraph = layerGraph(net);
[learnableLayer,classLayer] = findLayersToReplace(lgraph);
numClasses = numel(categories(imds_combine.Labels));

if isa(learnableLayer,'nnet.cnn.layer.FullyConnectedLayer')
    newLearnableLayer = fullyConnectedLayer(numClasses, ...
        'Name','new_fc', ...
        'WeightLearnRateFactor',10, ...
        'BiasLearnRateFactor',10);
   
elseif isa(learnableLayer,'nnet.cnn.layer.Convolution2DLayer')
    newLearnableLayer = convolution2dLayer(1,numClasses, ...
        'Name','new_conv', ...
        'WeightLearnRateFactor',10, ...
        'BiasLearnRateFactor',10);
end

lgraph = replaceLayer(lgraph,learnableLayer.Name,newLearnableLayer);

newClassLayer = classificationLayer('Name','new_classoutput');
lgraph = replaceLayer(lgraph,classLayer.Name,newClassLayer);
layers = lgraph.Layers;
connections = lgraph.Connections;

layers(1:10) = freezeWeights(layers(1:10));
lgraph = createLgraphUsingConnections(layers,connections);
miniBatchSize = 32;

options = trainingOptions('sgdm', ...
    'MiniBatchSize',miniBatchSize, ...
    'MaxEpochs',10, ...
    'InitialLearnRate',1e-3, ...
    'Shuffle','every-epoch', ...
    'Verbose',false, ...
    'Plots','training-progress');
net = trainNetwork(imds_combine,lgraph,options);
save('/home/user/FDMA/GTSRB/Models/Deep_Models/GTSRB_Mobile_50', 'net','-v7.3');

% To test trained model read each failure category images one by one in this way
imdsTest = imageDatastore('/home/user/Camera Failures/Traffic_Sign/Faulty Images/Train_data/GTSRB/Banding',...
 'IncludeSubfolders',true,'LabelSource','foldernames');
[YPred,scores] = classify(netTransfer,imdsTest);
%calculate Accuracy
Accuracy=mean(YPred==imdsTest.Labels);

