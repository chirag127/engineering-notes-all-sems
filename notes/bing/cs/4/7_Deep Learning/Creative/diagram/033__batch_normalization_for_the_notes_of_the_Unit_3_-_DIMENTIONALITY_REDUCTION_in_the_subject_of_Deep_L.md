Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch. This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .

The following diagram illustrates the basic architecture of a batch normalization layer:

```
Input layer: x1, x2, ..., xn
|
|  Forward pass
|
v
Batch normalization layer: y1, y2, ..., yn
|  Compute mean and variance of mini-batch
|  y_i = (x_i - mean) / sqrt(variance + epsilon)
|  y_i = gamma * y_i + beta
|  gamma and beta are learnable parameters
|
|  Backward pass
|
v
Output layer: z1, z2, ..., zn
```

The batch normalization layer computes the mean and variance of the mini-batch inputs and normalizes them by subtracting the mean and dividing by the square root of the variance plus a small constant epsilon. Then, it applies a linear transformation by multiplying the normalized inputs by a learnable parameter gamma and adding another learnable parameter beta. These parameters allow the layer to adjust the scale and shift of the normalized inputs to preserve the expressive power of the network. The backward pass computes the gradients of the loss function with respect to the inputs, outputs, and parameters of the batch normalization layer using the chain rule of differentiation.