### Batch Normalization for Deep Networks

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- Batch normalization has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization can be applied to either the activations of a prior layer or to the inputs directly.
- Batch normalization is implemented as a layer in the network, usually after a convolutional or fully connected layer and before a nonlinearity layer .
- Batch normalization has two learnable parameters, gamma and beta, which scale and shift the normalized output respectively  .
- Batch normalization requires keeping track of the running mean and variance of each layer during training, and using those statistics during inference .
- Batch normalization was proposed by Sergey Ioffe and Christian Szegedy in 2015 in their paper "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift".