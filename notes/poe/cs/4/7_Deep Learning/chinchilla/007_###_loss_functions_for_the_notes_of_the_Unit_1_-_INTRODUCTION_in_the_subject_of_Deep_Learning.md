### Loss Functions for the Notes of Unit 1 - Introduction in the Subject of Deep Learning

In deep learning, loss functions are used to measure the difference between the predicted output and the actual output. The goal is to minimize this difference, also known as the loss or the cost, during training. In this section, we will discuss some commonly used loss functions in deep learning.

1. Mean Squared Error (MSE) Loss Function:
MSE is a commonly used loss function for regression problems. It measures the average squared difference between the predicted and actual output. It can be represented mathematically as:

    MSE = 1/n * Σ(y_pred - y_actual)^2

    Where:
    n = number of samples
    y_pred = predicted output
    y_actual = actual output

2. Binary Cross-Entropy Loss Function:
Binary cross-entropy is a commonly used loss function for binary classification problems. It measures the difference between the predicted probability and the actual probability for a binary classification problem. It can be represented mathematically as:

    BCE = -1/n * Σ(y_actual * log(y_pred) + (1-y_actual) * log(1-y_pred))

    Where:
    n = number of samples
    y_pred = predicted probability
    y_actual = actual label (0 or 1)

3. Categorical Cross-Entropy Loss Function:
Categorical cross-entropy is a commonly used loss function for multi-class classification problems. It measures the difference between the predicted probability distribution and the actual probability distribution for a multi-class classification problem. It can be represented mathematically as:

    CCE = -1/n * ΣΣ(y_actual * log(y_pred))

    Where:
    n = number of samples
    y_pred = predicted probability distribution
    y_actual = actual probability distribution (one-hot encoded)

4. Hinge Loss Function:
Hinge loss is a commonly used loss function for binary classification problems. It is used in support vector machines (SVMs) to maximize the margin between the decision boundary and the closest data points. It can be represented mathematically as:

    Hinge Loss = max(0, 1 - y_pred * y_actual)

    Where:
    y_pred = predicted output
    y_actual = actual output (1 or -1)

5. Huber Loss Function:
Huber loss is a loss function that is less sensitive to outliers than mean squared error loss. It is commonly used in regression problems. It can be represented mathematically as:

    Huber Loss = 1/n * Σ(loss)

    Where:
    n = number of samples
    loss = 0.5 * (y_pred - y_actual)^2 if |y_pred - y_actual| <= delta 
           delta * (|y_pred - y_actual| - 0.5 * delta) otherwise

    Where delta is a hyperparameter that determines the threshold for the loss function.

Mnemonics and Learning Tricks:
- For binary classification problems, use binary cross-entropy loss function.
- For multi-class classification problems, use categorical cross-entropy loss function.
- For regression problems, use mean squared error loss function.
- Hinge loss is used in SVMs to maximize the margin between the decision boundary and the closest data points.
- Huber loss is less sensitive to outliers than mean squared error loss and is commonly used in regression problems.