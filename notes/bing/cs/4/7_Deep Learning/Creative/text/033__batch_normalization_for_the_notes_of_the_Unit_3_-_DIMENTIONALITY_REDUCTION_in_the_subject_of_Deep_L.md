### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- Batch normalization has the following benefits:
  - It stabilizes the learning process by reducing the internal covariate shift, which is the change in the distribution of layer inputs due to the update of network parameters .
  - It accelerates the training process by allowing higher learning rates and less careful initialization .
  - It provides some regularization effect by adding noise to the layer inputs .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly .
- Batch normalization requires estimating the mean and standard deviation for each mini-batch and keeping track of a running average of these statistics to use during inference .
- Batch normalization is implemented as a layer in most deep learning frameworks, such as Keras and TensorFlow .