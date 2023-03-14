### Weights Initialization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Weight initialization is a procedure to set the weights of a neural network to small random values that define the starting point for the optimization (learning or training) of the neural network model .
- Weight initialization is an important design choice when developing deep learning neural network models, as it can affect the convergence and performance of the model .
- Different weight initialization techniques have been proposed for different types of activation functions and network architectures .
- Some of the common weight initialization techniques are:

  - **Xavier weight initialization**: This technique is also known as Glorot initialization, named after the first author of the paper that proposed it. It is suitable for nodes that use the sigmoid or tanh activation functions. It initializes the weights by drawing random values from a uniform distribution in the range [-a, a], where a = sqrt(6 / (n_in + n_out)), and n_in and n_out are the number of inputs and outputs of the node, respectively. This technique aims to keep the variance of the inputs and outputs of each layer as close as possible.
  - **Normalized Xavier weight initialization**: This technique is a variation of the Xavier initialization that uses a normal distribution instead of a uniform distribution. It initializes the weights by drawing random values from a normal distribution with mean zero and standard deviation sigma, where sigma = sqrt(2 / (n_in + n_out)). This technique has similar properties as the Xavier initialization, but may have slightly different effects on the optimization process.
  - **He weight initialization**: This technique is also known as Kaiming initialization, named after the first author of the paper that proposed it. It is suitable for nodes that use the ReLU activation function. It initializes the weights by drawing random values from a normal distribution with mean zero and standard deviation sigma, where sigma = sqrt(2 / n_in), and n_in is the number of inputs of the node. This technique aims to keep the variance of the outputs of each layer as close as possible, while avoiding the problem of vanishing or exploding gradients.

- Some of the advantages and disadvantages of these techniques are:

  - **Xavier weight initialization**:
    - Advantages: It can help the model converge faster and achieve better performance than random initialization. It can prevent the saturation of the sigmoid and tanh activation functions.
    - Disadvantages: It may not work well for nodes that use the ReLU activation function, as it can cause the outputs to be too small and the gradients to vanish.
  - **Normalized Xavier weight initialization**:
    - Advantages: It has similar advantages as the Xavier initialization, but may be more robust to outliers and noise in the data.
    - Disadvantages: It has similar disadvantages as the Xavier initialization, and may also introduce more variance in the weights than the uniform distribution.
  - **He weight initialization**:
    - Advantages: It can help the model converge faster and achieve better performance than random initialization for nodes that use the ReLU activation function. It can prevent the vanishing or exploding gradients problem that may occur with the ReLU activation function.
    - Disadvantages: It may not work well for nodes that use the sigmoid or tanh activation functions, as it can cause the outputs to be too large and the gradients to explode.

- Some of the mnemonics and learning tricks for these techniques are:

  - **Xavier weight initialization**: Remember that it uses a uniform distribution and the formula a = sqrt(6 / (n_in + n_out)), where n_in and n_out are the number of inputs and outputs of the node. You can think of the 6 as the number of letters in Xavier, and the + sign as a cross or an X.
  - **Normalized Xavier weight initialization**: Remember that it uses a normal distribution and the formula sigma = sqrt(2 / (n_in + n_out)), where n_in and n_out are the number of inputs and outputs of the node. You can think of the 2 as the number of letters in He, and the + sign as a cross or an X.
  - **He weight initialization**: Remember that it uses a normal