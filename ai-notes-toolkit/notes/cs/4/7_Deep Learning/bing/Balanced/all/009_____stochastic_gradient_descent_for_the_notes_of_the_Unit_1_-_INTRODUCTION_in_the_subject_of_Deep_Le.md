# Stochastic Gradient Descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable) .
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the discrepancy between the predicted and true labels   .
- SGD works by updating the parameters (e.g. weights and biases) of the model in the opposite direction of the gradient of the objective function with respect to the parameters . The gradient is computed using a single or a small batch of training examples, which makes SGD faster and more scalable than batch gradient descent, which uses the entire training set  .
- SGD has several advantages, such as:
  - It can escape from local minima or saddle points, since the noise introduced by the random selection of examples can help the algorithm explore different regions of the parameter space  .
  - It can handle large and streaming data sets, since it does not need to store or process the entire data at once  .
  - It can adapt to changing data distributions, since it can update the parameters online as new data arrives  .
- SGD also has some drawbacks, such as:
  - It can be sensitive to the choice of learning rate, which controls the step size of the parameter updates. A too large learning rate can cause the algorithm to diverge or oscillate, while a too small learning rate can slow down the convergence or get stuck in suboptimal solutions   .
  - It can be affected by noisy gradients, which can introduce variance and instability in the parameter updates. This can be mitigated by using techniques such as momentum, adaptive learning rates, or gradient clipping   .
  - It can be biased by the order or the sampling of the training examples, which can affect the quality and the speed of the convergence. This can be alleviated by using techniques such as shuffling, stratification, or mini-batch sampling   .