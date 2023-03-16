### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- Batch normalization has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization can be applied to either the activations of a prior layer or to the inputs directly.
- Batch normalization was proposed by Sergey Ioffe and Christian Szegedy in their paper "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift" in 2015.
- Batch normalization reduces the internal covariate shift, which is the change in the distribution of layer inputs during training, as the parameters of the previous layers change.
- Batch normalization allows the use of higher learning rates, as it makes the network less sensitive to the scale and initialization of the parameters.
- Batch normalization can be implemented as a layer in a deep neural network, with learnable parameters that control the mean and variance of the normalized inputs.