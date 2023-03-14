Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch. This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .

The following diagram illustrates the basic architecture of a batch normalization layer:

```
Input layer --> Batch normalization layer --> Activation layer --> Output layer

Input layer: x1, x2, ..., xn
Batch normalization layer: y1, y2, ..., yn
Activation layer: f(y1), f(y2), ..., f(yn)
Output layer: z1, z2, ..., zn

The batch normalization layer performs the following operations:

1. Compute the mean and variance of the inputs for each mini-batch.
2. Normalize the inputs by subtracting the mean and dividing by the square root of the variance plus a small constant epsilon.
3. Scale and shift the normalized inputs by multiplying by a learnable parameter gamma and adding a learnable parameter beta.

Mathematically, the batch normalization layer can be expressed as:

yi = gamma * ((xi - mean) / sqrt(variance + epsilon)) + beta

where gamma and beta are learnable parameters that control the scaling and shifting of the normalized inputs, and epsilon is a small constant to avoid division by zero.

The batch normalization layer also keeps track of the running mean and variance of the inputs over the entire training set, which are used during inference to normalize the inputs of new data.
```