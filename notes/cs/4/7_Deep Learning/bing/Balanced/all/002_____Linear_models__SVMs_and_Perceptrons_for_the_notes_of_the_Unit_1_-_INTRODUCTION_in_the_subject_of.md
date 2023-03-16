# Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features.
- Linear models can be used for both regression and classification tasks, depending on the loss function and the output activation function.
- Linear models are simple, fast, and interpretable, but they have limited expressive power and cannot capture complex non-linear patterns in the data.
- Some examples of linear models are linear regression, logistic regression, support vector machines (SVMs), and perceptrons.

## Support vector machines (SVMs)

- SVMs are a type of linear model that aim to find the optimal hyperplane that maximizes the margin between the classes.
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors.
- SVMs can handle linearly separable and non-separable data by using different kernels, such as linear, polynomial, radial basis function (RBF), or sigmoid.
- SVMs are robust, accurate, and can handle high-dimensional data, but they are sensitive to outliers, require tuning of hyperparameters, and can be computationally expensive.

## Perceptrons

- Perceptrons are a type of linear model that learn a binary classifier by updating the weights based on the prediction errors.
- Perceptrons use a step function as the output activation function, which outputs 1 if the linear combination of the input features is positive, and 0 otherwise.
- Perceptrons can only converge to a solution if the data is linearly separable, otherwise they will oscillate indefinitely.
- Perceptrons are the simplest form of artificial neural networks, and can be extended to multi-layer perceptrons (MLPs) by adding hidden layers and non-linear activation functions.