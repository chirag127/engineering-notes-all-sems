### Linear models (SVMs and Perceptrons)

- Linear models are classifiers that use a linear function to separate the input space into two or more regions corresponding to different classes.
- Linear models can be represented by a weight vector **w** and a bias term **b**, such that the decision function is given by **f(x) = w^T x + b**.
- Linear models are simple, fast, and interpretable, but they may not be able to capture complex nonlinear patterns in the data.
- Two common types of linear models are support vector machines (SVMs) and perceptrons.

#### Support vector machines (SVMs)

- SVMs are linear models that aim to find the optimal hyperplane that maximizes the margin between two classes.
- The margin is the distance between the hyperplane and the closest points from each class, called support vectors.
- SVMs can handle linearly separable and non-separable data by using slack variables and kernel functions, respectively.
- Slack variables allow some points to violate the margin constraint, while kernel functions map the input data to a higher-dimensional feature space where a linear separation is possible.
- SVMs are associated with a convex optimization problem that guarantees a globally optimal solution.

#### Perceptrons

- Perceptrons are linear models that learn the weight vector and the bias term by iteratively updating them based on the prediction errors on the training data.
- Perceptrons use a threshold function to convert the linear output to a binary output, such as **sign(f(x))** or **step(f(x))**.
- Perceptrons can only handle linearly separable data, and they are not guaranteed to converge if the data is not separable.
- Perceptrons can be trained online, meaning that their weights can be updated as new examples arrive one at a time.
- Perceptrons may find any of the infinitely many hyperplanes that separate the data, and they are not optimal in terms of margin.