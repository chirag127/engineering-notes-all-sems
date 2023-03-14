### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks.
- Batch normalization also provides some regularization, reducing generalization error.
- Batch normalization works by affecting the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- Batch normalization adds two additional trainable parameters to each layer: a scale parameter (gamma) and a shift parameter (beta) .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly.
- Batch normalization can lead to faster learning rates, lower dropout rates, and more independent layer learning.