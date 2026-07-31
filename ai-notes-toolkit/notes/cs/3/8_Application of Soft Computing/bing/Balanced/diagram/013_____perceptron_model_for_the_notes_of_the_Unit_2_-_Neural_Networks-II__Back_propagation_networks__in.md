### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform binary classification.
- A perceptron has four key components:
  - **Inputs**: A set of numerical features that represent the data, such as x1, x2, ..., xn.
  - **Weights**: A set of coefficients that determine how much each input contributes to the output, such as w1, w2, ..., wn.
  - **Bias**: A constant term that shifts the decision boundary, such as b.
  - **Activation function**: A function that maps the weighted sum of the inputs and the bias to the output, such as a step function or a sigmoid function.
- The output of a perceptron is given by the following formula:

  ```math
  y = \phi(w_1x_1 + w_2x_2 + ... + w_nx_n + b)
  ```

  where y is the output, \phi is the activation function, w_i is the weight for the i-th input, x_i is the i-th input, and b is the bias.
- The perceptron can be trained using a learning algorithm that updates the weights and the bias based on the error between the predicted output and the actual output.
- The perceptron can be used to model linearly separable problems, such as logical operations (AND, OR, NOT) or simple classification tasks.
- The perceptron can be extended to a multi-layer perceptron, which consists of multiple perceptrons arranged in layers, to model more complex and nonlinear problems.