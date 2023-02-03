### batch normalization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

Batch normalization is a technique used in deep learning to normalize the activations of a layer in a neural network. The goal of batch normalization is to reduce the internal covariate shift, which is the change in the distribution of activations within a layer over time.

Batch normalization works by normalizing the activations of a layer for each mini-batch of data during training. This normalization is performed by subtracting the mean and dividing by the standard deviation of the activations for each mini-batch. The mean and standard deviation are then used to normalize the activations for each mini-batch during training.

Advantages of batch normalization include:

1. Faster convergence: Batch normalization can help to speed up the convergence of the network by reducing the internal covariate shift.

2. Improved regularization: Batch normalization can act as a regularization technique by adding noise to the activations, which can help to prevent overfitting.

3. Improved network stability: Batch normalization can help to improve the stability of the network by reducing the dependence of the activations on the initialization of the network parameters.

Disadvantages of batch normalization include:

1. Increased computation: Batch normalization requires additional computation to normalize the activations, which can slow down the training process.

2. Increased memory usage: Batch normalization requires additional memory to store the mean and standard deviation for each mini-batch.

In conclusion, batch normalization is a technique used in deep learning to normalize the activations of a layer in a neural network. Batch normalization can help to improve the convergence, regularization, and stability of the network. However, batch normalization also has some disadvantages, including increased computation and memory usage.
