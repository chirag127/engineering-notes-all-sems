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
  - It is scale-invariant, meaning that multiplying x and y by a constant does not change the value of the kernel
  - It is isotropic, meaning that it does not depend on the direction of the difference vector x - y
- The Gaussian kernel regression estimator is given by:

  f(x) = ∑i=1^n K(x, xi) yi / ∑i=1^n K(x, xi)

  where n is the number of data points, xi and yi are the input and output values of the i-th data point, and f(x) is the estimated function value at x.

- The Gaussian kernel regression estimator has the following properties:
  - It is a linear smoother, meaning that it is a linear combination of the data points
  - It is a local smoother, meaning that it gives more weight to the data points that are closer to the query point
  - It is a biased estimator, meaning that it does not necessarily pass through the data points
  - It is a consistent estimator, meaning that it converges to the true function as the number of data points increases and the bandwidth decreases
  - It is sensitive to the choice of the bandwidth parameter, which affects the smoothness and accuracy of the estimator
  - It is computationally expensive, as it requires calculating the kernel function for every pair of query and data points