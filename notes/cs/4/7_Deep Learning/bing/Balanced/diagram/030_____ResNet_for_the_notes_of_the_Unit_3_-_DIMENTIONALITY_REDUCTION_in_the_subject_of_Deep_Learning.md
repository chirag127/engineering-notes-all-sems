### ResNet

- ResNet stands for Residual Network, a deep neural network architecture that can achieve state-of-the-art performance on image recognition tasks.
- ResNet introduces the concept of residual learning, which is based on the idea that instead of learning a direct mapping from input to output, the network learns a residual function that adds some corrections to the input.
- ResNet uses skip connections or shortcut connections to connect the input of a layer to the output of a later layer, bypassing some intermediate layers. This allows the network to preserve the information from the input and avoid the problem of vanishing gradients.
- ResNet consists of several blocks of layers, each block having a skip connection that adds the input to the output of the block. The blocks can be either identity blocks or convolutional blocks, depending on whether the input and output have the same or different dimensions.
- ResNet can be trained using standard techniques such as stochastic gradient descent, batch normalization, and dropout. ResNet can also be modified and extended for different applications, such as object detection, semantic segmentation, and video recognition.