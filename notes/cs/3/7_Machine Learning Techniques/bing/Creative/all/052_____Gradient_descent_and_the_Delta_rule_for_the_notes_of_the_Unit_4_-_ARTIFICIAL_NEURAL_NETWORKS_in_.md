# Gradient descent and the Delta rule

- Gradient descent is a way to find a minimum in a high-dimensional space. You go in direction of the steepest descent.
- The Delta rule is an update rule for single layer perceptrons. It makes use of gradient descent.
- The key idea behind the Delta rule is to use gradient descent to search the hypothesis space of possible weight vectors to find the weights that best fit the training examples.
- This rule is important because gradient descent provides the basis for the BACKPROPAGATION algorithm, which can learn networks with many interconnected units.
- The Delta rule can be derived from the following steps:
  - Define an error function that measures the difference between the desired output and the actual output of the perceptron for a given input.
  - Calculate the partial derivative of the error function with respect to each weight, which gives the direction of the steepest ascent of the error function.
  - Update each weight by subtracting a small fraction of the partial derivative, which moves the weight in the opposite direction of the steepest ascent, i.e., the steepest descent.
  - Repeat the above steps until the error function reaches a minimum or a satisfactory level.
- The Delta rule can be expressed as:

  ![Delta rule formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/9a9c8a8c0f0a0c7f1f0f8f8a0a0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f