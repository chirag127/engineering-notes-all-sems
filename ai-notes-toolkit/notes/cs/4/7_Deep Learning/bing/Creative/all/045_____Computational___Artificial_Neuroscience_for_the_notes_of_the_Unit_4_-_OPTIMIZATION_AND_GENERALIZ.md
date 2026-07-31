# Computational & Artificial Neuroscience

## Unit 4 - OPTIMIZATION AND GENERALIZATION

- Optimization and generalization are two key aspects of learning in artificial neural networks.
- Optimization refers to the process of finding the optimal set of parameters (weights and biases) that minimize a loss function (a measure of the discrepancy between the network's output and the desired output) on a given training dataset.
- Generalization refers to the ability of the network to perform well on new and unseen data that are not part of the training dataset, i.e., to avoid overfitting or underfitting.
- Optimization and generalization are closely related, as the choice of the optimization algorithm, the network architecture, the regularization techniques, and the hyperparameters can affect both the speed and the quality of the learning process.

### Optimization Algorithms

- Optimization algorithms are methods that iteratively update the network's parameters based on some rules or heuristics, usually involving the gradient of the loss function with respect to the parameters.
- The gradient is a vector that points in the direction of the steepest ascent of the loss function, and thus the negative gradient points in the direction of the steepest descent.
- The most common optimization algorithm is gradient descent, which updates the parameters by taking small steps in the opposite direction of the gradient, proportional to a learning rate parameter.
- Gradient descent can be applied in different ways, such as batch, mini-batch, or stochastic, depending on how the training data are divided and used to compute the gradient.
- Gradient descent can also be modified or enhanced by using different techniques, such as momentum, Nesterov accelerated gradient, adaptive gradient, RMSprop, Adam, etc., to improve the convergence and stability of the optimization process.

### Generalization Techniques

- Generalization techniques are methods that aim to improve the network's performance on new and unseen data, by reducing the gap between the training and test errors, or by increasing the network's robustness to noise and variations in the input data.
- Some generalization techniques are applied during the optimization process, such as regularization, early stopping, dropout, batch normalization, etc., to prevent or penalize overfitting or underfitting.
- Other generalization techniques are applied after the optimization process, such as cross-validation, model selection, ensemble methods, etc., to evaluate and compare the network's performance on different datasets or models.