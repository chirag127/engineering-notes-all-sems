### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features.
- Linear models can be used for both regression and classification tasks, depending on the loss function and the output activation function used.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex non-linear patterns in the data.
- Support vector machines (SVMs) and perceptrons are two examples of linear models for classification.

#### Support vector machines (SVMs)

- SVMs are linear classifiers that find the optimal hyperplane that maximizes the margin between the classes.
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors.
- SVMs can handle non-linearly separable data by using kernel functions that map the input features to a higher-dimensional feature space where a linear hyperplane can be found.
- SVMs are robust, accurate, and can handle high-dimensional data, but they may be sensitive to outliers and noise, and require careful selection of the kernel and regularization parameters.

#### Perceptrons

- Perceptrons are linear classifiers that learn the weights of the input features by minimizing the classification error on the training data.
- Perceptrons update the weights iteratively using a learning rate and a gradient descent algorithm, such as stochastic gradient descent (SGD).
- Perceptrons are equivalent to a single-layer neural network with a binary output activation function, such as a step function or a sigmoid function.
- Perceptrons can only converge to a solution if the data is linearly separable, otherwise they may oscillate or diverge. Perceptrons can be extended to multi-layer perceptrons (MLPs) by adding hidden layers and non-linear activation functions, which can learn more complex functions and approximate any continuous function.