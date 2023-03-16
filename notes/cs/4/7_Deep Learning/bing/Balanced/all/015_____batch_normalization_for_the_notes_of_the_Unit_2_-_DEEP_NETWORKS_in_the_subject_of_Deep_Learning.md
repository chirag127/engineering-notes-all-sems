# Batch Normalization for Deep Networks

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- Batch normalization also helps to avoid overfitting and improve generalization by reducing the internal covariate shift, which is the change in the distribution of each layer's inputs during training as the parameters of the previous layers change.
- Batch normalization can be applied to either the activations of a prior layer or to the inputs directly.
- Batch normalization involves two steps: 
  - First, the mean and standard deviation of the mini-batch are computed and used to normalize the inputs.
  - Second, the normalized inputs are scaled and shifted by two learnable parameters, gamma and beta, which control the mean and variance of the outputs.
- Batch normalization can be implemented as a layer in a deep network, and it is usually placed before the activation function of the layer .
- Batch normalization has several advantages, such as:
  - Accelerating the training process by allowing higher learning rates and less careful initialization.
  - Providing some regularization effect by adding noise to the inputs of each layer.
  - Reducing the dependence on other regularization techniques, such as dropout or weight decay .
  - Enhancing the performance of various network architectures, such as convolutional, recurrent, and generative adversarial networks.