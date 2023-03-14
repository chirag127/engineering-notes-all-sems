### ResNet

ResNet is a type of artificial neural network that allows the model to skip one or more layers using shortcut connections. This approach makes it possible to train very deep networks without suffering from the vanishing gradient problem. ResNet has been widely used for various computer vision tasks, such as image classification, object detection and facial recognition.

The basic building block of ResNet is the residual block, which consists of two or more convolutional layers followed by a shortcut connection that adds the input of the block to its output. The shortcut connection helps to preserve the information from earlier layers and also reduces the complexity of the network.

The following diagram illustrates the basic architecture of a residual block:

```
  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  |                     |   |                     |
  +---------------------+   +---------------------+
  |                     |   |                     |
  |