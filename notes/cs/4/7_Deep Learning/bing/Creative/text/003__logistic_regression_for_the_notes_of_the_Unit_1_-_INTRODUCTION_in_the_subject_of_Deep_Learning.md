### Logistic Regression

- Logistic regression is a type of supervised learning algorithm that can be used for binary classification problems, where the output is either 0 or 1.
- Logistic regression models the probability of the output being 1 given the input features, using a sigmoid function as the activation function.
- The sigmoid function is defined as:

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

- The sigmoid function maps any real number to a value between 0 and 1, and has the following properties:

  - $\sigma(0) = 0.5$
  - $\sigma(x) \to 1$ as $x \to \infty$
  - $\sigma(x) \to 0$ as $x \to -\infty$
  - $\sigma(-x) = 1 - \sigma(x)$

- The logistic regression model can be written as:

$$\hat{y} = \sigma(w^Tx + b)$$

where $w$ is the weight vector, $x$ is the input feature vector, $b$ is the bias term, and $\hat{y}$ is the predicted output.

- The goal of logistic regression is to find the optimal values of $w$ and $b$ that minimize the loss function, which measures the discrepancy between the predicted output and the actual output.
- One common choice of loss function for logistic regression is the binary cross-entropy loss, which is defined as:

$$L(\hat{y}, y) = -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})]$$

where $y$ is the actual output, which is either 0 or 1.

- The binary cross-entropy loss has the following properties:

  - $L(\hat{y}, y) \to 0$ as $\hat{y} \to y$
  - $L(\hat{y}, y) \to \infty$ as $\hat{y} \to 1 - y$
  - $L(\hat{y}, y) \geq 0$ for any $\hat{y}$ and $y$

- The total loss for a given dataset of $m$ examples is the average of the individual losses:

$$J(w, b) = \frac{1}{m} \sum_{i=1}^m L(\hat{y}^{(i)}, y^{(i)})$$

where $\hat{y}^{(i)}$ and $y^{(i)}$ are the predicted and actual outputs for the $i$-th example, respectively.

- To minimize the total loss, we can use gradient descent, which is an iterative algorithm that updates the parameters $w$ and $b$ in the opposite direction of the gradient of the loss function with respect to the parameters:

$$w := w - \alpha \frac{\partial J}{\partial w}$$
$$b := b - \alpha \frac{\partial J}{\partial b}$$

where $\alpha$ is the learning rate, which controls the size of the update step.

- The gradient of the loss function with respect to the parameters can be derived using the chain rule of calculus:

$$\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)}) x^{(i)}$$
$$\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})$$

- By repeating the gradient descent update until convergence, we can obtain the optimal values of $w$ and $b$ that minimize the loss function and make the best predictions for the given dataset.