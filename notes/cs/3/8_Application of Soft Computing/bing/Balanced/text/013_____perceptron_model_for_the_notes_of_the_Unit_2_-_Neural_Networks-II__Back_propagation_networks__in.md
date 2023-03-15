### Perceptron Model

- A perceptron is a **simplified model of a biological neuron** that can perform **binary classification** tasks.
- A perceptron consists of four main components:
  - A set of **inputs** (x1, x2, ..., xn) that represent the features of the data.
  - A set of **weights** (w1, w2, ..., wn) that represent the importance of each input.
  - A **bias** (b) that represents the threshold for activation.
  - An **activation function** (ϕ) that determines the output of the perceptron based on the weighted sum of the inputs and the bias.
- The output of the perceptron (y) is given by:

  y = ϕ(w1x1 + w2x2 + ... + wnxn + b)

- The activation function ϕ is usually a **step function** that outputs 1 if the weighted sum is greater than or equal to zero, and 0 otherwise.
- The perceptron can be trained using the **perceptron learning algorithm**, which updates the weights and the bias based on the prediction errors.
- The perceptron learning algorithm works as follows:
  - Initialize the weights and the bias to zero or small random values.
  - For each training example (x, y):
    - Compute the output of the perceptron (y') using the current weights and bias.
    - Compute the error (e) as the difference between the desired output (y) and the actual output (y').
    - Update the weights and the bias using the following rules:

      wi = wi + αexi

      b = b + αe

    - Where α is the **learning rate**, a positive constant that controls the magnitude of the updates.
  - Repeat the above steps until the perceptron converges (no more errors) or a maximum number of iterations is reached.