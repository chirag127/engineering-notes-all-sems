AlexNet is a convolutional neural network (CNN) architecture that was designed by Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton. It won the ImageNet Large Scale Visual Recognition Challenge in 2012. 

AlexNet consists of eight layers: five convolutional layers and three fully connected layers. The network is split into two parallel streams, each running on one GPU. The first two convolutional layers are followed by max-pooling and local response normalization layers. The third, fourth and fifth convolutional layers are directly connected to each other. The last convolutional layer is followed by another max-pooling layer and then three fully connected layers. The final layer is a softmax layer that produces the output probabilities for 1000 classes. 

The following diagram illustrates the basic architecture of AlexNet using ASCII characters:

```
Input: 227 x 227 x 3 image
  |
  v
  |-----------------|    |-----------------|
  | Conv1: 96 11x11 | -> | MaxPool1: 3x3   |
  | filters, stride |    | stride 2        |
  | 4, pad 0        |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | LRN1            | -> | LRN1            |
  |                 |    |                 |
  |-----------------|    |-----------------|
  | Conv2: 256 5x5  | -> | MaxPool2: 3x3   |
  | filters, stride |    | stride 2        |
  | 1, pad 2        |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | LRN2            | -> | LRN2            |
  |                 |    |                 |
  |-----------------|    |-----------------|
  | Conv3: 384 3x3  | -> | Conv3: 384 3x3  |
  | filters, stride |    | filters, stride |
  | 1, pad 1        |    | 1, pad 1        |
  |-----------------|    |-----------------|
  | Conv4: 384 3x3  | -> | Conv4: 384 3x3  |
  | filters, stride |    | filters, stride |
  | 1, pad 1        |    | 1, pad 1        |
  |-----------------|    |-----------------|
  | Conv5: 256 3x3  | -> | Conv5: 256 3x3  |
  | filters, stride |    | filters, stride |
  | 1, pad 1        |    | 1, pad 1        |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | MaxPool3: 3x3   | -> | MaxPool3: 3x3   |
  | stride 2        |    | stride 2        |
  |                 |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | FC6: 4096 units | -> | FC6: 4096 units |
  |                 |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | FC7: 4096 units | -> | FC7: 4096 units |
  |                 |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | FC8: 1000 units | -> | FC8: 1000 units |
  |                 |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  | Softmax         | -> | Softmax         |
  |                 |    |                 |
  |-----------------|    |-----------------|
  |                 |    |                 |
  v                 v    v                 v
Output: 1000 class probabilities
```