 Here is the content in markdown format for the given topic:

### Factors affecting Backpropagation training

The following are the major factors that affect the training of a neural network using Backpropagation algorithm:

1. Learning rate (η): The learning rate controls the size of the weight updates. If the learning rate is too large, the network may oscillate and become unstable. If the learning rate is too small, the training will take a very long time to converge. An optimum value of learning rate should be chosen for efficient and stable training.
2. Momentum (α): Momentum is a technique that adds a fraction of the previous weight update to the current one. This accelerates convergence in the relevant direction and dampens oscillations. An optimum value of momentum should be chosen based on the problem.
3. Weight initialization: The initial weights chosen for the network can affect the training. If the weights are too large, the gradients may be very small and training will be slow. If the weights are too small, the gradients may be large and training will be unstable. Normal distribution random initialization is commonly used.
4. Number of hidden layers and neurons: The network architecture in terms of number of hidden layers and number of neurons in each layer is an important factor. Having too few hidden neurons may lead to underfitting and too many may lead to overfitting. The number of layers and neurons should be chosen based on the complexity of the problem.
5. Training data: The training data should be representative of the input space. If the training data does not adequately cover the input space, the network may not generalize well to new input patterns. The training data should be sufficiently large and varied to enable the network to capture the underlying patterns.
6. Preprocessing: Data preprocessing steps like normalization, scaling, etc help in improved training by accelerating convergence and avoiding issues like saturation of activation functions. Appropriate preprocessing of data is necessary for efficient training.

[You can include diagrams, examples, code snippets, etc here if required for better understanding]

The training of a neural network is an iterative process and the performance can be improved by tuning the various factors mentioned above and arriving at their optimal values for the problem. Proper choice of the training parameters and architecture can lead to a well-trained network that generalizes well to new patterns.