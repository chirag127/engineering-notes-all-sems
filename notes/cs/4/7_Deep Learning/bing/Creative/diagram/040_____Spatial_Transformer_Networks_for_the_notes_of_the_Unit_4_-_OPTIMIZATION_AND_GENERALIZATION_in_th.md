### Spatial Transformer Networks

Spatial transformer networks (STNs) are a type of neural network that can learn to perform spatial transformations on the input image in order to enhance the geometric invariance of the model. For example, they can crop a region of interest, scale and correct the orientation of an image.

STNs consist of three main components :

- The localization network is a regular CNN that regresses the transformation parameters. The transformation is never learned explicitly from the dataset, instead the network learns automatically the spatial transformations that enhance the global accuracy.
- The grid generator generates a grid of coordinates in the input image corresponding to each pixel from the output image. The grid is parameterized by the transformation parameters from the localization network.
- The sampler uses the grid and the input image to produce the output image using bilinear interpolation. The sampler is differentiable, so the gradients can be backpropagated through the whole network.

The STN can be inserted into any existing convolutional architecture, giving the neural network the ability to actively spatially transform feature maps, conditional on the feature map itself. This allows the network to handle large variations in the input data, such as pose, scale, rotation, etc.

STNs have been shown to improve the performance of various tasks, such as digit classification, face alignment, fine-grained recognition, etc . They are also computationally and parameter efficient, as they do not require any extra supervision or pre-processing of the data.

The following diagram illustrates the STN module:

```markdown
+----------------+                       +-----------------+
|                |                       |                 |
|  Input Image   |                       | Output Image    |
|                |                       |                 |
+-------+--------+                       +--------+--------+
        |                                       ^
        |                                       |
        |                                       |
        v                                       |
+-------+--------+     +----------------+      |
|                |     |                |      |
|Localization Net|---->|Grid Generator  |      |
|                |     |                |      |
+----------------+     +--------+-------+      |
                               |              |
                               |              |
                               v              |
                         +-----+------+       |
                         |            |       |
                         |  Sampler   |-------+
                         |            |
                         +------------+
```