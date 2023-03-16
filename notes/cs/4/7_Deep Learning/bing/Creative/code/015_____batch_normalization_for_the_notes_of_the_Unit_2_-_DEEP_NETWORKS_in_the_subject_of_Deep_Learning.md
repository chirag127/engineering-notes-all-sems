### Batch Normalization for Deep Networks

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- Batch normalization has the following advantages   :
  - It stabilizes the learning process by reducing the internal covariate shift, which is the change in the distribution of layer inputs during training.
  - It accelerates the training process by allowing higher learning rates and less careful initialization.
  - It acts as a regularizer by adding some noise to the layer inputs, and reduces the need for other regularization techniques such as dropout.
  - It improves the generalization performance by reducing the overfitting to the training data.
- Batch normalization can be applied to different types of layers, such as fully connected, convolutional, recurrent, etc.
- Batch normalization has some drawbacks, such as :
  - It adds some computational overhead and memory usage to the network.
  - It introduces some hyperparameters, such as the momentum and epsilon for the running mean and variance estimates.
  - It may reduce the representational power of some layers, such as the first and last ones.
  - It may not work well with some activation functions, such as sigmoid or tanh, that have limited range.