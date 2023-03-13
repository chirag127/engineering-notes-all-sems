### ResNet

ResNet is a type of artificial neural network that uses residual blocks and skip connections to overcome the problem of vanishing or exploding gradients in very deep networks. ResNet can have hundreds or thousands of layers without affecting the performance. ResNet is widely used for various computer vision tasks, such as image classification, object detection, and semantic segmentation.

The following diagram illustrates the basic architecture of a ResNet:

```
Input
  |
  v
Conv2D -> BatchNorm -> ReLU -> MaxPool
  |
  v
Residual Block 1 -> Residual Block 2 -> ... -> Residual Block N
  |
  v
Global Average Pool -> Fully Connected -> Softmax
  |
  v
Output
```

A residual block is a sub-network that consists of one or more convolutional layers followed by batch normalization and ReLU activation. A residual block also has a skip connection that adds the input of the block to the output of the block, creating a shortcut path for the information flow. The skip connection helps to preserve the identity of the input and avoid the degradation of the network performance as the depth increases.

The following diagram illustrates the structure of a residual block:

```
Input
  |----------------------+
  |                      |
  v                      |
Conv2D -> BatchNorm -> ReLU
  |                      |
  v                      |
Conv2D -> BatchNorm -> ReLU
  |                      |
  v                      v
  +--------------------> +
  |                      |
  v                      v
Output
```

There are different variants of ResNet, such as ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152. The number indicates the number of weighted layers in the network. ResNet-50, ResNet-101, and ResNet-152 use bottleneck blocks, which are modified residual blocks that reduce the number of channels in the first and third convolutional layers to save computation and memory. The following diagram illustrates the structure of a bottleneck block:

```
Input
  |----------------------+
  |                      |
  v                      |
Conv2D -> BatchNorm -> ReLU
  |                      |
  v                      |
Conv2D -> BatchNorm -> ReLU
  |                      |
  v                      |
Conv2D -> BatchNorm -> ReLU
  |                      v
  +--------------------> +
  |                      |
  v                      v
Output
```

ResNet is a powerful and versatile architecture that can achieve state-of-the-art results on many computer vision tasks. ResNet is also easy to implement and modify, as it only requires adding residual blocks and skip connections to a standard convolutional network. ResNet is one of the most influential and popular architectures in deep learning.