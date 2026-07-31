# Batch Normalization for Deep Networks

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- Batch normalization has the following advantages  :
  - It stabilizes the learning process and reduces the number of training epochs required to train deep networks.
  - It reduces the internal covariate shift, which is the change in the distribution of layer inputs due to the change in parameters of previous layers.
  - It allows the use of higher learning rates and less careful initialization.
  - It acts as a regularizer and reduces the need for dropout.
- Batch normalization can be applied to either the activations of a prior layer or to the inputs directly.
- Batch normalization requires keeping track of the running mean and standard deviation of the mini-batches during training, and using them to normalize the layer inputs during testing .
- Batch normalization can be implemented as a layer in a deep neural network, and is usually placed before the activation function .