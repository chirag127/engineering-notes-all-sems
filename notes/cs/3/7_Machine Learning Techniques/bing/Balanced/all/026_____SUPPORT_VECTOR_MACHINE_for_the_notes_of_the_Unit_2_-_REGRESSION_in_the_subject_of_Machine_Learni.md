# Support Vector Machine

- Support vector machine (SVM) is a supervised machine learning technique that can be used for both classification and regression tasks .
- SVM was first proposed by Vladimir Vapnik and his colleagues in 1992 .
- SVM is based on the idea of finding a hyperplane that separates the data points into different classes or predicts the output value for a given input .
- SVM is considered a nonparametric technique because it relies on kernel functions to map the data into a higher-dimensional space where a linear separation is possible .
- SVM has several advantages, such as:
  - It is effective in high-dimensional spaces.
  - It is robust to outliers and noise.
  - It can handle nonlinear and complex data patterns.
  - It has a clear geometric interpretation.
- SVM also has some disadvantages, such as:
  - It can be computationally expensive for large data sets.
  - It can be sensitive to the choice of kernel and parameters.
  - It can suffer from overfitting if the number of features is much larger than the number of samples.
  - It does not provide probability estimates for the predictions.

## SVM for Regression

- SVM can also be used for regression problems, where the goal is to predict a continuous output value for a given input .
- SVM regression is also known as support vector regression (SVR) or epsilon-SVR .
- SVR works by finding a function that fits the data points within a certain margin of error, called epsilon .
- SVR tries to minimize the following objective function :

  - L = 1/2 ||w||^2 + C * sum(max(0, |y_i - f(x_i)| - epsilon))^i
  - where w is the weight vector, C is the regularization parameter, y_i is the true output value, f(x_i) is the predicted output value, and epsilon is the margin of error.
- SVR uses the same kernel trick as SVM for classification to map the data into a higher-dimensional space where a linear function can be found .
- SVR has similar advantages and disadvantages as SVM for classification, except that it can also handle multiple output regression.