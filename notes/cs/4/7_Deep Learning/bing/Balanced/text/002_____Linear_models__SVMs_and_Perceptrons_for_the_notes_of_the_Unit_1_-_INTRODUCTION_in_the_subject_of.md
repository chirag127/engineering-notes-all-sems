### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features.
- Linear models can be used for both regression and classification tasks, depending on the loss function and the output activation function.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex non-linear patterns in the data.
- Support Vector Machines (SVMs) and Perceptrons are two popular types of linear models for classification.

#### Support Vector Machines (SVMs)

- SVMs are linear classifiers that find the optimal hyperplane that maximizes the margin between the classes.
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors.
- SVMs can handle non-linearly separable data by using kernel functions that map the input features to a higher-dimensional space where a linear hyperplane can be found.
- SVMs are robust, accurate, and can handle high-dimensional data, but they may be sensitive to outliers and noise, and require tuning of the hyperparameters.

#### Perceptrons

- Perceptrons are linear classifiers that learn the weights and bias of a linear function by minimizing the number of misclassified examples.
- Perceptrons update the weights and bias using a learning rate and a gradient descent algorithm, based on the error between the predicted and the true labels.
- Perceptrons are guaranteed to converge to a solution if the data is linearly separable, but they may not converge or find the optimal solution otherwise.
- Perceptrons are simple, fast, and online, but they may be unstable, sensitive to the learning rate, and unable to handle non-linearly separable data.