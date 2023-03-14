### AlexNet for the notes of the Unit 3 - DIMENSIONALITY REDUCTION in the subject of Deep Learning

AlexNet is a deep convolutional neural network that achieved state-of-the-art results on the ImageNet dataset in 2012. It was developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton from the University of Toronto.

#### Architecture of AlexNet
- AlexNet has a deep architecture with 8 layers, including 5 convolutional layers and 3 fully connected layers.
- The first convolutional layer has 96 filters of size 11x11 with a stride of 4 and applies rectified linear unit (ReLU) activation function.
- The second convolutional layer has 256 filters of size 5x5 with a stride of 1 and applies ReLU activation function.
- The third convolutional layer has 384 filters of size 3x3 with a stride of 1 and applies ReLU activation function.
- The fourth convolutional layer has 384 filters of size 3x3 with a stride of 1 and applies ReLU activation function.
- The fifth convolutional layer has 256 filters of size 3x3 with a stride of 1 and applies ReLU activation function.
- The output of the fifth convolutional layer is flattened and fed into three fully connected layers, each with 4096 units and ReLU activation function.
- The final fully connected layer has 1000 units, one for each class in the ImageNet dataset, and applies softmax activation function.

#### Advantages of AlexNet
- AlexNet was the first deep convolutional neural network to achieve state-of-the-art results on the ImageNet dataset, which marked a breakthrough in the field of computer vision.
- The architecture of AlexNet introduced several new concepts, such as the use of ReLU activation function, overlapping pooling, and dropout regularization, which have become standard practices in deep learning.
- AlexNet demonstrated the importance of using GPUs for training deep neural networks, which greatly reduced the training time.

#### Disadvantages of AlexNet
- The architecture of AlexNet is very deep and complex, which makes it computationally expensive to train and deploy.
- The size of the model is also large, which requires a lot of memory to store the parameters of the model.
- The architecture of AlexNet is prone to overfitting, which requires careful regularization techniques to prevent.

#### Mnemonics and Learning Tricks for AlexNet
- One mnemonic for remembering the architecture of AlexNet is to think of it as a pyramid, with the first convolutional layer being the widest and the subsequent layers becoming narrower as they go deeper.
- Another mnemonic is to remember the number of filters in each convolutional layer: 96-256-384-384-256, which follows a decreasing pattern.
- A learning trick for training AlexNet is to use data augmentation techniques, such as random cropping, flipping, and color shifting, which can increase the size of the training set and improve the generalization performance of the model.