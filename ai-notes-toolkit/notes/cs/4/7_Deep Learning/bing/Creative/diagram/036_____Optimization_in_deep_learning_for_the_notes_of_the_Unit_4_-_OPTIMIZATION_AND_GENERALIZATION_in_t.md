### Optimization in deep learning

- Optimization is the process of finding the optimal values of the parameters (weights and biases) of a deep neural network that minimize a loss function.
- Optimization methods are algorithms that update the parameters iteratively based on the gradients of the loss function with respect to the parameters.
- Optimization methods can be classified into two categories: first-order methods and second-order methods.
- First-order methods use only the first-order derivatives (gradients) of the loss function to update the parameters. They are faster and more scalable than second-order methods, but they may suffer from slow convergence, oscillations, or local minima.
- Second-order methods use the second-order derivatives (Hessian matrix) of the loss function to update the parameters. They are more accurate and robust than first-order methods, but they are computationally expensive and impractical for large-scale problems.
- Some of the most popular first-order optimization methods used in deep learning are:

  - Gradient descent: The simplest and most widely used optimization method. It updates the parameters by taking a small step in the opposite direction of the gradient of the loss function at the current parameter values. It has three variants: batch gradient descent, stochastic gradient descent, and mini-batch gradient descent.
  - Momentum: A technique that accelerates the convergence of gradient descent by adding a fraction of the previous parameter update to the current update. It helps to overcome local minima and reduce oscillations.
  - Nesterov accelerated gradient (NAG): A modification of momentum that incorporates a lookahead step to the gradient calculation. It improves the convergence rate and stability of momentum.
  - Adaptive gradient (AdaGrad): A method that adapts the learning rate for each parameter based on the historical gradients. It helps to deal with sparse and noisy gradients and improves the performance on convex problems.
  - AdaDelta: An extension of AdaGrad that addresses the problem of diminishing learning rates. It uses a moving average of the gradients and the parameter updates to scale the learning rate.
  - RMSProp: A method that also adapts the learning rate for each parameter based on the moving average of the squared gradients. It helps to overcome the problem of exploding and vanishing gradients and improves the performance on non-convex problems.
  - Adaptive moment estimation (Adam): A method that combines the advantages of momentum and RMSProp. It uses the moving averages of both the gradients and the squared gradients to update the parameters. It is one of the most popular and effective optimization methods in deep learning.