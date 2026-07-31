# Gaussian Kernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Gaussian kernel regression is a non-parametric technique to estimate the conditional expectation of a random variable.
- It is based on the idea of using a weighted average of the observed data points to approximate the unknown function.
- The weight of each data point is determined by a kernel function, which is a symmetric and positive function that measures the similarity or proximity of two points.
- The Gaussian kernel is a specific choice of kernel function that has the form of a normal distribution with mean zero and variance sigma^2.
- The Gaussian kernel has some desirable properties, such as being smooth, differentiable, and having a finite support.
- The variance parameter sigma^2 controls the bandwidth or smoothness of the kernel function. Smaller values of sigma^2 lead to more local and less smooth estimates, while larger values of sigma^2 lead to more global and smoother estimates.
- The optimal value of sigma^2 can be chosen by cross-validation or other criteria, such as the Akaike information criterion or the Bayesian information criterion.
- Gaussian kernel regression can be seen as a special case of kernel ridge regression, where the regularization parameter is zero.
- Gaussian kernel regression can also be related to neural networks and Gaussian processes, as shown in some recent works .