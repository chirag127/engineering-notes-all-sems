### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features.
- Linear models can be used for both regression and classification tasks, depending on the loss function and the output activation function.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex non-linear patterns in the data.
- Support Vector Machines (SVMs) and Perceptrons are two popular types of linear models for classification.

#### Support Vector Machines (SVMs)

- SVMs are linear classifiers that find the optimal hyperplane that maximizes the margin between the classes.
- The margin is the distance between the hyperplane and the closest points from each class, called the support vectors.
- SVMs can handle non-linearly separable data by using kernel functions that map the input features to a higher-dimensional space where they become linearly separable.
- SVMs are robust, accurate, and can handle high-dimensional data, but they may be sensitive to outliers and noise, and require tuning of hyperparameters such as the regularization parameter and the kernel function.

#### Perceptrons

- Perceptrons are linear classifiers that learn the weights of the input features by minimizing the classification error on the training data.
- Perceptrons update the weights iteratively using a learning rate and a gradient descent algorithm, such as stochastic gradient descent (SGD).
- Perceptrons are equivalent to a single-layer neural network with a binary output activation function, such as a step function or a sigmoid function.
- Perceptrons are simple, fast, and can learn online, but they may not converge if the data is not linearly separable, and they may be sensitive to the order of the training examples and the learning rate.