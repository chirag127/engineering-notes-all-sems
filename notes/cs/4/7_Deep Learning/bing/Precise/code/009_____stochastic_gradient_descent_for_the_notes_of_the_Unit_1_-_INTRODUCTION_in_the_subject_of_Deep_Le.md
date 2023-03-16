### Stochastic Gradient Descent

Stochastic Gradient Descent (SGD) is an optimization algorithm used to minimize an objective function by iteratively updating the parameters of the model. It is commonly used in training deep learning models.

Here are some key points to remember about SGD:

1. SGD is an iterative method that updates the parameters of the model in the direction of the negative gradient of the objective function with respect to the parameters.
2. The objective function is typically a loss function that measures the discrepancy between the predicted and true values.
3. The update is performed one training example at a time, or in small batches, which is why it is called "stochastic".
4. The learning rate is a hyperparameter that controls the step size of the update. It is important to choose an appropriate learning rate to ensure convergence.
5. SGD can be sensitive to the scaling of the input features, so it is common to normalize the data before training.
6. SGD can escape local minima, but it may also oscillate around the global minimum due to its stochastic nature.
7. Variants of SGD, such as momentum, Nesterov accelerated gradient, and Adam, have been proposed to improve convergence.
