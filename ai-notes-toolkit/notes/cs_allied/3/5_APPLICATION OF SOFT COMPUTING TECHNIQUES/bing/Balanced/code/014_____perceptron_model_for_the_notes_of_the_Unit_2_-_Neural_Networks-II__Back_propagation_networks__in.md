### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform **binary classification** tasks.
- A perceptron consists of four main components:
  - A set of **inputs** (x1, x2, ..., xn) that represent the features of the data.
  - A set of **weights** (w1, w2, ..., wn) that represent the importance of each input.
  - A **weighted sum** (z) that combines the inputs and weights: z = w1x1 + w2x2 + ... + wnxn + b, where b is a bias term.
  - An **activation function** (ϕ) that transforms the weighted sum into an output (y): y = ϕ(z).
- The activation function is usually a **threshold function** that outputs 1 if z is greater than or equal to some threshold value, and 0 otherwise.
- The perceptron can be trained using a **learning algorithm** that updates the weights and bias based on the **prediction errors** of the perceptron on the training data.
- The perceptron can **learn linearly separable** patterns, but it cannot learn nonlinear patterns or solve problems like XOR.
- The perceptron is the **basic unit** of more complex models like **neural networks** and **support vector machines**.