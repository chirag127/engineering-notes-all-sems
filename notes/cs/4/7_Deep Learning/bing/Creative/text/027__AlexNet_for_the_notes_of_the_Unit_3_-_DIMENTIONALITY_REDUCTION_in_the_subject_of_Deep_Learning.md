### AlexNet

AlexNet is the name of a convolutional neural network (CNN) architecture, designed by Alex Krizhevsky in collaboration with Ilya Sutskever and Geoffrey Hinton, who was Krizhevsky's Ph.D. advisor.  AlexNet competed in the ImageNet Large Scale Visual Recognition Challenge on September 30, 2012.  The network achieved a top-5 error of 15.3%, more than 10.8 percentage points lower than that of the runner up. The original paper's primary result was that the depth of the model was essential for its high performance, which was computationally expensive, but made feasible due to the utilization of graphics processing units (GPUs) during training. 

AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers published employing CNNs and GPUs to accelerate deep learning. As of early 2023, the AlexNet paper has been cited over 120,000 times according to Google Scholar. 

Some of the main features of AlexNet are:

- It contains eight layers; the first five are convolutional layers, some of them followed by max-pooling layers, and the last three are fully connected layers. The network, except the last layer, is split into two copies, each run on one GPU. 
- It uses rectified linear units (ReLU) as the activation function for the hidden layers, which are faster to train than the traditional sigmoid or tanh functions. 
- It applies local response normalization (LRN) after some convolutional layers, which helps with generalization and reduces overfitting. 
- It uses dropout, a regularization technique that randomly sets some neurons to zero during training, to reduce overfitting and improve generalization. 
- It uses data augmentation, such as cropping, flipping, and color alterations, to increase the size and diversity of the training data. 
- It uses a large dataset, ImageNet, which contains 22,000 classes across 15 million high-resolution images, to train the network.  

The following table shows the detailed architecture of AlexNet, with the number of filters, kernel size, stride, padding, and output size for each layer. 

| Layer | Type | Filters | Kernel | Stride | Padding | Output |
| ----- | ---- | ------- | ------ | ------ | ------- | ------ |
| 1 | Convolutional | 96 | 11x11 | 4 | 0 | 55x55x96 |
| 2 | Max Pooling | - | 3x3 | 2 | 0 | 27x27x96 |
| 3 | LRN | - | - | - | - | 27x27x96 |
| 4 | Convolutional | 256 | 5x5 | 1 | 2 | 27x27x256 |
| 5 | Max Pooling | - | 3x3 | 2 | 0 | 13x13x256 |
| 6 | LRN | - | - | - | - | 13x13x256 |
| 7 | Convolutional | 384 | 3x3 | 1 | 1 | 13x13x384 |
| 8 | Convolutional | 384 | 3x3 | 1 | 1 | 13x13x384 |
| 9 | Convolutional | 256 | 3x3 | 1 | 1 | 13x13x256 |
| 10 | Max Pooling | - | 3x3 | 2 | 0 | 6x6x256 |
| 11 | Fully Connected | 4096 | - | - | - | 4096 |
| 12 | Dropout | - | - | - | - | 4096 |
| 13 | Fully Connected | 4096 | - | - | - | 4096 |
| 14 | Dropout | - | - | - | - | 4096 |
| 15 | Fully Connected | 1000 | - | - | - | 1000 |
| 16 | Softmax | - | - | - | - | 1000 |

The following diagram illustrates the AlexNet architecture, with the two parallel streams for each GPU. [^2