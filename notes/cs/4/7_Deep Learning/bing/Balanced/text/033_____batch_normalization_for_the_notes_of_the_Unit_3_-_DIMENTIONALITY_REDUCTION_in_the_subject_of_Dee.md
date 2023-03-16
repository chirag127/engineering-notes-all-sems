### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- It affects the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- It has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- It also provides some regularization effect, reducing the need for dropout or weight decay .
- It can be applied to either the activations of a prior layer or to the inputs directly.
- It was proposed by Sergey Ioffe and Christian Szegedy in 2015.
- It is based on the idea of reducing the internal covariate shift, which is the change in the distribution of layer inputs during training due to the change of parameters in previous layers.
- It involves adding two learnable parameters, gamma and beta, to scale and shift the normalized inputs.
- It can be implemented as a layer in a deep neural network, usually after the activation function or before the linear transformation .
- It can improve the performance and convergence of various deep learning models, such as convolutional neural networks, recurrent neural networks, and generative adversarial networks .