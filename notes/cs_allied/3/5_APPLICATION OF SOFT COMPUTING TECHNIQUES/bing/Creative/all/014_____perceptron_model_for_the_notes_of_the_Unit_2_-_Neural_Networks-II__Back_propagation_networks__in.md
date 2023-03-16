# Perceptron Model

- The perceptron is a **simplified model of a biological neuron** that accepts multiple inputs and outputs a single value  .
- The perceptron has four key components:
  - **Input values**: These are the numerical values that represent the features of the data, such as pixels, coordinates, measurements, etc. Each input value is associated with a **weight**, which reflects its importance or contribution to the output.
  - **Weighted sum**: This is the linear combination of the input values and their weights, i.e., z = w1x1 + w2x2 + ... + wnxn + b, where b is a **bias** term that shifts the decision boundary.
  - **Activation function**: This is a function that maps the weighted sum to the output value, usually by applying a threshold or a non-linearity. For example, the **Heaviside step function** outputs 1 if the weighted sum is positive, and 0 otherwise.
  - **Output value**: This is the final prediction of the perceptron, which can be interpreted as a binary classification (0 or 1) or a continuous value.
- The perceptron can be trained using the **perceptron learning algorithm**, which updates the weights and bias based on the error between the output value and the true label   .
- The perceptron learning algorithm can be summarized as follows :
  - Initialize the weights and bias to zero or small random values.
  - For each training example, compute the output value and the error.
  - If the error is not zero, update the weights and bias by adding or subtracting a fraction of the input values, depending on the sign of the error.
  - Repeat the process until the error is zero for all training examples, or a maximum number of iterations is reached.
- The perceptron can learn linearly separable patterns, but it cannot learn non-linear patterns, such as XOR  . To overcome this limitation, multiple perceptrons can be combined to form a **multi-layer perceptron** or a **neural network**, which can learn more complex functions  .