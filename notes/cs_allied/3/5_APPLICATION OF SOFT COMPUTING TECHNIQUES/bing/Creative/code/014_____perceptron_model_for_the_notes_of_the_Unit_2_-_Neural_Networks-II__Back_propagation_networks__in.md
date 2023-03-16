### Perceptron Model

- The perceptron is a **simplified model of a biological neuron** that accepts multiple inputs and outputs a single value  .
- The perceptron has four key components:
  - **Input values (x1, x2, ..., xn)**: These are the numerical values that are fed into the perceptron, such as features of a data point.
  - **Weights (w1, w2, ..., wn)**: These are the numerical values that represent the strength of the connection between each input and the output. They are learned by the perceptron during the training process.
  - **Weighted sum (z)**: This is the sum of the products of the inputs and their corresponding weights, i.e. z = w1x1 + w2x2 + ... + wnxn.
  - **Activation function (ϕ)**: This is a function that maps the weighted sum to the output value, usually by applying a threshold. For example, a common activation function is the Heaviside step function, which outputs 1 if z is positive and 0 otherwise.
- The perceptron can be used for **binary classification** tasks, such as predicting whether an email is spam or not, or whether a tumor is malignant or benign  .
- The perceptron can be trained using the **perceptron learning algorithm**, which is an iterative process that updates the weights based on the prediction errors  .
  - The algorithm starts with random or zero weights, and a learning rate parameter (η) that controls the size of the weight updates.
  - For each training example, the algorithm computes the output of the perceptron using the current weights and compares it with the true label (y).
  - If the output matches the label, the weights are unchanged. If the output is incorrect, the weights are updated by adding or subtracting the product of the learning rate and the input value, depending on the sign of the error.
  - The algorithm repeats this process until the perceptron converges to a solution, or a maximum number of iterations is reached.
- The perceptron has some limitations and assumptions  :
  - It can only learn linearly separable functions, i.e. functions that can be separated by a straight line in the input space. If the data is not linearly separable, the perceptron will never converge and will make errors on some examples.
  - It is sensitive to the order and the size of the training examples, as different sequences or subsets of examples may lead to different solutions.
  - It does not have a way of measuring the confidence or the uncertainty of its predictions, as it only outputs a binary value.
  - It does not generalize well to multiple classes or complex functions, as it is a single-layer model with a simple activation function.