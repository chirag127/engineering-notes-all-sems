### Weights Initialization

- Weight initialization is a procedure to set the weights of a neural network to small random values that define the starting point for the optimization (learning or training) of the neural network model  .
- Weight initialization is a very important concept in deep neural networks and using the right initialization technique can heavily affect the accuracy of the deep learning model.
- An appropriate weight initialization technique must be employed, taking various factors such as activation function used, into consideration.
- Some common weight initialization techniques are:

  - **Zero initialization**: Setting all the weights to zero. This is not a good technique as it leads to symmetry and prevents the network from learning anything.
  - **Random initialization**: Setting the weights to small random values, usually drawn from a normal or uniform distribution. This breaks the symmetry and allows the network to learn different features.
  - **Xavier initialization**: Setting the weights to random values scaled by a factor of $\sqrt{\frac{1}{n_{in}}}$, where $n_{in}$ is the number of incoming connections to a node. This technique is suitable for nodes that use sigmoid or tanh activation functions, as it helps to keep the variance of the activations and gradients consistent across layers .
  - **He initialization**: Setting the weights to random values scaled by a factor of $\sqrt{\frac{2}{n_{in}}}$, where $n_{in}$ is the number of incoming connections to a node. This technique is suitable for nodes that use ReLU activation functions, as it helps to avoid the problem of vanishing gradients .
  - **Bias initialization**: Setting the bias terms to zero or small positive values. This helps to avoid the problem of dead neurons and allows the network to learn the bias from the data .