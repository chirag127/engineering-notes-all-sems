### Logistic Regression for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Logistic regression is a supervised learning algorithm used to classify data into two or more classes.
- Logistic regression can be used for both binary and multiclass classification.
- Logistic regression uses an equation as the representation, very much like linear regression.
- Input values (x) are combined linearly using weights or coefficient values (referred to as the Greek capital letter Beta) to predict an output value (y).
- A key difference from linear regression is that the output value being modeled is a categorical value (0 or 1) rather than a numeric value.
- Logistic regression uses the logistic function, also called the sigmoid function, to transform the linear combination of inputs into a value between 0 and 1, which can be interpreted as a probability of belonging to a certain class.
- The logistic function is defined as:

  `y = 1 / (1 + e^(-b0 - b1*x))`

  Where y is the predicted output, b0 is the bias or intercept term and b1 is the coefficient for the single input value (x).

- The logistic function has an S-shaped curve that can take any real-valued number and map it into a value between 0 and 1, but never exactly at those limits.
- The logistic function is also called the logit function, and the inverse of the logistic function is called the log-odds function, which maps a probability value into a real-valued number.
- The log-odds function is defined as:

  `log-odds = ln(y / (1 - y))`

  Where y is the probability of belonging to a certain class, and ln is the natural logarithm function.

- The log-odds function can be used to derive the logistic regression equation from the linear regression equation, by applying the inverse logit function to both sides of the equation.
- The logistic regression equation can be written as:

  `log-odds = b0 + b1*x`

  Where log-odds is the natural logarithm of the odds ratio, which is the ratio of the probability of belonging to a certain class over the probability of not belonging to that class.

- The logistic regression equation can be extended to multiple inputs by adding more terms to the linear combination of inputs, such as:

  `log-odds = b0 + b1*x1 + b2*x2 + ... + bn*xn`

  Where b0, b1, b2, ..., bn are the coefficients for the n input values (x1, x2, ..., xn).

- The coefficients of the logistic regression equation can be learned from the training data using various techniques, such as gradient descent, Newton's method, or stochastic gradient descent.
- The goal of learning the coefficients is to minimize the error between the predicted outputs and the actual outputs, which can be measured by a loss function, such as the cross-entropy loss or the log-likelihood loss.
- The cross-entropy loss is defined as:

  `L = - (y * ln(p) + (1 - y) * ln(1 - p))`

  Where y is the actual output, p is the predicted output, and ln is the natural logarithm function.

- The cross-entropy loss measures the difference between the actual and predicted probabilities of belonging to a certain class, and penalizes wrong predictions more than correct predictions.
- The log-likelihood loss is defined as:

  `L = - ln(p)`

  Where p is the predicted probability of the actual output.

- The log-likelihood loss measures the likelihood of the predicted probability given the actual output, and maximizes the likelihood of the correct predictions.
- The cross-entropy loss and the log-likelihood loss are equivalent for binary classification, but differ for multiclass classification.
- Logistic regression can be used as a part of a bigger model, such as a neural network, by using it as the last layer of the model.
- Logistic regression can also be used as a baseline model to compare the performance of more complex models, such as deep learning models.
- Logistic regression is a simple but widely employed machine learning method that can solve complex problems in a variety of industries, such as medicine, finance, and marketing.

- Some mnemonics and learning tricks for logistic regression are:

  - Remember that logistic regression is used for classification, not regression, by thinking of the word "logic", which implies discrete values, not continuous values.
  - Remember that logistic regression uses the logistic function, which has an S-shaped curve, by