# Unit 1 - INTRODUCTION

### Stochastic Gradient Descent

- Stochastic Gradient Descent (SGD) is an optimization algorithm used to minimize an objective function.
- It is commonly used in machine learning and deep learning to update the parameters of a model.
- SGD is an iterative method that updates the parameters in small steps in the direction of the negative gradient of the objective function.
- The objective function is typically a loss function that measures the difference between the predicted and true values.
- The gradient of the objective function with respect to the parameters is calculated using a single training example or a small batch of training examples.
- The parameters are then updated by subtracting the gradient multiplied by a learning rate.
- The learning rate is a hyperparameter that controls the step size of the updates.
- SGD introduces randomness in the optimization process, which can help the algorithm escape local minima and find better solutions.
- However, the randomness can also cause the algorithm to fluctuate around the optimal solution and slow down the convergence.
- To mitigate this issue, the learning rate is often decreased over time according to a schedule.
- Variants of SGD, such as momentum, Nesterov accelerated gradient, and Adam, incorporate additional techniques to speed up convergence and improve the final solution.