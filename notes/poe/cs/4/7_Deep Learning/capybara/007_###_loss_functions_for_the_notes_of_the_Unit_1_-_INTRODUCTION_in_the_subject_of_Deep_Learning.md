### Loss Functions for the Notes of the Unit 1 - INTRODUCTION in the Subject of Deep Learning

A loss function, also known as a cost function or objective function, is a mathematical function that measures the difference between the predicted output and the actual output in a machine learning model. The goal of a loss function is to minimize this difference or error as much as possible.

In Deep Learning, there are various loss functions that are commonly used, depending on the type of problem and the type of output. Here are some of the most commonly used loss functions in Deep Learning:

1. Mean Squared Error (MSE) Loss Function:
   This is the most commonly used loss function for regression problems. It measures the average squared difference between the predicted and actual output. The formula for MSE is:

   MSE = 1/n * Σ(yi - ŷi)²

   where n is the number of samples, yi is the actual output, and ŷi is the predicted output.

2. Binary Cross-Entropy Loss Function:
   This is the most commonly used loss function for binary classification problems. It measures the difference between the predicted probability and the actual probability of a binary outcome. The formula for binary cross-entropy is:

   BCE = -1/n * Σ(yi * log(ŷi) + (1 - yi) * log(1 - ŷi))

   where n is the number of samples, yi is the actual outcome (0 or 1), and ŷi is the predicted probability of the outcome being 1.

3. Categorical Cross-Entropy Loss Function:
   This is the most commonly used loss function for multi-class classification problems. It measures the difference between the predicted probability and the actual probability of a categorical outcome. The formula for categorical cross-entropy is:

   CCE = -1/n * ΣΣ(yij * log(ŷij))

   where n is the number of samples, yij is the actual probability of the jth class for the ith sample, and ŷij is the predicted probability of the jth class for the ith sample.

4. Hinge Loss Function:
   This is a loss function that is commonly used for support vector machines (SVMs) in binary classification problems. It measures the distance between the predicted output and the decision boundary. The formula for hinge loss is:

   Hinge = 1/n * Σ(max(0, 1 - yi * ŷi))

   where n is the number of samples, yi is the actual outcome (1 or -1), and ŷi is the predicted outcome.

These are some of the most commonly used loss functions in Deep Learning. It is important to choose the right loss function for your problem, as it can have a significant impact on the performance of your model.