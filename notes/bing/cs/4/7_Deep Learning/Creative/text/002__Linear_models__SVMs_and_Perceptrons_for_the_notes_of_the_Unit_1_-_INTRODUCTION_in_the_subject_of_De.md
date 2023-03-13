### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input data.
- Linear models can be used for both regression and classification tasks, depending on the output variable.
- Linear models are simple, interpretable, and computationally efficient, but they may not capture the complexity and non-linearity of some real-world problems.
- Some examples of linear models are:

  - **Support Vector Machines (SVMs)**: SVMs are linear classifiers that find the optimal hyperplane that separates the data into two or more classes. SVMs can also use kernels to map the data into a higher-dimensional space where a linear separation is possible. SVMs are robust to outliers and can handle high-dimensional data, but they may suffer from overfitting if the kernel is not chosen carefully.
  - **Perceptrons**: Perceptrons are the simplest form of neural networks, consisting of a single layer of artificial neurons that output a binary value based on a linear combination of the inputs and a threshold. Perceptrons can learn linearly separable patterns, but they cannot learn non-linear or XOR-like patterns. Perceptrons can be extended to multi-layer perceptrons (MLPs) by adding hidden layers and non-linear activation functions.

- Linear models can be trained using various optimization methods, such as gradient descent, stochastic gradient descent, or coordinate descent. The objective function to minimize can be different depending on the task and the model, such as mean squared error, hinge loss, or cross-entropy loss.
- Linear models can be evaluated using various metrics, such as accuracy, precision, recall, F1-score, or mean absolute error. The performance of linear models can also depend on the choice of hyperparameters, such as the learning rate, the regularization term, or the kernel function.