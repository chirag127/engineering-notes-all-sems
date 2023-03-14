
### Stochastic Gradient Descent for the Notes of the Unit 1 - INTRODUCTION in the Subject of Deep Learning

Stochastic Gradient Descent (SGD) is an essential algorithm for Deep Learning. It is a method for optimizing an objective function by iteratively updating the model parameters with small steps in the direction of the negative gradient of the objective function. This is done in a stochastic manner, which means that the gradient is estimated using a randomly chosen subset of the training data.

SGD is used to optimize a variety of objectives, such as minimizing the squared error, minimizing the negative log-likelihood of a model, and minimizing the hinge loss of a model. SGD has several advantages, such as being computationally efficient, being able to handle large datasets, and being able to optimize non-convex objectives.

SGD can be used to optimize a variety of objectives, including linear and logistic regression, neural networks, and support vector machines. SGD is also used in unsupervised learning, such as clustering and dimensionality reduction.

SGD is an iterative algorithm, meaning that it updates the model parameters with small steps in the direction of the negative gradient of the objective function. The step size is usually determined using a line search algorithm that finds the step size that minimizes the objective function.

Mnemonics and learning tricks for SGD include:

* **S**tep size: Choose a step size that minimizes the objective function.
* **G**radient: Estimate the gradient using a randomly chosen subset of the training data.
* **D**irection: Update the model parameters in the direction of the negative gradient.