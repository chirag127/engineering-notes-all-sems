### Non-convex optimization for deep networks

- Non-convex optimization is the process of finding the optimal solution of a function that is not convex, meaning that it has multiple local minima and maxima, and possibly saddle points.
- Non-convex optimization problems are common in machine learning and deep learning, such as training deep neural networks and learning latent variable models.
- Non-convex optimization problems are generally NP-hard to solve, meaning that there is no efficient algorithm that can guarantee to find the global optimum in polynomial time.
- However, non-convex optimization problems can still be solved approximately by using gradient-based methods, such as gradient descent, stochastic gradient descent, mini-batch gradient descent, momentum, Adam, etc.
- Gradient-based methods rely on the idea of following the direction of the steepest descent of the function, which is given by the negative gradient, until a local minimum is reached.
- Gradient-based methods can be applied to non-convex functions, but they are not guaranteed to converge to the global minimum, and may get stuck at a local minimum or a saddle point.
- However, recent theoretical and empirical results have shown that gradient-based methods can still perform well on non-convex optimization problems, especially for deep neural networks .
- Some of the reasons why gradient-based methods work well for non-convex optimization problems are:

  - The non-convex functions encountered in deep learning are often smooth and have a low degree of non-convexity, meaning that they have few and shallow local minima and saddle points.
  - The stochasticity and noise introduced by the data and the mini-batch sampling can help the gradient-based methods escape from local minima and saddle points.
  - The over-parameterization of deep neural networks, meaning that they have more parameters than necessary to fit the data, can reduce the number of bad local minima and make them easier to escape from.
  - The regularization techniques, such as weight decay, dropout, batch normalization, etc, can improve the generalization and stability of the gradient-based methods.

- Therefore, non-convex optimization for deep networks is a challenging but feasible problem, and gradient-based methods are the most widely used and effective algorithms for solving it.