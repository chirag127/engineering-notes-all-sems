# Logistic Regression for the Notes of the Unit 1 - INTRODUCTION in the Subject of Deep Learning

- Logistic regression is a supervised learning algorithm used to classify data into two or more classes   .
- Logistic regression can be used for both binary and multiclass classification  .
- Logistic regression predicts the output of a categorical dependent variable (such as yes/no, 0/1, true/false, etc.) using a given set of independent variables (such as features, attributes, etc.) .
- Logistic regression uses a linear function to model the relationship between the independent variables and the dependent variable, and then applies a sigmoid function to map the linear output to a probability value between 0 and 1  .
- Logistic regression can be expressed as:

    y = h(x) = sigmoid(θ^T^ x) = 1 / (1 + e^(-θ^T^ x)^)

    where y is the predicted output, x is the input vector, θ is the parameter vector, and sigmoid is the sigmoid function .

- Logistic regression can be trained using various optimization methods, such as gradient descent, Newton's method, or stochastic gradient descent, to find the optimal values of θ that minimize the cost function  .
- Logistic regression can be used as the last layer of a deep learning model, where the features are usually learned by previous layers, such as convolutional neural networks or recurrent neural networks .
- Logistic regression can also be used as a standalone model, if the features are hand-crafted and sufficient for the classification task .
- Logistic regression is a simple, fast, and powerful algorithm that can achieve good performance on many classification problems, especially when the data is linearly separable .