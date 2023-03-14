### Batch Normalization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks.
- Batch normalization also provides some regularization, reducing generalization error.
- Batch normalization works by subtracting the batch mean and dividing by the batch standard deviation of the inputs to a layer .
- This ensures that the inputs to a layer have a mean of zero and a standard deviation of one, which are desirable properties for neural network inputs.
- Batch normalization also adds two trainable parameters to each layer: a scale factor (gamma) and a shift factor (beta) .
- These parameters allow the network to learn the optimal mean and variance for each layer's inputs, and can be used to undo the normalization if needed .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly.
- Batch normalization is usually applied before the activation function of a layer.
- Batch normalization can be implemented using the `BatchNormalization` layer in Keras or the `tf.keras.layers.BatchNormalization` layer in TensorFlow 2.
- Batch normalization has some advantages and disadvantages:

  - Advantages:
    - It accelerates the training process by allowing higher learning rates and reducing the dependence on initialization .
    - It reduces the need for other regularization techniques such as dropout or weight decay .
    - It makes the network more robust to changes in the input distribution .
  - Disadvantages:
    - It adds computational complexity and memory overhead to the network .
    - It introduces hyperparameters such as momentum and epsilon that need to be tuned .
    - It may reduce the interpretability of some features or gradients .

- A possible mnemonic to remember the steps of batch normalization is:

  - **B**atch mean and standard deviation
  - **A**lign inputs by subtracting mean and dividing by standard deviation
  - **T**rainable parameters: scale and shift
  - **C**hoose where to apply: before or after activation
  - **H**yperparameters: momentum and epsilon

- A possible learning trick to understand the intuition behind batch normalization is to imagine a scenario where the inputs to a layer are either too large or too small, causing the activation function to saturate and produce gradients close to zero. This would slow down the learning process and make the network sensitive to the initial weights. By normalizing the inputs, the activation function can operate in a more linear region, where the gradients are larger and more informative. This would speed up the learning process and make the network more robust to the initial weights.