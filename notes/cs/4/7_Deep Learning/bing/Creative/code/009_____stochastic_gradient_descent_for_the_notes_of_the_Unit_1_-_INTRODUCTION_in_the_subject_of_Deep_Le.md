# Stochastic Gradient Descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable).
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the discrepancy between the predicted and true labels of the data .
- SGD works by updating the parameters of the model (e.g. weights and biases) in the opposite direction of the gradient of the objective function with respect to the parameters, using a small subset of the data (called a mini-batch) at each iteration.
- The advantages of SGD are that it is computationally efficient, can handle large and streaming data, and can escape from local minima.
- The disadvantages of SGD are that it is sensitive to the learning rate, the mini-batch size, and the initialization of the parameters, and that it can have high variance and oscillations.
- SGD can be improved by using various techniques, such as momentum, adaptive learning rates, regularization, and early stopping.