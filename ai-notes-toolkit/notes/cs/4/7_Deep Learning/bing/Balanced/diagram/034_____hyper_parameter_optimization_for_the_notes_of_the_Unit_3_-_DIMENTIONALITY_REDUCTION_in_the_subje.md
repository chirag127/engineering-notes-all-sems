### Hyperparameter optimization

- Hyperparameter optimization is the problem of choosing a set of optimal hyperparameters for a deep learning model.
- Hyperparameters are parameters whose values are used to control the learning process, such as learning rate, number of hidden layers, number of neurons, activation functions, etc.
- Hyperparameter optimization aims to find the best combination of hyperparameters that minimizes a predefined loss function or maximizes a predefined performance metric on a validation set or a test set.
- Hyperparameter optimization can improve the generalization ability and the robustness of deep learning models, as well as reduce the training time and the computational cost.
- Hyperparameter optimization can be divided into two categories: black-box optimization and white-box optimization.
  - Black-box optimization treats the deep learning model as a black box and does not use any information about its internal structure or gradient information. It only evaluates the model output based on the input hyperparameters and the loss function or the performance metric. Examples of black-box optimization algorithms are grid search, random search, evolutionary algorithms, Bayesian optimization, etc.
  - White-box optimization exploits the information about the deep learning model structure or gradient information to guide the search for optimal hyperparameters. Examples of white-box optimization algorithms are gradient-based methods, such as gradient descent, stochastic gradient descent, Adam, etc.