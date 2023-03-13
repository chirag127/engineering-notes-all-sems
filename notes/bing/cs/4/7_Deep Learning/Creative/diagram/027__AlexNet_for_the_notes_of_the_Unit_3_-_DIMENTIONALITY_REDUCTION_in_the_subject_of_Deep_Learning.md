AlexNet is a convolutional neural network (CNN) architecture that was designed by Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton. It won the ImageNet Large Scale Visual Recognition Challenge in 2012. It consists of eight layers: five convolutional layers and three fully connected layers. The following diagram illustrates the basic architecture of AlexNet:

```
Input: 227 x 227 x 3 image
  |
  v
Conv1: 96 filters of size 11 x 11 x 3, stride 4, padding 0
  |
  v
MaxPool1: 3 x 3 window, stride 2
  |
  v
Norm1: Local Response Normalization
  |
  v
Conv2: 256 filters of size 5 x 5 x 48, stride 1, padding 2
  |
  v
MaxPool2: 3 x 3 window, stride 2
  |
  v
Norm2: Local Response Normalization
  |
  v
Conv3: 384 filters of size 3 x 3 x 256, stride 1, padding 1
  |
  v
Conv4: 384 filters of size 3 x 3 x 192, stride 1, padding 1
  |
  v
Conv5: 256 filters of size 3 x 3 x 192, stride 1, padding 1
  |
  v
MaxPool3: 3 x 3 window, stride 2
  |
  v
FC1: 4096 neurons
  |
  v
FC2: 4096 neurons
  |
  v
FC3: 1000 neurons (output layer)
  |
  v
Softmax: 1000 classes
```