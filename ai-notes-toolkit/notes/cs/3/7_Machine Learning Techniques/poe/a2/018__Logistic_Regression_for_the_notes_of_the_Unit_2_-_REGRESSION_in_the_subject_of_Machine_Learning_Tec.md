 Here is the formal content in markdown format without any emojis or external links for the topic Logistic Regression for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques:

### Logistic Regression

1. Logistic Regression is a supervised classification algorithm. It is used to predict a binary outcome (1 / 0, yes / no, true / false) given a set of independent variables.
2. In Logistic Regression, the dependent variable (target) is a binary variable that contains only two possible categories. The goal is to use an algorithm to predict the binary target variable based on the values of the independent variables.
3. The algorithm involves developing a better-fit logistic regression model based on the training dataset and using it to predict the outcome for new data.
4. The logistic regression model is:
$$h(x) = \frac{1}{1 + e^{-(w^Tx+b)}}$$
Where
- $h(x)$ is the hypothesis function
- $w$ is the weight vector
- $x$ is the input vector
- $b$ is the bias

5. The probability that the outcome is 1 is given by $h(x)$. Hence, to get the final class, we threshold $h(x)$ at 0.5, i.e. if $h(x) \geq 0.5$, then predict 1 (True), else predict 0 (False).
6. The weights ($w$) and bias ($b$) are estimated using Maximum Likelihood Estimation. The model performance can be evaluated using confusion matrix, accuracy, precision, recall, F1 score, etc.