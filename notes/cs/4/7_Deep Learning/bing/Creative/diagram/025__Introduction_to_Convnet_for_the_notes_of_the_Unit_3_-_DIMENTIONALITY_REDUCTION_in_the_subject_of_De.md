A Convolutional Neural Network, also known as CNN or ConvNet, is a class of neural networks that specializes in processing data that has a grid-like topology, such as an image. A digital image is a binary representation of visual data. A convolutional neural network is used to detect and classify objects in an image.

A ConvNet architecture is composed of three main types of layers: convolutional layers, pooling layers, and fully connected layers.

- Convolutional layers apply a set of filters to the input data, producing a set of feature maps that capture the local patterns in the data.
- Pooling layers reduce the spatial dimensions of the feature maps, making the network more efficient and invariant to small translations.
- Fully connected layers connect every neuron in one layer to every neuron in the next layer, performing the final classification or regression task.

The following diagram illustrates the basic architecture of a ConvNet using ASCII art:

```
Input image: 32 x 32 x 3 (RGB)
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+

Convolutional layer 1: 6 filters of size 5 x 5 x 3, stride 1, no padding
+------------------------+     +------------------------+
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |                        |
|                        |     |  +-----------------+   |
|                        |     |  |                 |   |
|                        |     |  |                 |   |
+------------------------+     |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  |                 |   |
                               |  +-----------------+   |
                               +------------------------+

Pooling layer 1: max pooling of size 2 x 2, stride 2
+------------------------+     +-----------------+
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     |                 |
|                        |     +-----------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+

Convolutional layer 2: 16 filters of size 5 x 5 x 6, stride 1, no padding
+-----------------+     +-----------------+
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     +-----------------+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+-----------------+

Pooling layer 2: max pooling of size 2 x 2, stride 2
+-----------------+     +----------+
|                 |     |          |
|                 |     |          |
|                 |     |          |
|                 |     |          |
|                 |     |          |
|                 |     |          |
|                 |     |          |
|                 |     +----------+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+-----------------+

Flattening layer: reshape the feature maps into a vector of size 400
+----------+     +---+
|          |     |   |
|          |     |   |
|          |     |   |
|          |     |   |
|          |     |   |
|          |     |   |
|          |     |   |
+----------