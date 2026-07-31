### Stochastic Gradient Descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable) .
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the error between the predicted and true outputs  .
- SGD works by updating the parameters (e.g. weights and biases) of the model in the opposite direction of the gradient of the objective function with respect to the parameters, using a small learning rate .
- SGD differs from batch gradient descent in that it uses only one or a few training examples at a time to compute the gradient, instead of using the whole training set . This makes SGD faster and more memory-efficient, but also more noisy and less stable .
- SGD can be improved by using various techniques, such as momentum, learning rate decay, mini-batches, regularization, and adaptive learning rates  . These techniques can help SGD converge faster, avoid local minima, reduce overfitting, and adapt to the complexity of the data  .