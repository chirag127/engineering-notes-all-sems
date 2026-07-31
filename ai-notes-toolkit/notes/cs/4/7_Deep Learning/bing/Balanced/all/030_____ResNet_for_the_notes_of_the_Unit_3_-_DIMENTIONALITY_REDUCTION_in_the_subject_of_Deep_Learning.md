# ResNet

- ResNet stands for Residual Network, a type of deep neural network that can learn from very deep architectures without suffering from the vanishing or exploding gradient problem.
- ResNet introduces the concept of skip connections or shortcut connections, which are connections that bypass one or more layers in the network and add the output of an earlier layer to a later layer.
- Skip connections help to preserve the information and gradient flow in the network, and also reduce the effective depth of the network, making it easier to optimize.
- ResNet can be seen as a collection of residual blocks, where each block consists of two or more convolutional layers and a skip connection that adds the input of the block to the output of the block.
- ResNet can be trained using standard techniques such as stochastic gradient descent, batch normalization, and dropout.
- ResNet has achieved state-of-the-art results on various computer vision tasks, such as image classification, object detection, and semantic segmentation.