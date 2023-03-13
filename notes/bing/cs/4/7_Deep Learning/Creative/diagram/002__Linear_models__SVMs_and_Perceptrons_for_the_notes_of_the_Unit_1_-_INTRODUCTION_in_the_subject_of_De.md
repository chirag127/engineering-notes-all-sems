Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input data. They are often used for classification or regression problems. Some examples of linear models are support vector machines (SVMs) and perceptrons.

SVMs are linear models that try to find the optimal hyperplane that maximizes the margin between the classes. They can also use kernels to map the input data to a higher-dimensional space where they are linearly separable. SVMs can handle both binary and multiclass classification problems.

Perceptrons are linear models that try to find any hyperplane that separates the classes. They use a simple update rule to adjust the weights based on the prediction errors. Perceptrons can only handle binary classification problems, and they may not converge if the data are not linearly separable.

The following diagram illustrates the basic architecture of a linear model:

```
    Input layer            Output layer
    x1 x2 ... xn           y
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    |  |   |   |           |
    w1 w2 ... wn           b
    \  /   /   /           /
     \/   /   /           /
      \  /   /           /
       \/   /           /
        \  /           /
         \/           /
          \          /
           \        /
            \      /
             \    /
              \  /
               \/
               z
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               f(z)
```

The input layer consists of n features x1, x2, ..., xn. The output layer consists of a single node y, which represents the predicted class or value. The linear model computes a weighted sum of the input features, plus a bias term b, to obtain z:

z = w1 * x1 + w2 * x2 + ... + wn * xn + b

The linear model then applies a function f to z to obtain the output y:

y = f(z)

The function f depends on the type of problem and the linear model. For example, for binary classification, f could be a sigmoid function that outputs a probability between 0 and 1. For multiclass classification, f could be a softmax function that outputs a probability distribution over the classes. For regression, f could be an identity function that outputs z itself.

The linear model learns the weights w1, w2, ..., wn and the bias b from the training data, by minimizing a loss function that measures the discrepancy between the predicted output y and the true output y'. The loss function also depends on the type of problem and the linear model. For example, for binary classification, the loss function could be the cross-entropy loss. For multiclass classification, the loss function could be the hinge loss. For regression, the loss function could be the mean squared error.