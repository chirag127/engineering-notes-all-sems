### What a shallow network computes for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- A shallow network is a neural network that has only one hidden layer between the input and output layers .
- A shallow network computes a nonlinear transformation of the input features, using the weights and biases of the hidden layer neurons, and then applies another linear or nonlinear transformation to produce the output, using the weights and biases of the output layer neurons.
- A shallow network can be represented by the following equation:

```
y = f(W2 * g(W1 * x + b1) + b2)
```

where x is the input vector, y is the output vector, W1 and W2 are the weight matrices, b1 and b2 are the bias vectors, g is the activation function of the hidden layer, and f is the activation function of the output layer.

- A shallow network can learn to approximate any continuous function, given enough hidden neurons and training data, according to the universal approximation theorem.
- A shallow network can be trained using gradient descent and backpropagation, which are algorithms that update the weights and biases based on the error between the predicted output and the actual output.
- A shallow network can be used for various tasks, such as regression, classification, clustering, dimensionality reduction, etc., depending on the choice of the output layer activation function and the loss function.
- A shallow network has some advantages and disadvantages compared to a deep network, which has more than one hidden layer :

  - Advantages:
    - Easier to train and interpret
    - Less prone to overfitting and vanishing gradients
    - Faster to compute and evaluate
  - Disadvantages:
    - Less expressive and flexible
    - Less able to capture complex and hierarchical patterns
    - More sensitive to the choice of hyperparameters and initialization