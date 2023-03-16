### Optimization in deep learning

- Optimization is the process of finding the optimal values of the parameters (weights and biases) of a deep neural network that minimize a loss function.
- Optimization methods are algorithms that update the parameters iteratively based on the gradients of the loss function with respect to the parameters.
- Optimization methods can be classified into two categories: first-order methods and second-order methods.
- First-order methods only use the first-order derivatives (gradients) of the loss function, while second-order methods also use the second-order derivatives (Hessian matrix) or approximations of them.
- First-order methods are more widely used in deep learning because they are faster and more scalable than second-order methods, which require more computation and memory.
- Some of the most common first-order optimization methods in deep learning are:

  - Gradient descent: the simplest and most basic optimization method, which updates the parameters by subtracting a fraction of the gradient from the current values.
  - Momentum: a method that adds a momentum term to the gradient descent update, which helps to accelerate the convergence and overcome local minima or saddle points.
  - Nesterov accelerated gradient (NAG): a method that improves the momentum method by using a lookahead gradient, which reduces the overshooting and oscillations of the update.
  - Adaptive gradient (AdaGrad): a method that adapts the learning rate for each parameter based on the historical gradients, which helps to deal with sparse and noisy gradients.
  - AdaDelta: a method that improves AdaGrad by using a moving average of the gradients and the parameter updates, which reduces the aggressive and monotonically decreasing learning rate of AdaGrad.
  - RMSProp: a method that also uses a moving average of the gradients, but with a decay factor that controls the influence of the past gradients, which helps to avoid the diminishing learning rate problem of AdaGrad.
  - Adaptive moment estimation (Adam): a method that combines the ideas of momentum and RMSProp, by using a moving average of both the gradients and the squared gradients, which helps to balance the magnitude and direction of the parameter updates.