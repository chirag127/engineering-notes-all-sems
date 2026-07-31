### Non-convex optimization for deep networks

1. Non-convex optimization is a type of optimization that deals with non-convex programs, which were previously seen as the defining boundary for tractability in continuous optimization.
2. Many problems of interest arising from machine learning and statistical modeling, such as training deep neural networks and learning latent variable models, are non-convex.
3. Despite being non-convex, deep neural networks are surprisingly amenable to optimization by gradient descent.
4. Non-convex optimization techniques, such as sparse recovery, help discard irrelevant parameters and promote compact and accurate models.
5. The freedom to express the learning problem as a non-convex optimization problem gives immense modeling power to the algorithm designer, but often such problems are NP-hard to solve.
6. A popular workaround to this has been to relax non-convex problems to convex ones and use traditional methods to solve the (convex) relaxed optimization problems.
7. For Non-convex Optimization Convergence, many Convex Optimization techniques can be used such as stochastic gradient descent (SGD), mini-batching, stochastic variance-reduced gradient (SVRG), and momentum.
8. There has been recent increased interest in optimization algorithms for non-convex optimization in application to training deep neural networks and other optimization problems in data analysis.
