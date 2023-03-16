### Non-convex optimization for deep networks

- Non-convex optimization (NCO) is the study of finding the global minimum of a function that is not convex, meaning that it may have multiple local minima and maxima .
- NCO is relevant for deep learning because many problems of interest, such as training deep neural networks and learning latent variable models, are non-convex .
- NCO is challenging because it is often NP-hard to solve, meaning that there is no efficient algorithm that can guarantee to find the global minimum in polynomial time.
- NCO is also difficult because it may involve non-smooth functions, meaning that they are not differentiable everywhere or have discontinuities.
- Despite these challenges, NCO has been shown to be surprisingly amenable to optimization by gradient-based methods, such as stochastic gradient descent (SGD), mini-batching, stochastic variance-reduced gradient (SVRG), and momentum .
- These methods rely on the idea that the gradient of a non-convex function can provide useful information about the direction of descent, even if it does not point to the global minimum .
- Moreover, these methods can exploit the structure and properties of the non-convex function, such as smoothness, Lipschitz continuity, strong convexity, or sparsity, to improve their convergence and performance .
- Recent theoretical advances in NCO have provided global performance guarantees for some of these methods, such as showing that they can escape from saddle points, find approximate local minima, or achieve linear convergence rates under certain conditions .
- These results have helped to explain the empirical success of NCO in deep learning and other machine learning applications, and have also suggested new directions for improving and designing NCO algorithms .