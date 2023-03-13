### Batch Normalization

- Batch normalization is a technique that improves the performance and stability of deep neural networks by normalizing the inputs of each layer.
- Batch normalization reduces the internal covariate shift, which is the change in the distribution of layer inputs due to the updates of the previous layers' parameters during training.
- Batch normalization also reduces the dependence of gradients on the scale and initialization of the parameters, which allows the use of higher learning rates and less careful initialization.
- Batch normalization consists of two steps: 
  - First, the inputs of each layer are standardized by subtracting the mean and dividing by the standard deviation of the mini-batch.
  - Second, the standardized inputs are rescaled and shifted by learnable parameters, which allow the network to restore the representation power of the layer if needed.
- Batch normalization can be applied to any layer in the network, such as fully connected layers, convolutional layers, or recurrent layers.
- Batch normalization has several benefits, such as:
  - It accelerates the convergence of the network by reducing the gradient vanishing and exploding problems.
  - It regularizes the network by adding noise to the layer inputs, which reduces overfitting and the need for other regularization techniques such as dropout.
  - It simplifies the network design by making the network less sensitive to the choice of hyperparameters such as learning rate, weight decay, or activation function.
- Batch normalization has some drawbacks, such as:
  - It adds computational complexity and memory overhead to the network, which may slow down the training and inference speed.
  - It introduces dependencies between the samples in the mini-batch, which may affect the performance of the network when the batch size is small or when the data distribution is non-stationary.
  - It may not work well with some types of layers or architectures, such as batch normalization applied to the recurrent connections of an RNN, or batch normalization applied to the generator of a GAN.