### Logistic Regression

- Logistic regression is a type of supervised learning algorithm that can be used for binary classification problems, where the output is either 0 or 1.
- Logistic regression models the probability of the output being 1 given the input features, using a sigmoid function that maps any real value to a value between 0 and 1.
- The sigmoid function is defined as:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

- where z is a linear combination of the input features and the model parameters, such as:

$$z = w_0 + w_1 x_1 + w_2 x_2 + ... + w_n x_n$$

- The model parameters can be learned by minimizing a loss function that measures the discrepancy between the predicted probabilities and the actual labels, such as the cross-entropy loss:

$$L(y, \hat{y}) = - y \log(\hat{y}) - (1 - y) \log(1 - \hat{y})$$

- where y is the actual label (0 or 1) and $\hat{y}$ is the predicted probability (between 0 and 1).
- The cross-entropy loss can be minimized using gradient descent, which updates the model parameters iteratively by moving in the opposite direction of the gradient of the loss function with respect to the parameters.
- Logistic regression can be extended to multi-class classification problems by using the softmax function instead of the sigmoid function, which can output a probability distribution over K classes, such that the sum of the probabilities is 1.
- The softmax function is defined as:

$$\text{softmax}(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$

- where z is a vector of K values, one for each class, and $\text{softmax}(z)_i$ is the probability of the output being class i.
- The cross-entropy loss can be generalized to multi-class problems by using the following formula:

$$L(y, \hat{y}) = - \sum_{i=1}^K y_i \log(\hat{y}_i)$$

- where y is a one-hot encoded vector of K values, such that only one element is 1 and the rest are 0, and $\hat{y}$ is the predicted probability vector.
- Logistic regression is a simple but powerful algorithm that can be used as a baseline for binary and multi-class classification problems. It can also be seen as a special case of a neural network with no hidden layers and a sigmoid or softmax activation function at the output layer.