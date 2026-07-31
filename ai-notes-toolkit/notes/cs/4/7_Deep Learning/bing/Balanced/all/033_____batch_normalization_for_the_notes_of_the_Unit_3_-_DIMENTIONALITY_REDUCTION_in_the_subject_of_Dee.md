# Batch Normalization

- Batch normalization is a technique that aims to improve the performance and stability of neural networks by normalizing the inputs of each layer, i.e., making them have mean zero and standard deviation one.
- Batch normalization can reduce the dependence of gradients on the scale of the parameters or their initial values, which can accelerate the convergence of the training process and reduce the need for careful parameter initialization or small learning rates.
- Batch normalization can also act as a regularizer, reducing the need for other regularization techniques such as dropout or weight decay, by adding some noise to the inputs of each layer during training.
- Batch normalization is applied to the inputs of each layer before the activation function, using the statistics of the mini-batch. Specifically, for a mini-batch of size m, the batch normalization algorithm computes the mean and variance of the inputs as follows:

$$\mu_B = \frac{1}{m} \sum_{i=1}^m x_i$$

$$\sigma_B^2 = \frac{1}{m} \sum_{i=1}^m (x_i - \mu_B)^2$$

- Then, the inputs are normalized by subtracting the mean and dividing by the standard deviation, and scaled and shifted by two learnable parameters, gamma and beta, as follows:

$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$

$$y_i = \gamma \hat{x}_i + \beta$$

- The epsilon term is a small constant added for numerical stability. The gamma and beta parameters are learned during training and allow the network to restore the original scale and shift of the inputs if needed.
- During inference, the mean and variance of the inputs are not computed from the mini-batch, but from the entire training set, using moving averages. This ensures that the outputs of the network are deterministic and not affected by the randomness of the mini-batch selection.
- Batch normalization can be applied to any type of layer, such as fully connected, convolutional, or recurrent layers. However, the computation of the mean and variance may differ depending on the layer type and the data format. For example, for convolutional layers, the mean and variance are computed for each feature map across the spatial dimensions and the mini-batch, and the same gamma and beta parameters are used for each spatial location.