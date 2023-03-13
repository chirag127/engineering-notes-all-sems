### Loss functions for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- A loss function is a mathematical function that measures the difference between the predicted output and the true output in a deep learning model  .
- A loss function evaluates how well the algorithm is modelling the dataset and provides feedback to update the model parameters.
- The goal of a deep learning model is to minimize the loss function by adjusting the weights and biases of the network layers.
- There are different types of loss functions for different types of problems, such as regression, classification, and generative models .
- Some of the most common loss functions for deep learning are:

  - **Mean Squared Error (MSE)**: This is the average of the squared differences between the predicted and true values. It is used for regression problems, where the output is a continuous value. MSE is sensitive to outliers and large errors .

    - Formula: `MSE = (1/n) * sum((y_true - y_pred)^2)`
    - Example: Predicting house prices based on features.
    - Advantages: Easy to calculate and differentiate.
    - Disadvantages: Can lead to overfitting and poor generalization.

  - **Mean Absolute Error (MAE)**: This is the average of the absolute differences between the predicted and true values. It is also used for regression problems, where the output is a continuous value. MAE is less sensitive to outliers and large errors than MSE .

    - Formula: `MAE = (1/n) * sum(|y_true - y_pred|)`
    - Example: Predicting customer satisfaction ratings based on feedback.
    - Advantages: Robust to outliers and large errors.
    - Disadvantages: Can lead to underfitting and poor optimization.

  - **Binary Cross-Entropy (BCE)**: This is the negative of the logarithm of the probability of the true class. It is used for binary classification problems, where the output is either 0 or 1. BCE penalizes wrong predictions more than correct predictions  .

    - Formula: `BCE = - (y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred))`
    - Example: Predicting whether an email is spam or not based on its content.
    - Advantages: Suitable for imbalanced datasets and probabilistic outputs.
    - Disadvantages: Can lead to numerical instability and saturation.

  - **Categorical Cross-Entropy (CCE)**: This is the negative of the logarithm of the probability of the true class. It is used for multi-class classification problems, where the output is one of k possible classes. CCE penalizes wrong predictions more than correct predictions  .

    - Formula: `CCE = - sum(y_true * log(y_pred))`
    - Example: Predicting the type of animal in an image based on its features.
    - Advantages: Suitable for imbalanced datasets and probabilistic outputs.
    - Disadvantages: Can lead to numerical instability and saturation.

  - **Sparse Categorical Cross-Entropy (SCCE)**: This is the same as CCE, except that the true output is encoded as an integer instead of a one-hot vector. It is used for multi-class classification problems, where the output is one of k possible classes. SCCE reduces the memory and computational requirements of CCE .

    - Formula: `SCCE = - sum(log(y_pred[y_true]))`
    - Example: Predicting the digit in a handwritten image based on its pixels.
    - Advantages: Reduces the memory and computational requirements of CCE.
    - Disadvantages: Can lead to numerical instability and saturation.

  - **Kullback-Leibler Divergence (KLD)**: This is the difference between two probability distributions. It is used for generative models, where the output is a probability distribution. KLD measures how well the output distribution matches the true distribution .

    - Formula: `KLD = sum(y_true * log(y_true / y_pred))`
    - Example: Generating realistic images based on a latent vector.
    - Advantages: Suitable for measuring the similarity of probability distributions.