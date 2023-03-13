### Non-convex optimization for deep networks for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning

- Non-convex optimization (NCO) is the process of finding the optimal solution of a function that is not convex, meaning that it has multiple local minima and maxima, and possibly saddle points.
- NCO is challenging because traditional convex optimization methods, such as gradient descent, may get stuck in suboptimal local minima or saddle points, and finding the global minimum is often NP-hard.
- NCO is widely used in machine learning and deep learning, where many problems of interest, such as training deep neural networks and learning latent variable models, are non-convex.
- Despite being non-convex, deep neural networks are surprisingly amenable to optimization by gradient descent and its variants, such as stochastic gradient descent (SGD), mini-batching, stochastic variance-reduced gradient (SVRG), and momentum.
- Some possible reasons for the success of NCO for deep learning are:
  - The loss function of deep neural networks may have many local minima that are close to the global minimum in terms of function value, and gradient descent can escape from poor local minima by exploiting the noise in the gradient estimation.
  - The loss function of deep neural networks may have many saddle points that are not too sharp, and gradient descent can escape from saddle points by exploiting the curvature information in the Hessian matrix or its approximations.
  - The loss function of deep neural networks may have some symmetries or invariances that make the optimization landscape smoother and easier to navigate.
- Some possible challenges and limitations of NCO for deep learning are:
  - The convergence rate and complexity of NCO algorithms may depend on the problem size, the dimensionality, the smoothness, the curvature, and the noise level of the function, and these factors may vary widely in different applications and datasets.
  - The optimal solution of NCO may not be unique or stable, and may depend on the initialization, the learning rate, the regularization, and the random seed of the algorithm, and these factors may affect the generalization performance and the interpretability of the model.
  - The optimal solution of NCO may not be robust or reliable, and may be sensitive to outliers, adversarial examples, model misspecification, and distribution shift, and these factors may affect the security and the fairness of the model.

- Some possible mnemonics and learning tricks for NCO for deep learning are:
  - NCO stands for Non-Convex Optimization, which is Not Completely Obvious, but Necessary for Complex Objectives.
  - Gradient descent is a greedy algorithm that goes Downhill, but may get Stuck in a Valley or a Plateau, unless it has some Noise or Momentum to help it Escape.
  - Saddle points are like Horses, they have a High Back and a Low Belly, and they are Hard to Ride, unless you have a Saddle or a Whip to control them.
  - Symmetries and invariances are like Mirrors and Rotations, they make the function look the Same from different Angles, and they make the optimization Easier and Smoother.