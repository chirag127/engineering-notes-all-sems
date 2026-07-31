# Optimization in deep learning

- Optimization is the process of finding the optimal values of the parameters of a deep neural network that minimize a loss function or maximize a performance metric.
- Optimization methods are algorithms that update the parameters of a deep neural network based on the gradients of the loss function with respect to the parameters.
- Optimization methods can be classified into two categories: first-order methods and second-order methods.
- First-order methods only use the first-order derivatives (gradients) of the loss function to update the parameters. They are simpler and faster than second-order methods, but they may suffer from slow convergence, oscillations, or local minima.
- Second-order methods use the second-order derivatives (Hessian matrix) of the loss function to update the parameters. They are more accurate and robust than first-order methods, but they are more complex and computationally expensive, especially for large-scale problems.
- Some of the most popular optimization methods in deep learning are:

  - Gradient descent: The simplest and most widely used first-order method. It updates the parameters by taking a small step in the opposite direction of the gradient of the loss function at the current parameter values. It can be applied in batch mode (using the whole dataset), mini-batch mode (using a subset of the dataset), or stochastic mode (using a single sample).
  - Momentum: A first-order method that adds a momentum term to the gradient descent update rule. The momentum term is a fraction of the previous parameter update, which helps to accelerate the convergence and overcome local minima or saddle points.
  - Nesterov accelerated gradient (NAG): A first-order method that improves the momentum method by using a lookahead gradient instead of the current gradient. The lookahead gradient is computed at a point that is slightly ahead of the current parameter values, which helps to reduce the overshooting and oscillations of the momentum method.
  - Adaptive gradient (AdaGrad): A first-order method that adapts the learning rate for each parameter based on the historical gradients. It assigns a larger learning rate to the parameters that have smaller gradients and a smaller learning rate to the parameters that have larger gradients. This helps to improve the convergence and robustness of the gradient descent method, especially for sparse data.
  - AdaDelta: A first-order method that improves the AdaGrad method by using a moving average of the historical gradients instead of the sum of the squared gradients. This helps to avoid the problem of the learning rate decaying to zero, which may happen in the AdaGrad method.
  - RMSProp: A first-order method that improves the AdaDelta method by using a moving average of the squared gradients instead of the squared gradients. This helps to reduce the noise and stabilize the learning rate.
  - Adaptive moment estimation (Adam): A first-order method that combines the ideas of momentum and adaptive learning rate. It uses a moving average of the gradients and the squared gradients to update the parameters. It also introduces a bias correction term to account for the initialization of the moving averages at zero. It is one of the most popular and effective optimization methods in deep learning.     

: https://heartbeat.comet.ml/7-optimization-methods-used-in-deep-learning-dd0a57fe6b1
: https://www.e2enetworks.com/blog/optimization-in-deep-learning-learn-with-examples
: https://towardsdatascience.com/optimization-methods-in-deep-learning-790629f184b1
: https://arxiv.org/abs/2302.09566
: https://link.springer.com/article/10.1007/s40305-020-00309-6