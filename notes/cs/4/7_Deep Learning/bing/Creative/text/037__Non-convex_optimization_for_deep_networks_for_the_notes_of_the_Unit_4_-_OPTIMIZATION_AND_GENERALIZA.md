### Non-convex optimization for deep networks

- Non-convex optimization is the study of finding the optimal solution of a problem that has a non-convex objective function or non-convex constraints.
- Non-convex optimization problems are often NP-hard, meaning that there is no efficient algorithm that can guarantee to find the global optimum in polynomial time.
- Non-convex optimization problems arise frequently in machine learning and deep learning, especially when the models are non-linear, such as neural networks, tensor models, and latent variable models.
- Non-convex optimization problems can have multiple local optima, saddle points, and flat regions, which can make gradient-based methods get stuck or converge slowly.
- Non-convex optimization problems can also have structural properties, such as sparsity, low rank, or smoothness, that can be exploited to design efficient algorithms or to obtain theoretical guarantees.
- Some popular techniques for non-convex optimization include:

  - Relaxation: transforming a non-convex problem into a convex one by relaxing some of the constraints or approximating the objective function, and then solving the convex problem using traditional methods.
  - Heuristics: applying simple and intuitive algorithms, such as projected gradient descent, alternating minimization, or stochastic gradient descent, that can often find good solutions in practice, but may not have rigorous convergence or optimality guarantees.
  - Randomization: introducing randomness into the optimization process, such as by initializing the algorithm from multiple starting points, adding noise to the gradient, or sampling a subset of the data, to escape from local optima or saddle points and to improve the convergence rate or the generalization performance.
  - Regularization: adding a penalty term to the objective function that favors solutions with certain desirable properties, such as sparsity, low rank, or smoothness, and that can also prevent overfitting or improve the conditioning of the problem.
  - Proximal methods: using a proximal operator that can efficiently solve a subproblem involving a convex function and a simple constraint, such as a norm or a projection, and that can also incorporate regularization or sparsity-inducing terms.
  - Coordinate descent: updating one or a few variables at a time, while keeping the others fixed, which can reduce the computational complexity and exploit the structure of the problem.
  - Majorization-minimization: constructing a surrogate function that upper bounds the original objective function and that is easier to minimize, and then iteratively minimizing the surrogate function until convergence.
  - Gradient-based methods: using the gradient or a subgradient of the objective function to guide the search direction, which can be combined with line search, trust region, or momentum techniques to improve the convergence speed or stability.
  - Second-order methods: using the Hessian or an approximation of the second derivative of the objective function to refine the search direction, which can be more effective near local optima or saddle points, but also more expensive to compute and store.
  - Variational methods: reformulating the optimization problem as a variational problem that involves finding the minimum of a functional, which can be solved using techniques such as the Euler-Lagrange equation, the calculus of variations, or the augmented Lagrangian method.