### Gaussian Kernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Kernel regression is a non-parametric method of estimating a function from a set of data points.
- Kernel regression uses a weighted average of the data points, where the weights are determined by a kernel function that measures the similarity or distance between the query point and the data points.
- A kernel function is a symmetric and positive definite function that satisfies the following properties:
  - K(x, y) = K(y, x) for any x and y
  - K(x, y) ≥ 0 for any x and y
  - ∫K(x, y) dx dy = 1 for any y
- A common choice of kernel function is the Gaussian kernel, which is defined as:

  K(x, y) = exp(-||x - y||^2 / (2b^2))

  where b is a bandwidth parameter that controls the width of the kernel.

- The Gaussian kernel has the following properties:
  - It is smooth and differentiable everywhere
  - It has a bell-shaped curve that decays rapidly as the distance between x and y increases
  - It has a single parameter b that determines the trade-off between bias and variance of the estimator
  - It is invariant to translations and rotations of the data
- The Gaussian kernel regression estimator is given by:

  f(x) = ∑i=1^n K(x, xi) yi / ∑i=1^n K(x, xi)

  where n is the number of data points, xi are the input features, and yi are the output labels.

- The Gaussian kernel regression estimator has the following properties:
  - It is a linear combination of the data labels, weighted by the kernel function
  - It is a local estimator, meaning that it only depends on the data points that are close to the query point
  - It is a smooth and continuous function that interpolates the data points
  - It is sensitive to the choice of the bandwidth parameter b, which affects the smoothness and complexity of the estimator
  - It can handle nonlinear and high-dimensional data, as long as the kernel function captures the underlying structure of the data
- The Gaussian kernel regression estimator can be computed efficiently using matrix operations, such as:

  f(x) = K(x, X) y / K(x, X) 1

  where K(x, X) is a vector of kernel values between x and each row of X, y is a vector of data labels, and 1 is a vector of ones.