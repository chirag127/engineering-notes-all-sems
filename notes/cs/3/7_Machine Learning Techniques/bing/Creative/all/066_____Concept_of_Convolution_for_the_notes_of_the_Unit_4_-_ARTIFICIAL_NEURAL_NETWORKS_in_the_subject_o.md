# Concept of Convolution for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- A convolutional neural network (CNN) is a type of artificial neural network that uses a mathematical operation called convolution in place of general matrix multiplication in at least one of its layers.
- Convolution is a process of combining two functions to produce a third function that expresses how one function is modified by the other.
- In a CNN, the input is usually an image or a sequence of images, and the convolution operation is applied to a set of filters or kernels that slide over the input and produce feature maps  .
- The feature maps capture the spatial patterns and dependencies in the input, such as edges, shapes, colors, textures, etc  .
- The convolution operation can be defined as follows:

  - Let $f(x,y)$ be the input image and $g(x,y)$ be the filter or kernel.
  - The convolution of $f$ and $g$ is denoted by $f*g$ and is given by:

    $$f*g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x-s,y-t)g(s,t)$$

  - where $a$ and $b$ are the half-width and half-height of the filter, respectively.
  - The convolution operation can be visualized as follows:

    ![Convolution operation](https://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif)

- The convolution operation has some properties that make it suitable for neural networks:

  - It is linear, which means that it can be expressed as a matrix multiplication and can be easily differentiated and optimized.
  - It is translation invariant, which means that the output does not change if the input is shifted by some amount. This allows the network to learn features that are independent of their location in the input.
  - It is sparse, which means that each output element depends only on a small region of the input. This reduces the number of parameters and computations required by the network.
  - It is parameter sharing, which means that the same filter is applied to different regions of the input. This allows the network to learn features that are generalizable across the input.

- A CNN typically consists of three types of layers: convolutional layer, pooling layer, and fully-connected layer  .

  - A convolutional layer applies one or more filters to the input and produces one or more feature maps. The filters are learned by the network during training and can have different sizes, shapes, and strides  .
  - A pooling layer reduces the size and dimensionality of the feature maps by applying a downsampling operation, such as max pooling, average pooling, or L2-norm pooling. The pooling operation helps to reduce the computational cost and overfitting of the network  .
  - A fully-connected layer connects every neuron in the previous layer to every neuron in the next layer and performs a nonlinear activation function, such as sigmoid, tanh, or ReLU. The fully-connected layer is usually the final layer of the network and produces the output or prediction  .

- A CNN can be represented by the following diagram:

  ![CNN diagram](https://upload.wikimedia.org/wikipedia/commons/6/63/Typical_cnn.png)

- A CNN can be trained using the same methods as other neural networks, such as gradient descent, backpropagation, and stochastic gradient descent. The main challenge is to find the optimal values for the filters and the network architecture  .