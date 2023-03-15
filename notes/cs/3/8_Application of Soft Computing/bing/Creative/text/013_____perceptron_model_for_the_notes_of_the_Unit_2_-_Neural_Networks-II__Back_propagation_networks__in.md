### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform binary classification.
- A perceptron consists of four main components:
  - A set of input features **x1, x2, ..., xn** that represent the attributes of the data point.
  - A set of weights **w1, w2, ..., wn** that measure the importance of each input feature.
  - A bias term **b** that shifts the decision boundary away from the origin.
  - An activation function **ϕ** that maps the weighted sum of the inputs and the bias to an output value, usually 0 or 1.
- The output of a perceptron is given by the following formula:

  ```math
  y = ϕ(w1x1 + w2x2 + ... + wnxn + b)
  ```

- The activation function ϕ is typically a **step function** that returns 1 if the argument is positive and 0 otherwise.
- The perceptron can be trained using a **learning algorithm** that updates the weights and the bias based on the prediction errors.
- The perceptron learning algorithm works as follows:
  - Initialize the weights and the bias to zero or small random values.
  - For each training example **(x, y)**, where **x** is the input vector and **y** is the true label, do the following:
    - Compute the output **y'** of the perceptron using the current weights and bias.
    - Compute the error **e = y - y'**.
    - Update the weights and the bias using the following rules:

      ```math
      w_i = w_i + αex_i
      b = b + αe
      ```

      where **α** is the learning rate, a positive constant that controls the size of the updates.
  - Repeat the above steps until the perceptron converges to a solution or a maximum number of iterations is reached.