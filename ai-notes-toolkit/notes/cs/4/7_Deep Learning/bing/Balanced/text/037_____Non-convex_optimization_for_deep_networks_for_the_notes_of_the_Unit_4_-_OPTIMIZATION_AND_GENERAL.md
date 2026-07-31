### Non-convex optimization for deep networks

- Non-convex optimization (NCO) is the study of finding the global minimum of a function that is not convex, meaning it may have multiple local minima and maxima.
- NCO is relevant for deep learning because many problems of interest, such as training deep neural networks and learning latent variable models, are non-convex.
- NCO is challenging because traditional convex optimization methods, such as gradient descent, may get stuck in local minima or saddle points, and finding the global minimum is often NP-hard.
- NCO techniques for deep learning include:
  - Initialization: choosing a good starting point for the optimization algorithm, such as random initialization, pre-training, or orthogonal initialization.
  - Regularization: adding constraints or penalties to the objective function, such as sparsity, dropout, or weight decay, to avoid overfitting and improve generalization.
  - Optimization algorithms: using variants of gradient descent that can escape local minima or saddle points, such as stochastic gradient descent (SGD), mini-batch SGD, momentum, Nesterov accelerated gradient, Adam, RMSProp, or stochastic variance-reduced gradient (SVRG).
  - Learning rate scheduling: adjusting the step size of the optimization algorithm over time, such as using a constant, decreasing, or adaptive learning rate, to balance exploration and exploitation.
  - Normalization: scaling or shifting the inputs or outputs of the neural network layers, such as batch normalization, layer normalization, or group normalization, to reduce internal covariate shift and improve convergence.
  - Architecture design: choosing the structure and parameters of the neural network, such as the number of layers, neurons, activation functions, or connections, to enhance the expressiveness and efficiency of the model.
- NCO theory for deep learning aims to provide rigorous analysis and guarantees of the convergence, complexity, and generalization of the optimization algorithms and models for non-convex problems.
- NCO theory for deep learning relies on tools and concepts from mathematics, such as calculus, linear algebra, probability, statistics, geometry, and complexity theory.