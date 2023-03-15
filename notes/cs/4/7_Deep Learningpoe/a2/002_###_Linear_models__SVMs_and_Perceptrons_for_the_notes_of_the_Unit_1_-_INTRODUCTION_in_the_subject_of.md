 Here is the content in markdown format for the topic ### Linear models (SVMs and Perceptrons for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Linear models (SVMs and Perceptrons)

- Perceptrons are the simplest type of neural network. They are linear classifiers that separate data with a straight line (in 2D) or hyperplane (in higher dimensions).
- They were introduced in the 1950s but faced limitations with non-linear data. Modern neural networks overcome these limitations.
- The steps to train a perceptron are:

1. Initialize weights randomly
2. For each training example:

- Calculate the output (predict class) using `output = sign(sum(input * weights))`
- If output is incorrect, update weights: `weights = weights + input * error`

3. Repeat step 2 until all examples are classified correctly

- Advantages: Simple to implement and train, can learn linear boundaries
- Disadvantages: Limited to linear separable data, prone to overfitting

- Support Vector Machines (SVMs) are more advanced linear models that use a kernel trick to map inputs to high-dimensional space to find optimal hyperplanes for separation.
- They aim to maximize the margin of separation between classes and have regularization parameters to control overfitting.
- SVMs can handle non-linear data by using non-linear kernels (e.g. radial basis function (RBF) kernel).
- Advantages: Effective in high-dimensional spaces, flexible to non-linear data, reduced overfitting
- Disadvantages: Choosing kernel and parameters can be difficult, can be slower to train than perceptrons

- Examples, diagrams and more details can be added as needed. Let me know if you would like me to elaborate on any part of this answer further.