### Loss Functions for the Notes of the Unit 1 - INTRODUCTION in the Subject of Deep Learning

- A loss function is a function that compares the target and predicted output values of a deep learning model and measures how well the model fits the training data.
- The goal of training a deep learning model is to minimize the average loss over the entire training dataset by adjusting the model parameters (weights and biases) using an optimization algorithm such as gradient descent.
- The choice of the loss function depends on the type of the problem (regression or classification), the output distribution (continuous or discrete), and the desired properties of the loss function (differentiability, robustness, etc.).
- There are many loss functions to choose from, but some of the most common ones are:

  - **Mean Squared Error (MSE)**: This is the average of the squared differences between the target and predicted values. It is used for regression problems where the output is continuous and normally distributed. It is sensitive to outliers and large errors. It is also differentiable and easy to compute. The formula is:

    ```
    MSE = (1/n) * sum((y_true - y_pred)^2)
    ```

    where n is the number of examples, y_true is the target value, and y_pred is the predicted value.

  - **Mean Absolute Error (MAE)**: This is the average of the absolute differences between the target and predicted values. It is also used for regression problems where the output is continuous, but it is more robust to outliers and large errors than MSE. It is not differentiable at zero, but it is easy to compute. The formula is:

    ```
    MAE = (1/n) * sum(|y_true - y_pred|)
    ```

    where n is the number of examples, y_true is the target value, and y_pred is the predicted value.

  - **Binary Cross-Entropy (BCE)**: This is the negative of the average of the logarithm of the predicted probabilities for the target values. It is used for binary classification problems where the output is either 0 or 1. It penalizes wrong predictions more than correct ones, and it encourages the model to output probabilities close to 0 or 1. It is differentiable and easy to compute. The formula is:

    ```
    BCE = -(1/n) * sum(y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred))
    ```

    where n is the number of examples, y_true is the target value (0 or 1), and y_pred is the predicted probability (between 0 and 1).

  - **Categorical Cross-Entropy (CCE)**: This is the negative of the average of the logarithm of the predicted probabilities for the target classes. It is used for multiclass classification problems where the output is one of K possible classes. It penalizes wrong predictions more than correct ones, and it encourages the model to output probabilities close to 1 for the correct class and close to 0 for the other classes. It is differentiable and easy to compute. The formula is:

    ```
    CCE = -(1/n) * sum(sum(y_true * log(y_pred)))
    ```

    where n is the number of examples, y_true is the target one-hot vector (a vector of length K with 1 in the correct class and 0 in the other classes), and y_pred is the predicted probability vector (a vector of length K with probabilities between 0 and 1).

  - **Sparse Categorical Cross-Entropy (SCCE)**: This is the same as CCE, but it uses the target class index instead of the one-hot vector. It is used for multiclass classification problems where the output is one of K possible classes, but the target values are integers from 0 to K-1. It is more efficient than CCE in terms of memory and computation. The formula is:

    ```
    SCCE = -(1/n) * sum(log(y_pred[y_true]))
    ```

    where n is the number of examples, y_true is the target class index (an integer from 0 to K-1), and y_pred is the predicted probability vector (a vector of length K with probabilities between 0 and 1).

- Some mnemonics and learning tricks for the loss functions are:

  - MSE: Mean Squared Error, Squares the Errors, Sensitive to Outliers, Used for Regression
  - MAE: Mean Absolute Error, Absolutes the Errors, Robust to Outliers, Used