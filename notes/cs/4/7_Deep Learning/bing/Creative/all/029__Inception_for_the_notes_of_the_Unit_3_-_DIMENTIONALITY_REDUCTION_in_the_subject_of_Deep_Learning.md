### Inception for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Inception is a deep learning model based on convolutional neural networks (CNNs) that was introduced by Google researchers in 2014.
- Inception consists of repeating components called Inception modules, which allow for more efficient computation and deeper networks through a dimensionality reduction with stacked 1x1 convolutions.
- The main idea behind Inception is to use multiple kernel filter sizes within the CNN, and rather than stacking them sequentially, ordering them to operate on the same level.
- This way, the network can capture features at different scales and levels of abstraction, and also reduce the number of parameters and computations.
- The original Inception model, also known as GoogLeNet or Inception v1, won the ImageNet Large Scale Visual Recognition Challenge 2014 (ILSVRC14) with a top-5 error rate of 6.67%.
- The Inception module in Inception v1 works by performing a convolution on an input with not one, but three different sizes of filters (1x1, 3x3, 5x5). Also, max pooling is performed. Then, the resulting outputs are concatenated and sent to the next layer.
- To make the process even less computationally expensive, the Inception module adds an extra 1x1 convolution before the 3x3 and 5x5 layers. By doing so, the number of input channels is limited and 1x1 convolutions are far cheaper than 5x5 convolutions.
- The 1x1 convolution is added after the max-pooling layer, rather than before, to preserve the spatial information.
- The Inception module can be illustrated as follows:

```
Input
  |
  |-----(1x1 Conv)----|
  |                   |
  |-----(1x1 Conv)--(3x3 Conv)----|
  |                   |            |
  |-----(1x1 Conv)--(5x5 Conv)----|----Concat----Output
  |                   |            |
  |-----(3x3 MaxPool)-(1x1 Conv)----|
  |
```

- The number of multiplier operations within individual Inception module components can be calculated as follows:

  - For a 1x1 convolution, the number of operations is equal to the number of input channels times the number of output channels times the height times the width of the output feature map.
  - For a 3x3 convolution, the number of operations is equal to the number of input channels times the number of output channels times the height times the width of the output feature map times 9 (the size of the filter).
  - For a 5x5 convolution, the number of operations is equal to the number of input channels times the number of output channels times the height times the width of the output feature map times 25 (the size of the filter).
  - For a 3x3 max pooling, the number of operations is equal to the number of input channels times the height times the width of the output feature map times 9 (the size of the filter).
  - For a concatenation, the number of operations is equal to zero, as it only involves rearranging the data.

- For example, if the input has 256 channels and the output has 512 channels, and the height and width of the output feature map are 28x28, then the number of operations for each component is:

  - For the 1x1 convolution branch, the number of operations is 256 x 64 x 28 x 28 = 12,582,912
  - For the 1x1 convolution followed by 3x3 convolution branch, the number of operations is (256 x 64 x 28 x 28) + (64 x 128 x 28 x 28 x 9) = 38,146,048
  - For the 1x1 convolution followed by 5x5 convolution branch, the number of operations is (256 x 16 x 28 x 28) + (16 x 32 x 28 x 28 x 25) = 18,874,368
  - For the 3x3 max pooling followed by 1x1 convolution branch, the number of operations is (256 x 28 x 28 x 9) +