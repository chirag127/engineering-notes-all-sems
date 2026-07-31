### Non-convex optimization for deep networks

- Non-convex optimization (NCO) is the study of finding the global minimum of a function that is not convex, meaning it may have multiple local minima and maxima.
- NCO is relevant for deep learning because many problems of interest, such as training deep neural networks and learning latent variable models, are non-convex and cannot be easily solved by convex optimization methods.
- NCO is challenging because it is often NP-hard to find the global minimum of a non-convex function, and gradient-based methods may get stuck in local minima or saddle points.
- NCO techniques for deep learning include:
  - Initialization: choosing a good starting point for the optimization algorithm, such as using random weights or pre-training.
  - Regularization: adding constraints or penalties to the objective function to avoid overfitting and improve generalization, such as weight decay, dropout, or batch normalization.
  - Optimization algorithms: using variants of gradient descent that can escape local minima or saddle points, such as stochastic gradient descent (SGD), momentum, Nesterov accelerated gradient (NAG), adaptive gradient (AdaGrad), RMSProp, Adam, or stochastic variance-reduced gradient (SVRG).
  - Learning rate scheduling: adjusting the step size of the optimization algorithm according to some criteria, such as decreasing the learning rate over time or using a cyclical learning rate.
  - Second-order methods: using information about the curvature of the objective function, such as the Hessian matrix or its approximations, to speed up convergence and avoid saddle points, such as Newton's method, quasi-Newton methods, or trust region methods.
- NCO theory for deep learning aims to provide guarantees on the convergence, complexity, and generalization of optimization algorithms for non-convex problems, such as:
  - Showing that gradient descent can converge to a global minimum or a second-order stationary point under certain assumptions on the objective function, such as smoothness, strong convexity, or restricted strong convexity.
  - Showing that SGD can converge to a global minimum or a second-order stationary point with high probability under certain assumptions on the objective function and the noise distribution, such as smoothness, strong convexity, or restricted strong convexity, and sub-Gaussian noise or bounded variance.
  - Showing that NCO algorithms can achieve a trade-off between the optimization error and the generalization error, such as using the notion of sharpness, flatness, or stability.
  - Showing that NCO algorithms can exploit the structure or properties of the objective function, such as sparsity, low-rank, or Lipschitz continuity, to improve the convergence rate or the generalization performance.