### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform binary classification.
- A perceptron consists of four main components:
  - A set of **inputs** (x1, x2, ..., xn) that represent the features of the data.
  - A set of **weights** (w1, w2, ..., wn) that represent the importance of each input.
  - A **weighted sum** (z) that computes the linear combination of inputs and weights: z = w1x1 + w2x2 + ... + wnxn + b, where b is a bias term.
  - An **activation function** (ϕ) that applies a threshold to the weighted sum and outputs either 0 or 1: ϕ(z) = 1 if z > 0, 0 otherwise.
- A perceptron can be trained using a **learning algorithm** that updates the weights and bias based on the prediction errors.
  - The algorithm starts with random weights and bias and iterates over the training data.
  - For each data point, the algorithm computes the prediction (ŷ) using the activation function and compares it with the actual label (y).
  - If the prediction is correct, the algorithm does nothing. If the prediction is wrong, the algorithm adjusts the weights and bias by adding or subtracting a fraction of the input values.
  - The fraction is determined by a **learning rate** (η) that controls how fast the algorithm learns.
  - The algorithm repeats this process until the prediction errors are minimized or a maximum number of iterations is reached.
- A perceptron can be represented as a **graphical model** that shows the inputs, weights, bias, weighted sum, activation function, and output.
  - The inputs are shown as circles, the weights are shown as arrows, the bias is shown as a constant, the weighted sum is shown as a sum node, the activation function is shown as a threshold node, and the output is shown as a circle.
  - The graphical model can be simplified by omitting the sum and threshold nodes and showing only the inputs, weights, bias, and output.
  - The graphical model can also be extended to show multiple perceptrons connected to form a **layer** or a **network**.

![Perceptron graphical model](https://miro.medium.com/max/1400/1*4TJWlK-FPhskEIJshfEx5g.png)

: https://en.wikipedia.org/wiki/Perceptron
: https://www.section.io/engineering-education/perceptron-algorithm/
: https://towardsdatascience.com/perceptron-explanation-implementation-and-a-visual-example-3c8e76b4e2d1
: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html
: https://medium.com/geekculture/the-perceptron-algorithm-how-it-works-and-why-it-works-3668a80f8797