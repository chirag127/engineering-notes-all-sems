### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- Batch normalization has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization was proposed by Sergey Ioffe and Christian Szegedy in 2015 in their paper "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift" .
- Batch normalization can be applied to either the activations of a prior layer or to the inputs directly.
- Batch normalization can be implemented using the BatchNormalization layer in Keras or the torch.nn.BatchNorm2d module in PyTorch.