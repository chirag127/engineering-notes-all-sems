 Here is the content in markdown format without any emojis or external links, written in a formal tone with points:

### Stochastic Gradient Descent

1. Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fit linear/logistic regression models on medium/large sized learning problems.
2. Instead of using the whole training set in each iteration like in Batch Gradient Descent, we randomly pick a small subset of training samples in each iteration. We then update the model parameters by taking a gradient step towards the minimizing the loss calculated on just the chosen samples.
3. This has a couple of key benefits:
    - Since we are using just a subset of the training data, each gradient step is much faster to compute. This can lead to a significant speed up compared to Batch Gradient Descent when working with large datasets.
    - For large training sets, evaluating the cost function on the whole training set can be prohibitively expensive as it needs to be done in every iteration. This makes SGD a more practical alternative.
4. A potential downside is that we may get noisy gradient estimates, as we are only using a random subset of the data. This can result in a less optimal minimum being found. However, in practice this effect is often small, and the significant speed up gained using SGD often outweighs this disadvantage.
5. When implementing SGD, a few important hyperparameters to tune are:
    - Learning rate: The size of the gradient steps taken. Needs to be tuned for convergence.
    - Subset size: The number of training samples to use in each gradient estimate. Larger values can reduce noise but may be slower.
    - Stopping criteria: An approach to detect when gradient descent has converged to a (local) minimum. For example, stop when gradient magnitudes are small, or a fixed number of iterations is reached.