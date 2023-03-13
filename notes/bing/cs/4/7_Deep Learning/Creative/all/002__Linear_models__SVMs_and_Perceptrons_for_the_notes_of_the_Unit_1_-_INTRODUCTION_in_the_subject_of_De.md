### Linear models (SVMs and Perceptrons) for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Linear models are a class of machine learning algorithms that can learn to classify data into labels based on a linear combination of input features.
- Linear models can be used for binary or multiclass classification tasks, depending on the number of output units and the activation function used.
- Linear models are simple, fast, and interpretable, but they have limitations in modeling complex and nonlinear patterns in the data.
- Two common examples of linear models are Support Vector Machines (SVMs) and Perceptrons.

#### Support Vector Machines (SVMs)

- SVMs are a type of linear model that can find the optimal hyperplane that separates the data into two classes with the maximum margin.
- SVMs can also use kernel functions to map the data into a higher-dimensional space where they become linearly separable.
- SVMs are robust, accurate, and can handle high-dimensional data, but they can be sensitive to outliers and noise, and require careful tuning of the hyperparameters.
- SVMs can be formulated as a convex optimization problem that can be solved efficiently using quadratic programming or stochastic gradient descent.

#### Perceptrons

- Perceptrons are a type of linear model that can learn to classify data into two classes by updating the weights and bias based on the prediction errors.
- Perceptrons are also the simplest form of artificial neural networks, with a single layer of input and output units connected by weighted edges.
- Perceptrons are easy to implement and understand, but they can only learn linearly separable patterns, and they may not converge if the data is not linearly separable.
- Perceptrons can be extended to multilayer perceptrons (MLPs) by adding one or more hidden layers of nonlinear units, which can learn more complex and nonlinear patterns in the data.