### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a technique for computing the gradients of the loss function with respect to the weights and biases of a deep neural network. It is based on the chain rule of calculus, which allows us to express the derivative of a composite function as the product of the derivatives of its components.
- Backpropagation consists of two phases: a forward pass and a backward pass. In the forward pass, the network computes the output for a given input and compares it with the desired output (the label or target). The difference between the output and the target is the loss or error. In the backward pass, the network propagates the error from the output layer to the input layer, updating the weights and biases along the way according to the gradient descent rule.
- The gradient descent rule is a simple algorithm for finding the minimum of a function by iteratively moving in the opposite direction of the gradient (the slope or direction of steepest descent). The gradient descent rule for updating a weight w is:

  `w = w - alpha * dL/dw`

  where alpha is the learning rate (a hyperparameter that controls the size of the update step) and dL/dw is the partial derivative of the loss function L with respect to w.

- The gradient descent rule for updating a bias b is similar:

  `b = b - alpha * dL/db`

- The partial derivatives dL/dw and dL/db can be computed using the chain rule. For example, if we have a network with two layers, a hidden layer h and an output layer y, and a loss function L, then the partial derivative of L with respect to a weight w connecting the input x to the hidden layer h is:

  `dL/dw = dL/dy * dy/dh * dh/dw`

  where dL/dy is the derivative of the loss function with respect to the output, dy/dh is the derivative of the output with respect to the hidden layer, and dh/dw is the derivative of the hidden layer with respect to the weight.

- The chain rule can be applied recursively to compute the gradients for deeper networks with more layers. The key idea is to store the intermediate values of the forward pass (such as the activations and the derivatives of the activation functions) and use them in the backward pass to avoid redundant computations.

- Regularization is a technique for reducing overfitting, which is a common problem in deep learning. Overfitting occurs when the network learns the training data too well and fails to generalize to new or unseen data. Overfitting can be detected by monitoring the training and validation errors. If the training error is much lower than the validation error, the network is overfitting.

- Regularization aims to prevent overfitting by adding a penalty term to the loss function that depends on the complexity of the network. The penalty term can be based on different measures of complexity, such as the number of parameters, the magnitude of the weights, or the sparsity of the activations. The most common regularization techniques are:

  - L2 regularization: This technique adds a penalty term proportional to the sum of the squares of the weights to the loss function. This encourages the network to use smaller weights, which reduces the variance of the output and makes the network less sensitive to small changes in the input. The penalty term is:

    `lambda/2 * sum(w^2)`

    where lambda is the regularization parameter (a hyperparameter that controls the strength of the regularization) and w is a weight.

  - L1 regularization: This technique adds a penalty term proportional to the sum of the absolute values of the weights to the loss function. This encourages the network to use sparse weights, which means that many weights are zero or close to zero. This reduces the number of effective parameters and makes the network more interpretable. The penalty term is:

    `lambda * sum(|w|)`

    where lambda is the regularization parameter and w is a weight.

  - Dropout: This technique randomly drops out (sets to zero) some of the units in the network during training. This prevents the network from relying too much on specific units and forces it to learn more robust features. Dropout can be applied to any layer in the network, but it is more effective on the hidden layers. The dropout rate is the probability of dropping out a unit (a hyperparameter that controls the amount of dropout). Dropout can be seen as a form of ensemble learning, where the network averages the predictions of many subnetworks with different architectures.