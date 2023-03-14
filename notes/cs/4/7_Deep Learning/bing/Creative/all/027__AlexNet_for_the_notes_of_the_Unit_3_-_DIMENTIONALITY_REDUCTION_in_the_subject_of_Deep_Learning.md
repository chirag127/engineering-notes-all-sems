### AlexNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- AlexNet is the name of a convolutional neural network (CNN) architecture, designed by Alex Krizhevsky in collaboration with Ilya Sutskever and Geoffrey Hinton, who was Krizhevsky's Ph.D. advisor. 
- AlexNet competed in the ImageNet Large Scale Visual Recognition Challenge on September 30, 2012. The network achieved a top-5 error of 15.3%, more than 10.8 percentage points lower than that of the runner up. 
- The original paper's primary result was that the depth of the model was essential for its high performance, which was computationally expensive, but made feasible due to the utilization of graphics processing units (GPUs) during training. 
- AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers published employing CNNs and GPUs to accelerate deep learning. As of early 2023, the AlexNet paper has been cited over 120,000 times according to Google Scholar. 

#### AlexNet Architecture

- AlexNet contained eight layers; the first five were convolutional layers, some of them followed by max-pooling layers, and the last three were fully connected layers. 
- The network, except the last layer, is split into two copies, each run on one GPU. This was done to overcome the memory limitations of the GPUs at that time. 
- The entire structure can be written as

```
CNN(96, 11, 4) -> RN -> MP(3, 2) -> CNN(256, 5, 1) -> RN -> MP(3, 2) -> CNN(384, 3, 1) -> CNN(384, 3, 1) -> CNN(256, 3, 1) -> MP(3, 2) -> FC(4096) -> FC(4096) -> Linear(1000)
```

where

- CNN = convolutional layer (with ReLU activation)
- RN = local response normalization
- MP = maxpooling layer
- FC = fully connected layer (with ReLU activation)
- Linear = fully connected layer (without activation)

- The input size of the network is 227 x 227 x 3, which means the network takes RGB images of size 227 x 227 as input. 
- The output size of the network is 1000, which means the network predicts the probability of each of the 1000 classes in the ImageNet dataset. 
- The following table shows the detailed specifications of each layer in the network. 

| Layer | Type | Maps | Size | Kernel | Stride | Padding | Groups |
| ----- | ---- | ---- | ---- | ------ | ------ | ------- | ------ |
| 0 | Input | 3 | 227 x 227 | - | - | - | - |
| 1 | Convolution | 96 | 55 x 55 | 11 x 11 | 4 | 0 | 2 |
| 2 | ReLU | 96 | 55 x 55 | - | - | - | - |
| 3 | Response Normalization | 96 | 55 x 55 | - | - | - | - |
| 4 | Maxpooling | 96 | 27 x 27 | 3 x 3 | 2 | 0 | - |
| 5 | Convolution | 256 | 27 x 27 | 5 x 5 | 1 | 2 | 2 |
| 6 | ReLU | 256 | 27 x 27 | - | - | - | - |
| 7 | Response Normalization | 256 | 27 x 27 | - | - | - | - |
| 8 | Maxpooling | 256 | 13 x 13 | 3 x 3 | 2 | 0 | - |
| 9 | Convolution | 384 | 13 x 13 | 3 x 3 | 1 | 1 | 1 |
| 10 | ReLU | 384 | 13 x 13 | - | - | - | - |
| 11 | Convolution | 384 | 13 x 13