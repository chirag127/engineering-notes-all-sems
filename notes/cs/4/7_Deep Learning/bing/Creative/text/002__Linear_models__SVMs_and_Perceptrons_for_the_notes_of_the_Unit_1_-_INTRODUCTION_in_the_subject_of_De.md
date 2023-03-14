### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input data.
- Linear models can be used for both regression and classification tasks, depending on the output type (continuous or discrete) and the loss function (squared error, hinge loss, etc.).
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex nonlinear patterns or interactions in the data.
- Some examples of linear models are:

  - **Support Vector Machines (SVMs)**: SVMs are linear classifiers that find the optimal hyperplane that separates the data into two classes with the maximum margin. SVMs can also use kernel functions to map the data into a higher-dimensional space where they become linearly separable.
  - **Perceptrons**: Perceptrons are linear classifiers that update their weights based on the prediction errors of the training examples. Perceptrons can learn linearly separable functions, but they may not converge if the data is not linearly separable.
  - **Linear Regression**: Linear regression is a linear model that predicts a continuous output variable based on a linear combination of the input features. Linear regression can use different methods to estimate the model parameters, such as ordinary least squares, ridge regression, or lasso regression.
  - **Logistic Regression**: Logistic regression is a linear model that predicts a binary output variable based on a linear combination of the input features, followed by a sigmoid function. Logistic regression can use different methods to estimate the model parameters, such as maximum likelihood, gradient descent, or Newton's method.