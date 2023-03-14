### Linear models (SVMs and Perceptrons) for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input features to perform classification or regression tasks.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex patterns or non-linear relationships in the data.
- Support Vector Machines (SVMs) and Perceptrons are two examples of linear models for binary classification tasks.

#### Support Vector Machines (SVMs)

- SVMs are a type of linear model that try to find the optimal hyperplane that maximizes the margin between the two classes in the feature space.
- The margin is the distance between the hyperplane and the closest points from each class, called the support vectors.
- SVMs can handle linearly separable and non-linearly separable data by using different kernels, such as linear, polynomial, radial basis function (RBF), or sigmoid.
- SVMs are robust, accurate, and can handle high-dimensional data, but they may be sensitive to outliers, noise, or overfitting, and they may require tuning of hyperparameters, such as the regularization parameter C and the kernel parameters.

#### Perceptrons

- Perceptrons are a type of linear model that try to find a hyperplane that separates the two classes by minimizing the number of misclassified points.
- Perceptrons update the weights of the linear function based on the sign of the prediction error for each point, using a learning rate parameter.
- Perceptrons can only handle linearly separable data, and they are guaranteed to converge to a solution if the data is linearly separable.
- Perceptrons are simple, easy to implement, and can be used as building blocks for more complex neural networks, but they may not converge or may oscillate if the data is not linearly separable, and they may be sensitive to the order of the data points and the learning rate parameter.

#### Comparison

- Both SVMs and Perceptrons are linear models that try to find a hyperplane that separates the two classes, but they use different criteria and methods to do so.
- SVMs try to maximize the margin between the classes, while Perceptrons try to minimize the number of misclassified points.
- SVMs use quadratic programming or gradient descent to find the optimal solution, while Perceptrons use a simple update rule based on the sign of the error.
- SVMs can handle non-linearly separable data by using kernels, while Perceptrons can only handle linearly separable data.
- SVMs are more accurate and robust than Perceptrons, but they may require more computation and tuning than Perceptrons.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the difference between SVMs and Perceptrons is: **S**VMs find the **S**afest hyperplane, while **P**erceptrons find the **P**ractical hyperplane.
- A possible learning trick to understand the concept of margin in SVMs is to imagine that the hyperplane is a road and the support vectors are the cars on the road. The margin is the width of the road, and the goal is to make the road as wide as possible without hitting any cars.
- A possible learning trick to understand the concept of kernel in SVMs is to imagine that the kernel is a function that transforms the data into a different space, where the classes are more easily separable. For example, the RBF kernel can transform the data into a space where the classes are separated by concentric circles.