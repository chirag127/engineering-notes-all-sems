### Stochastic Gradient Descent

Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable). It is often used for machine learning, especially for fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression.

The main idea of SGD is to update the parameters of the model (e.g. weights and biases) by taking small steps in the opposite direction of the gradient of the objective function with respect to the parameters. The gradient is computed using a single or a small batch of randomly selected training examples, instead of the whole training set. This makes SGD faster and more scalable than batch gradient descent, which uses the entire training set to compute the gradient at each iteration.

The steps of SGD are as follows:

1. Initialize the parameters randomly or with some heuristic.
2. Repeat until convergence or a maximum number of iterations is reached:
    - Pick a random training example or a small batch of training examples.
    - Compute the gradient of the objective function with respect to the parameters using the selected example(s).
    - Update the parameters by subtracting a fraction of the gradient, called the learning rate.
3. Return the final parameters.

SGD has some advantages and disadvantages over batch gradient descent:

- Advantages:
    - It can handle large and streaming data sets, as it only requires a small amount of memory and computation per iteration.
    - It can escape from local minima and saddle points, as it introduces noise and randomness in the optimization process.
    - It can be easily parallelized and distributed across multiple machines or devices.
- Disadvantages:
    - It can be noisy and unstable, as it depends on the quality and order of the selected examples.
    - It can oscillate around the optimal solution, as it may overshoot or undershoot the gradient direction.
    - It requires careful tuning of the learning rate and other hyperparameters, such as the batch size and the momentum term.

SGD can be modified and improved by using different variants and extensions, such as:

- Mini-batch SGD: It uses a small batch of examples (e.g. 32 or 64) instead of a single example to compute the gradient, which can reduce the variance and noise of SGD and improve the convergence speed and accuracy.
- Momentum SGD: It adds a fraction of the previous parameter update to the current update, which can accelerate the convergence and dampen the oscillations of SGD.
- Nesterov accelerated gradient (NAG): It uses a lookahead gradient, which is computed at the predicted next position of the parameters, instead of the current position, which can improve the accuracy and stability of SGD.
- Adagrad: It adapts the learning rate for each parameter based on the historical gradients, which can handle sparse and non-stationary data and reduce the need for manual tuning of the learning rate.
- RMSprop: It uses an exponentially weighted moving average of the squared gradients to adjust the learning rate, which can prevent the learning rate from decaying too quickly or too slowly.
- Adam: It combines the ideas of momentum and RMSprop, and uses biased estimates of the first and second moments of the gradients to update the parameters, which can achieve fast and stable convergence.