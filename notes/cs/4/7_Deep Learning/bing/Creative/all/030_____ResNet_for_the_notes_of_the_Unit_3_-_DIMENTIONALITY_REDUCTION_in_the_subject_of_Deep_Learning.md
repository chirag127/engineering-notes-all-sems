# ResNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- ResNet stands for Residual Network, a type of deep neural network that can learn complex functions by using residual connections or skip connections.
- Residual connections are shortcuts that allow the input of a layer to be added to the output of a later layer, bypassing some intermediate layers.
- Residual connections help to solve the problem of vanishing gradients and degradation of accuracy when training very deep networks, by creating direct paths for the gradient to flow back.
- ResNet was proposed by He et al. in 2015 and won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) with a 152-layer network that achieved 3.57% top-5 error rate.
- ResNet can be seen as a generalization of Highway Networks, which use gated units to control the flow of information through skip connections.
- ResNet can be divided into several building blocks, each consisting of a few convolutional layers and a residual connection. The basic building block for ResNet-18 and ResNet-34 is shown below:

![Basic ResNet block](https://miro.medium.com/max/700/1*ByrVJspW-TefwlH7OLxNkg.png)

- The basic building block for ResNet-50, ResNet-101 and ResNet-152 is shown below:

![Bottleneck ResNet block](https://miro.medium.com/max/700/1*FfXnAZWfjIqBd2j2hJ71yQ.png)

- The bottleneck block uses a 1x1 convolution to reduce the number of channels before applying a 3x3 convolution, and then another 1x1 convolution to restore the number of channels. This reduces the computational cost and the number of parameters.
- ResNet can be applied to various tasks such as image classification, object detection, semantic segmentation, and face recognition. ResNet can also be combined with other techniques such as attention, dilated convolutions, and adversarial training to improve the performance.
- ResNet is one of the most influential and widely used architectures in deep learning, and has inspired many variants and extensions, such as DenseNet, ResNeXt, and Wide ResNet.