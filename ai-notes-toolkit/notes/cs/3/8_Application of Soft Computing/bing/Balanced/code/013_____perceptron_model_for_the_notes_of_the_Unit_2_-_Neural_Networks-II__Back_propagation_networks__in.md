### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform binary classification.
- A perceptron consists of four main components:
  - A set of **inputs** (x1, x2, ..., xn) that represent the features of the data.
  - A set of **weights** (w1, w2, ..., wn) that determine the importance of each input.
  - A **weighted sum** (z) that computes the linear combination of inputs and weights: z = w1x1 + w2x2 + ... + wnxn + b, where b is a bias term.
  - An **activation function** (ϕ) that applies a threshold to the weighted sum and outputs either 0 or 1: ϕ(z) = 1 if z ≥ 0, 0 otherwise.
- A perceptron can be represented by the following diagram:

![Perceptron diagram](https://miro.medium.com/max/1400/1*4TJWlKuP0hF1kWUZDUImaQ.png)

- A perceptron can be trained using the **perceptron learning algorithm**, which updates the weights and bias based on the prediction errors on the training data.
- The perceptron learning algorithm works as follows:
  - Initialize the weights and bias to zero or small random values.
  - For each training example (x, y), where x is the input vector and y is the true label (0 or 1):
    - Compute the weighted sum z and the output ϕ(z) of the perceptron.
    - Compare the output with the true label and calculate the error e = y - ϕ(z).
    - Update the weights and bias by adding the product of the error and the input: wi = wi + e * xi, b = b + e, for i = 1, 2, ..., n.
  - Repeat the above steps until the error is zero or a maximum number of iterations is reached.