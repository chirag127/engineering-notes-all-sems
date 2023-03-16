### ResNet

- ResNet stands for Residual Network, a type of deep neural network that uses residual connections or skip connections to overcome the problem of vanishing gradients and degradation of accuracy in very deep networks.
- Residual connections are shortcuts that allow the input of a layer to be added to the output of a later layer, bypassing some intermediate layers. This helps to preserve the information and gradient flow across the network and avoid the loss of signal or the increase of noise.
- ResNet was proposed by He et al. in 2015 and won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) with a 152-layer network that achieved a top-5 error rate of 3.57%, surpassing human performance.
- ResNet is based on the idea that instead of learning an identity mapping from input to output, it is easier to learn a residual mapping that adds some correction to the input. Mathematically, this can be expressed as:

  $$y = F(x) + x$$

  where $y$ is the output, $x$ is the input, and $F(x)$ is the residual function learned by the intermediate layers.
- ResNet consists of several building blocks, each of which has a residual connection. There are two types of blocks: basic blocks and bottleneck blocks. Basic blocks are used for networks with less than 50 layers, and bottleneck blocks are used for deeper networks with more than 50 layers.
- Basic blocks have two convolutional layers with batch normalization and ReLU activation, followed by an element-wise addition with the input. The dimensions of the input and output are the same, so no projection is needed. The structure of a basic block is shown below:

  ![Basic block](https://miro.medium.com/max/700/1*FfGm2sQj3wXfZy2B8jW7Rw.png)

- Bottleneck blocks have three convolutional layers with batch normalization and ReLU activation, followed by an element-wise addition with the input. The first and third layers have a 1x1 kernel size and reduce and restore the number of channels, respectively. The second layer has a 3x3 kernel size and performs the main convolution. The dimensions of the input and output may differ, so a projection layer with a 1x1 convolution may be needed to match them. The structure of a bottleneck block is shown below:

  ![Bottleneck block](https://miro.medium.com/max/700/1*6hF97Upuqg_LdsqWY6n_wg.png)

- ResNet can be easily extended to deeper networks by stacking more blocks. The number of channels is doubled every time the spatial resolution is halved by a stride of 2. The network starts with a 7x7 convolution with a stride of 2, followed by a 3x3 max pooling with a stride of 2. The network ends with a global average pooling and a fully connected layer with softmax activation. The architecture of ResNet-50, a 50-layer network, is shown below:

  ![ResNet-50](https://miro.medium.com/max/700/1*6hF97Upuqg_LdsqWY6n_wg.png)

- ResNet is a powerful and versatile network that can be applied to various computer vision tasks, such as image classification, object detection, semantic segmentation, and face recognition. ResNet has also inspired many variants and extensions, such as ResNeXt, DenseNet, and SENet, that further improve the performance and efficiency of deep neural networks.