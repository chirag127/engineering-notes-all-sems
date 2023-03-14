 Here is the content in markdown format for the topic ### stochastic gradient descent for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Stochastic Gradient Descent

- Stochastic Gradient Descent (SGD) is a gradient descent algorithm where the gradients are estimated from a single training example (or a minibatch of examples) at each iteration.
- In SGD, the weights are updated after each training example is processed, leading to faster convergence to a minimum than batch gradient descent. However, the path taken by SGD to reach the minimum is more irregular and unpredictable.
- Advantages:
    - Faster convergence rate than batch gradient descent since weights are updated more frequently.
    - Can handle large training datasets since only one or a few training examples are used to calculate gradients at each step.
- Disadvantages:
    - May not converge to the global minimum, can get stuck in local minima.
    - The path to convergence is noisy and meandering, making it difficult to diagnose convergence or divergence.
- Key steps:
    1. Randomly pick a training example
    2. Calculate the gradient of the loss function w.r.t weights using the chosen training example
    3. Update the weights by moving in the negative gradient direction
- Application: SGD is typically used to train large neural networks and deep learning models due to scalability and fast convergence. It is a very popular optimization algorithm for training machine learning models.

- Mnemonics: SGD - One by one learning; Gradient - Slope direction; Descent - Move downwards
- Learning trick: Visualize the slope directions and weight updates for individual training examples to understand how SGD works and converges to a minimum.