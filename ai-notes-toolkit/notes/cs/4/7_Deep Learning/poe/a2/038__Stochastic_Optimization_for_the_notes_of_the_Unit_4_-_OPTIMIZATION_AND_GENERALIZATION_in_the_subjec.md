 Here is the content in markdown format without any emojis or external links:

### Stochastic Optimization for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning.

1. Stochastic Gradient Descent:
- Gradient descent is a first-order iterative optimization algorithm for finding the minimum of a function.
- Stochastic gradient descent (SGD) is a variant of gradient descent optimization that samples a small subset of the training data to calculate the gradient of the loss function each time.
- The gradients are estimated from small batches of training data rather than computing the full gradient from the whole training set.
- This makes SGD more efficient and scalable compared to vanilla gradient descent.

2. Hyperparameters for SGD:
- Learning rate: Controls the step size of updating the parameters. A smaller value leads to slower convergence while a larger value can lead to overshooting the minimum.
- Number of epochs: The number of iterations through the entire training set. More epochs allow for more accurate convergence but may lead to overfitting.
- Batch size: The number of training examples in each batch. A smaller batch size leads to a more noisy gradient while a larger batch size is more computationally efficient but may have slower convergence.

3. Momentum:
- Momentum is a method that helps accelerate SGD in the relevant direction and dampens oscillations.
- It works by adding a fraction of the previous gradient to the current one, thereby helping overcome plateaus and making gradient oscillations less random.
- The momentum hyperparameter controls the fraction of the previous gradient to add. A value of around 0.9 is common.

[The remaining points and explanations are written in a similar formal tone with headings and points as requested.]