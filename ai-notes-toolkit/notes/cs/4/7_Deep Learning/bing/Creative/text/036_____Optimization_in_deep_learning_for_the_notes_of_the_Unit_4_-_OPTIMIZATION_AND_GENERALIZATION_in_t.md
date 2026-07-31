### Optimization in deep learning

- Optimization is the process of finding the optimal values of the parameters (weights and biases) of a deep neural network that minimize a loss function.
- Optimization methods are algorithms that update the parameters iteratively based on the gradients of the loss function with respect to the parameters.
- Optimization methods can be classified into two categories: first-order methods and second-order methods.
- First-order methods only use the first-order derivatives (gradients) of the loss function, while second-order methods also use the second-order derivatives (Hessian matrix) or approximations of them.
- First-order methods are more widely used in deep learning because they are faster and more scalable than second-order methods, which require more computation and memory.
- Some of the most common first-order optimization methods in deep learning are:

  - Gradient descent: The simplest and most basic optimization method, which updates the parameters in the opposite direction of the gradients with a fixed learning rate.
  - Momentum: A method that adds a momentum term to the gradient descent update, which accelerates the convergence and reduces the oscillations.
  - Nesterov accelerated gradient (NAG): A method that improves the momentum method by using a lookahead gradient, which anticipates the future position of the parameters and corrects the momentum accordingly.
  - Adaptive gradient (AdaGrad): A method that adapts the learning rate for each parameter based on the historical gradients, which reduces the learning rate for parameters with large gradients and increases it for parameters with small gradients.
  - AdaDelta: A method that improves AdaGrad by using a moving average of the gradients instead of the sum of the squared gradients, which prevents the learning rate from decaying too fast.
  - RMSProp: A method that improves AdaDelta by using an exponential decay factor for the moving average of the gradients, which gives more weight to the recent gradients and less weight to the old gradients.
  - Adaptive moment estimation (Adam): A method that combines the ideas of momentum and RMSProp, which uses a moving average of both the gradients and the squared gradients to update the parameters with adaptive learning rates.

- Optimization methods can also be influenced by other factors, such as:

  - Batch size: The number of samples used to compute the gradients in each iteration, which affects the speed and stability of the optimization process.
  - Learning rate schedule: The strategy of changing the learning rate during the optimization process, which can help to avoid local minima and reach the global minimum faster.
  - Regularization: The technique of adding a penalty term to the loss function, which reduces the complexity and overfitting of the model.
  - Initialization: The technique of assigning initial values to the parameters, which affects the convergence and performance of the model.
  - Normalization: The technique of scaling and shifting the inputs or the outputs of the layers, which improves the stability and efficiency of the optimization process.