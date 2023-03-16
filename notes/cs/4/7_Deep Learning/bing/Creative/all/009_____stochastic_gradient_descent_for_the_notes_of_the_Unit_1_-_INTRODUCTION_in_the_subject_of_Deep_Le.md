# Stochastic Gradient Descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable) .
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the discrepancy between the predicted and true labels  .
- SGD works by updating the parameters (e.g. weights and biases) of the model in the opposite direction of the gradient of the objective function with respect to the parameters .
- The gradient is computed using a single or a small batch of training examples, which makes SGD faster and more scalable than batch gradient descent, which uses the entire training set  .
- SGD introduces randomness in the optimization process, which can help escape from local minima and find better solutions . However, SGD also has some drawbacks, such as high variance, sensitivity to learning rate and hyperparameters, and difficulty in convergence  .
- There are many variants and extensions of SGD, such as momentum, Nesterov accelerated gradient, AdaGrad, RMSProp, Adam, etc., that aim to improve the performance and stability of SGD  .