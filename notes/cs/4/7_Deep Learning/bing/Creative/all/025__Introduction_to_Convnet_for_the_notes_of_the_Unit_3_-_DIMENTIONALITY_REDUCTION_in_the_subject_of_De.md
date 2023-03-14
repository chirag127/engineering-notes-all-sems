### Introduction to ConvNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- A Convolutional Neural Network, also known as CNN or ConvNet, is a class of deep neural networks that specializes in processing data that has a grid-like topology, such as an image.
- A digital image is a binary representation of visual data. It consists of pixels arranged in rows and columns. Each pixel has a numerical value that indicates its color intensity.
- A ConvNet can learn to extract features from the input image by applying a series of mathematical operations, called convolutions, to the pixel values.
- A convolution is essentially sliding a filter, also known as a kernel, over the input. The filter is a matrix of weights that are learned during training. The filter is multiplied element-wise with the input, and the results are summed up to produce a single output value. This process is repeated for every possible position of the filter on the input, resulting in a feature map.
- A feature map is the output of one filter applied to the previous layer. It represents the presence or absence of a certain feature in the input. For example, a filter can detect edges, corners, curves, etc.
- A ConvNet can have multiple filters in each convolutional layer, resulting in multiple feature maps. The number of filters is a hyperparameter that can be tuned to optimize the performance of the network.
- A ConvNet can also have multiple convolutional layers, each extracting more abstract and complex features from the previous layer. The deeper the network, the more expressive and powerful it becomes.
- A ConvNet can also include other types of layers, such as pooling layers, fully connected layers, and activation functions.
- A pooling layer is used to reduce the spatial dimensions of the feature maps, while preserving the most important information. Pooling can be done by applying a function, such as max, average, or min, to a region of the feature map, and outputting the result. Pooling can help to reduce the number of parameters, memory usage, and computation time of the network, as well as to prevent overfitting.
- A fully connected layer is a layer where every neuron is connected to every neuron in the previous layer. It is used to perform classification or regression on the extracted features. A fully connected layer can also be seen as a convolutional layer with a filter that has the same size as the input.
- An activation function is a function that introduces non-linearity to the network. It is applied to the output of a layer, and determines whether a neuron should fire or not. Some common activation functions are sigmoid, tanh, ReLU, and softmax.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the components of a ConvNet is: **C**onvolution, **P**ooling, **F**ully **C**onnected, **A**ctivation (CPFC-A).
- A possible learning trick to understand how convolutions work is to imagine sliding a magnifying glass over an image, and looking at the pixel values through the glass. The glass is the filter, and the output is the feature map.
- A possible learning trick to understand how pooling works is to imagine dividing the image into smaller regions, and picking the most representative pixel value in each region. The function that picks the pixel value is the pooling function, and the output is the pooled feature map.