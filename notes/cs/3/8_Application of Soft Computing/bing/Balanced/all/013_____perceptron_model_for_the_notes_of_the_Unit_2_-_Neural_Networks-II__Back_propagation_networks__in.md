# Perceptron Model

- The perceptron is a **simplified model of a biological neuron** that accepts multiple inputs and outputs a single value  .
- The perceptron has four key components:
  - **Input values**: These are the numerical values that represent the features of the data, such as pixels, coordinates, measurements, etc.
  - **Weights**: These are the numerical values that determine how much each input contributes to the output. They can be positive or negative, and are usually initialized randomly or with zeros.
  - **Weighted sum**: This is the result of multiplying each input by its corresponding weight and adding them together. It represents the strength of the signal that the perceptron receives.
  - **Activation function**: This is a function that maps the weighted sum to the output value. It usually has a threshold or a range that determines whether the output is positive or negative, or between 0 and 1. A common activation function is the **step function**, which outputs 1 if the weighted sum is greater than or equal to 0, and 0 otherwise.
- The perceptron can be represented by the following diagram :

![Perceptron diagram](https://miro.medium.com/max/1400/1*6xGh6l7y6nZT6Zy0fZw8jg.png)

- The perceptron can be used for **binary classification** tasks, such as identifying whether an image contains a cat or a dog, or whether an email is spam or not  .
- The perceptron can learn from data by **updating its weights** based on the errors it makes on the training examples  .
- The perceptron learning algorithm is as follows  :
  - Initialize the weights to random values or zeros.
  - For each training example, compute the output value using the current weights and the activation function.
  - Compare the output value with the actual label of the example, and calculate the error.
  - Update the weights by adding or subtracting a fraction of the error multiplied by the input value. This fraction is called the **learning rate**, and it controls how fast the perceptron learns.
  - Repeat the steps until the error is minimized or a maximum number of iterations is reached.
- The perceptron can only learn **linearly separable** patterns, meaning that the data can be divided by a straight line or a hyperplane .
- The perceptron can be extended to handle **multiclass classification** or **nonlinear patterns** by using multiple perceptrons in parallel or in layers, forming a **neural network** .