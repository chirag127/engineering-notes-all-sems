### Weights Initialization

- Weights initialization is the process of assigning initial values to the parameters of a neural network before training.
- It is important to choose appropriate weights initialization methods because they can affect the convergence, speed, and performance of the network.
- Some common methods of weights initialization are:

  - **Random initialization**: Assigning random values to the weights, usually from a normal or uniform distribution. This can help to break the symmetry of the network and avoid the problem of vanishing or exploding gradients. However, random initialization can also lead to poor results if the scale of the weights is too large or too small.

  - **Xavier initialization**: Assigning weights based on the fan-in and fan-out of the network, which are the number of input and output units for each layer. This can help to balance the variance of the weights and the gradients across the layers. The formula for Xavier initialization is:

    `w = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in)`

  - **He initialization**: A variation of Xavier initialization that is suitable for networks with ReLU activation functions. It uses a larger scale factor for the weights to avoid the problem of dying ReLU units. The formula for He initialization is:

    `w = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in / 2)`

  - **Orthogonal initialization**: Assigning weights that are orthogonal to each other, meaning that they have zero correlation. This can help to preserve the information flow and gradient propagation in the network. The weights are obtained by applying a QR decomposition to a random matrix and then scaling it by a factor.

  - **Sparse initialization**: Assigning weights that are mostly zero, except for a few non-zero values per column. This can help to reduce the number of parameters and improve the sparsity of the network. The non-zero values are usually drawn from a normal distribution.

Some additional points are:

- Weights initialization can also be influenced by the choice of activation functions, learning rate, regularization, and optimization algorithms.
- There is no single best method of weights initialization for all networks and problems. It is advisable to experiment with different methods and compare their results.
- Weights initialization can also be combined with other techniques such as batch normalization, dropout, and skip connections to improve the performance and stability of the network.