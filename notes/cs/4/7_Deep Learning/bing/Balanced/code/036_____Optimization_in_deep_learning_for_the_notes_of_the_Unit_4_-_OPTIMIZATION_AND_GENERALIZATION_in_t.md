### Optimization in deep learning

- Optimization is the process of finding the optimal values of the parameters (weights and biases) of a deep neural network that minimize a loss function.
- Optimization methods are algorithms that update the parameters iteratively based on the gradients of the loss function with respect to the parameters.
- Optimization methods can be classified into two categories: first-order methods and second-order methods.
- First-order methods only use the first-order derivatives (gradients) of the loss function, while second-order methods also use the second-order derivatives (Hessian matrix) or approximations of them.
- First-order methods are more popular and widely used in deep learning, because they are faster and more scalable than second-order methods, especially for large-scale problems with millions of parameters and data points.
- Some of the common first-order optimization methods used in deep learning are:

  - Gradient descent: The simplest and most basic optimization method, which updates the parameters in the opposite direction of the gradients with a fixed learning rate.
  - Momentum: A method that accelerates the convergence of gradient descent by adding a momentum term to the parameter update, which is a fraction of the previous update. This helps to overcome local minima and oscillations.
  - Nesterov accelerated gradient (NAG): A variant of momentum that incorporates a lookahead step to the parameter update, which improves the accuracy of the gradients and the convergence speed.
  - Adaptive gradient (AdaGrad): A method that adapts the learning rate for each parameter based on the historical gradients, which reduces the need for manual tuning of the learning rate and improves the performance for sparse gradients.
  - AdaDelta: A modification of AdaGrad that addresses the problem of diminishing learning rates by using a moving average of the gradients and the parameter updates, which makes the method more robust and stable.
  - RMSProp: A method that also adapts the learning rate for each parameter based on the moving average of the squared gradients, which prevents the learning rate from becoming too small and improves the performance for non-stationary objectives.
  - Adaptive moment estimation (Adam): A method that combines the advantages of momentum and RMSProp, by using both the moving average of the gradients and the squared gradients to update the parameters, which makes the method suitable for a wide range of problems and datasets.

- Optimization methods can also be influenced by other factors, such as the choice of the loss function, the initialization of the parameters, the regularization techniques, the batch size, the learning rate schedule, and the stopping criteria.