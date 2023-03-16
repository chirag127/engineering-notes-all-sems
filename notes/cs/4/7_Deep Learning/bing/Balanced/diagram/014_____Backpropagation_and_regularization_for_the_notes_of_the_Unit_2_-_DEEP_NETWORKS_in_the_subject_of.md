### Backpropagation and regularization

Backpropagation is a method of training neural networks by computing the gradients of the loss function with respect to the weights and biases of the network. It consists of two phases: forward propagation and backward propagation.

- Forward propagation: The input data is fed into the network and the output is computed by applying the activation functions and the weights and biases of each layer. The output is compared with the target labels and the loss function is calculated.
- Backward propagation: The loss function is differentiated with respect to the weights and biases of each layer, using the chain rule of calculus. The gradients are propagated from the output layer to the input layer, updating the weights and biases along the way by subtracting a fraction of the gradients (called the learning rate).

Regularization is a technique of preventing overfitting in neural networks by adding a penalty term to the loss function. Overfitting occurs when the network learns the noise or the specific patterns of the training data, rather than the general features of the problem. Regularization reduces the complexity of the network and makes it more generalizable to unseen data.

Some common regularization methods are:

- L2 regularization: The penalty term is the sum of the squares of the weights, multiplied by a regularization parameter (lambda). This shrinks the weights towards zero and reduces their influence on the output.
- L1 regularization: The penalty term is the sum of the absolute values of the weights, multiplied by a regularization parameter (lambda). This also shrinks the weights towards zero, but also induces sparsity, meaning some weights become exactly zero and are eliminated from the network.
- Dropout: A random fraction of the neurons in each layer are temporarily removed from the network during training, along with their connections. This reduces the co-dependency of the neurons and forces the network to learn more robust features. The dropout rate is a hyperparameter that controls the fraction of neurons to be dropped. During testing, all the neurons are used, but their outputs are scaled down by the dropout rate to maintain the expected output.
- Batch normalization: The inputs or the outputs of each layer are normalized by subtracting the mean and dividing by the standard deviation of the mini-batch. This reduces the internal covariate shift, meaning the distribution of the inputs or outputs of each layer does not change significantly during training. This speeds up the convergence and reduces the sensitivity to the initialization and the learning rate of the network. Batch normalization also has a regularizing effect, as it adds some noise to the inputs or outputs of each layer.