### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .
- Batch normalization also provides some regularization, reducing generalization error.

#### Why Batch Normalization?

- Training deep neural networks with tens of layers is challenging as they can be sensitive to the initial random weights and configuration of the learning algorithm.
- One possible reason for this difficulty is the distribution of the inputs to layers deep in the network may change after each mini-batch when the weights are updated. This can cause the learning algorithm to forever chase a moving target.
- This change in the distribution of inputs to layers in the network is referred to the technical name “internal covariate shift”.
- Batch normalization addresses this problem by normalizing the inputs to each layer so that they have a mean of zero and a standard deviation of one .
- This ensures that the inputs to each layer have a consistent and stable distribution, and the network can learn faster and more effectively .

#### How Batch Normalization Works?

- To enhance the stability of a deep learning network, batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- Since this shifting or scaling of outputs by a randomly initialized parameter reduces the accuracy of the weights in the next layer, a stochastic gradient descent is applied to remove this normalization if the loss function is too high .
- The end result is batch normalization adds two additional trainable parameters to a layer: The normalized output that’s multiplied by a gamma (standard deviation) parameter, and the additional beta (mean) parameter .
- This is why batch normalization works together with gradient descents so that data can be “denormalized” by simply changing just these two weights for each output .
- This leads to less data loss and increased stability across the network by changing all the other relevant weights .

#### Tips for Using Batch Normalization

- Batch normalization can be applied to either the activations of a prior layer or inputs directly.
- Batch normalization is usually placed before the activation function of a layer, but after the convolution or linear transformation.
- Batch normalization can be used with most types of neural networks, such as convolutional, recurrent, and feedforward.
- Batch normalization can improve the performance of networks that use activation functions that are sensitive to the scale of their inputs, such as sigmoid, tanh, and relu.
- Batch normalization can also reduce the need for other regularization techniques, such as dropout or weight decay.