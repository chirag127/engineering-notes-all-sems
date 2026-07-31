### Linear models (SVMs and Perceptrons)

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features.
- Linear models can be used for both regression and classification tasks, depending on the loss function and the output activation function.
- Linear models are simple, fast, and interpretable, but they have limited expressive power and cannot capture complex non-linear patterns in the data.
- Support vector machines (SVMs) and perceptrons are two popular types of linear models for classification.

#### Support vector machines (SVMs)

- SVMs are linear classifiers that find the optimal hyperplane that maximizes the margin between the classes.
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors.
- SVMs can handle non-linearly separable data by using kernel functions that map the input features to a higher-dimensional feature space where a linear hyperplane can be found.
- SVMs are robust, accurate, and can handle high-dimensional data, but they are sensitive to the choice of kernel and hyperparameters, and can be computationally expensive for large datasets.

#### Perceptrons

- Perceptrons are linear classifiers that learn the weights of the input features by updating them based on the prediction errors.
- Perceptrons use a step function as the output activation function, which outputs 1 if the linear combination of the input features is positive, and 0 otherwise.
- Perceptrons can converge to a solution if the data is linearly separable, but they are sensitive to noise and outliers, and can oscillate indefinitely if the data is not linearly separable.
- Perceptrons are the simplest form of artificial neural networks, which are composed of multiple layers of perceptrons or other non-linear units that can learn complex non-linear functions from the data.