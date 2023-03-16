### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- It affects the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- It reduces the internal covariate shift, which is the change in the distribution of layer inputs during training due to the change in parameters of previous layers.
- It has several advantages, such as:
  - It accelerates the training process by allowing higher learning rates and reducing the dependence on initialization  .
  - It provides some regularization effect by adding noise to the layer inputs and reducing the need for dropout  .
  - It makes the network more robust to different hyperparameters and input scales  .
- It has some drawbacks, such as:
  - It adds computational complexity and memory overhead to the network .
  - It introduces a dependence on the batch size and may not work well for small or varying batch sizes .
  - It may not be compatible with some network architectures or optimization methods .
- It can be implemented as a layer in the network, usually after the activation function of a hidden layer or before the activation function of the output layer  .
- It has two learnable parameters, gamma and beta, that scale and shift the normalized inputs respectively   .
- It can be applied differently during training and inference, using either the mini-batch statistics or the moving average statistics for normalization   .