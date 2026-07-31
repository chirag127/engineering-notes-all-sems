### What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and the output layers.
- A shallow network can be seen as a function that maps an input vector **x** to an output vector **y** by applying a series of linear and nonlinear transformations.
- The output of the hidden layer is given by **h = f(Wx + b)**, where **W** is a weight matrix, **b** is a bias vector, and **f** is an activation function that introduces nonlinearity.
- The output of the network is given by **y = g(Vh + c)**, where **V** is another weight matrix, **c** is another bias vector, and **g** is another activation function that may or may not be different from **f**.
- A shallow network can compute a variety of functions, depending on the choice of the activation functions and the values of the parameters **W**, **b**, **V**, and **c**.
- A shallow network can approximate any continuous function on a compact domain to any desired degree of accuracy, as long as it has enough hidden units. This is known as the universal approximation theorem.
- A shallow network can also learn to classify data into different categories, by using a suitable loss function and a training algorithm that adjusts the parameters to minimize the loss on a given dataset.
- A shallow network can be trained using gradient-based methods, such as gradient descent or stochastic gradient descent, that compute the partial derivatives of the loss function with respect to the parameters and update them in the opposite direction of the gradient.
- A shallow network can be visualized as a computational graph, where each node represents a variable or an operation, and each edge represents a dependency or a flow of information. The graph can be used to compute the forward pass (from input to output) and the backward pass (from output to input) of the network.