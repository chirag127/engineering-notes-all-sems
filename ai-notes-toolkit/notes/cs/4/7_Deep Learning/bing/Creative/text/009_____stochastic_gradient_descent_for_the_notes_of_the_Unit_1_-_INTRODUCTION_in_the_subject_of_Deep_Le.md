### Stochastic Gradient Descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable).
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the discrepancy between the predicted and true labels of the data .
- SGD works by updating the parameters of the model (e.g. weights and biases) in the opposite direction of the gradient of the objective function with respect to the parameters, using a small subset of the data (e.g. one or a few examples) at each iteration .
- The advantages of SGD are that it is computationally efficient, can handle large and streaming data, and can escape from local minima due to the noise introduced by the random sampling of the data .
- The disadvantages of SGD are that it is sensitive to the learning rate (the step size of the parameter update), the initialization of the parameters, and the choice of the subset size (also called the batch size) .
- SGD can be improved by using various techniques, such as momentum, adaptive learning rates, mini-batch sampling, regularization, and early stopping .