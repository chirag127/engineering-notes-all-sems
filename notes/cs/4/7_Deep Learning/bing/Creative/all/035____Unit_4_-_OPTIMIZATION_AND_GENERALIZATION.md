## Unit 4 - OPTIMIZATION AND GENERALIZATION

- Optimization is the process of finding the best parameters for a machine learning model that minimize the loss function on the training data.
- Generalization is the ability of a machine learning model to perform well on new and unseen data that is not part of the training data.
- Optimization and generalization are related but not the same. A model that is well-optimized may not generalize well, and a model that generalizes well may not be well-optimized.
- There are various methods and techniques to optimize and generalize machine learning models, such as gradient descent, regularization, cross-validation, and early stopping.
- Gradient descent is an iterative algorithm that updates the model parameters by moving in the direction of the negative gradient of the loss function with respect to the parameters. The size of the update is determined by the learning rate, which is a hyperparameter that controls how fast the model learns.
- Regularization is a technique that adds a penalty term to the loss function to reduce the complexity of the model and prevent overfitting. There are different types of regularization, such as L1, L2, and dropout.
- Cross-validation is a technique that splits the training data into k folds, and uses one fold as the validation set and the rest as the training set. The model is trained and evaluated on each fold, and the average performance is reported. Cross-validation helps to estimate the generalization error and select the best hyperparameters for the model.
- Early stopping is a technique that stops the training process when the validation error stops decreasing or starts increasing. Early stopping helps to avoid overfitting and save computational resources.