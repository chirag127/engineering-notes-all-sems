### Batch Normalization for the Notes of the Unit 2 - DEEP NETWORKS in the Subject of Deep Learning

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks.
- Batch normalization also provides some regularization, reducing generalization error.
- Batch normalization addresses the problem of internal covariate shift, which is the change in the distribution of inputs to layers deep in the network after each weight update.
- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation.
- Batch normalization adds two additional trainable parameters to a layer: the normalized output that’s multiplied by a gamma (standard deviation) parameter, and the additional beta (mean) parameter.
- Batch normalization works together with gradient descent so that data can be “denormalized” by simply changing just these two weights for each output.
- Batch normalization can be applied to either the activations of a prior layer or inputs directly.
- Batch normalization can be implemented in Keras and TensorFlow 2 using the BatchNormalization layer.
- Batch normalization can be used before or after the activation function, depending on the preference.
- Batch normalization can improve the performance and stability of artificial neural networks.

#### Mnemonics and Learning Tricks

- One possible mnemonic to remember the formula for batch normalization is: **B**atch **N**ormalization = **B**atch **M**ean **S**ubtraction / **B**atch **S**tandard **D**eviation
- Another possible mnemonic to remember the benefits of batch normalization is: **B**atch **N**ormalization = **B**etter **N**etworks
- A possible learning trick to understand the concept of batch normalization is to imagine a group of students taking a test. If the test is too easy or too hard, the scores will be skewed and not representative of the students' abilities. But if the test is normalized, meaning the scores are adjusted to have a mean of zero and a standard deviation of one, then the scores will be more comparable and fair. Similarly, batch normalization adjusts the inputs to a layer to have a mean of zero and a standard deviation of one, making them more comparable and fair for the next layer.