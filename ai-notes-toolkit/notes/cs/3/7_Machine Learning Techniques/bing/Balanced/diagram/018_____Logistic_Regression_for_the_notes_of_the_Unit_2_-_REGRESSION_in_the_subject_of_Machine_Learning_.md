### Logistic Regression for Machine Learning

- Logistic regression is a supervised learning algorithm for classification problems  .
- It is used to predict the probability of a binary (yes/no) outcome based on one or more input variables (features)   .
- It is based on the logistic function, also known as the sigmoid function, which maps any real value to a value between 0 and 1  .
- The logistic function is defined as:

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

- The logistic regression model is represented by a linear equation that combines the input variables with the coefficients (weights) to predict the log-odds of the outcome  .
- The log-odds is the logarithm of the odds ratio, which is the ratio of the probability of the positive class to the probability of the negative class  .
- The logistic regression equation is:

$$
\log \frac{p}{1-p} = b_0 + b_1 x_1 + b_2 x_2 + ... + b_n x_n
$$

- Where $p$ is the probability of the positive class, $b_0$ is the intercept, $b_1, b_2, ..., b_n$ are the coefficients, and $x_1, x_2, ..., x_n$ are the input variables  .
- To convert the log-odds to the probability, we apply the inverse of the logistic function, which is:

$$
p = \frac{e^{\log \frac{p}{1-p}}}{1 + e^{\log \frac{p}{1-p}}} = \frac{1}{1 + e^{-(b_0 + b_1 x_1 + b_2 x_2 + ... + b_n x_n)}}
$$

- The goal of logistic regression is to find the optimal values of the coefficients that maximize the likelihood of correctly predicting the outcome for the given data  .
- The likelihood is the product of the probabilities of the observed outcomes, and it can be written as:

$$
L(b_0, b_1, ..., b_n) = \prod_{i=1}^m p_i^{y_i} (1 - p_i)^{1 - y_i}
$$

- Where $m$ is the number of observations, $p_i$ is the predicted probability for the $i$-th observation, and $y_i$ is the actual outcome for the $i$-th observation  .
- To maximize the likelihood, we can use a technique called gradient ascent, which iteratively updates the coefficients by moving in the direction of the steepest increase of the likelihood function  .
- Alternatively, we can minimize the negative log-likelihood, which is equivalent to maximizing the likelihood, but easier to work with mathematically  .
- The negative log-likelihood is:

$$
NLL(b_0, b_1, ..., b_n) = -\sum_{i=1}^m y_i \log p_i + (1 - y_i) \log (1 - p_i)
$$

- To minimize the negative log-likelihood, we can use a technique called gradient descent, which iteratively updates the coefficients by moving in the direction of the steepest decrease of the negative log-likelihood function  .
- The gradient descent update rule is:

$$
b_j := b_j - \alpha \frac{\partial NLL}{\partial b_j}
$$

- Where $b_j$ is the $j$-th coefficient, $\alpha$ is the learning rate, and $\frac{\partial NLL}{\partial b_j}$ is the partial derivative of the negative log-likelihood with respect to the $j$-th coefficient  .
- The partial derivative of the negative log-likelihood with respect to the $j