# Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features to perform classification or regression tasks.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex nonlinear patterns in the data.
- Support vector machines (SVMs) and perceptrons are two examples of linear models that are widely used in deep learning.

## Support vector machines (SVMs)

- SVMs are a type of linear classifier that find the optimal hyperplane that maximizes the margin between the two classes in the training data.
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors.
- SVMs can handle linearly separable and non-separable data by using different kernels, such as linear, polynomial, radial basis function (RBF), or sigmoid, that transform the input space into a higher-dimensional feature space where the data becomes more separable.
- SVMs are robust to outliers, have good generalization performance, and can handle high-dimensional data, but they may suffer from overfitting, scalability, and interpretability issues.

## Perceptrons

- Perceptrons are a type of linear classifier that learn a set of weights and a bias term that define a linear function or decision boundary that separates the two classes in the training data.
- Perceptrons update the weights and bias using a simple learning rule that minimizes the classification error on the training data.
- Perceptrons can only handle linearly separable data, and they may not converge if the data is not separable.
- Perceptrons are the simplest form of artificial neural networks, and they can be extended to multilayer perceptrons (MLPs) that can learn nonlinear functions and decision boundaries by adding hidden layers and activation functions.