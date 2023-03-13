### Weights Initialization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Weight initialization is a procedure to set the weights of a neural network to small random values that define the starting point for the optimization (learning or training) of the neural network model.
- Weight initialization is important because it affects the convergence and performance of the model. If the weights are too small, the signal may vanish during the forward and backward propagation. If the weights are too large, the signal may explode and cause numerical instability.
- Different weight initialization techniques have been proposed for different activation functions and network architectures. Some of the common techniques are:

  - **Zero initialization**: All the weights are set to zero. This is not a good technique because it makes the network symmetric and prevents it from learning anything.
  - **Random initialization**: The weights are randomly sampled from a uniform or normal distribution. This introduces some diversity and breaks the symmetry, but it may also cause problems such as poor gradient flow, slow convergence, or local minima.
  - **Xavier initialization**: The weights are randomly sampled from a normal distribution with mean zero and variance 1/√n, where n is the number of inputs to the layer. This technique tries to balance the variance of the inputs and outputs of each layer, and works well for sigmoid and tanh activation functions .
  - **He initialization**: The weights are randomly sampled from a normal distribution with mean zero and variance 2/√n, where n is the number of inputs to the layer. This technique is a modification of Xavier initialization for ReLU activation function, and it helps to avoid the vanishing gradient problem  .
  - **Orthogonal initialization**: The weights are randomly sampled from an orthogonal matrix, which preserves the norm and angle of the inputs during the forward propagation. This technique is useful for recurrent neural networks, where the weights are shared across time steps.

- Some mnemonics and learning tricks for weight initialization are:

  - **Zero initialization**: Zero is a hero, but not for weight initialization.
  - **Random initialization**: Random is better than zero, but not optimal for every scenario.
  - **Xavier initialization**: Xavier is the savior for sigmoid and tanh layers.
  - **He initialization**: He is the key for ReLU layers.
  - **Orthogonal initialization**: Orthogonal is normal for recurrent neural networks.