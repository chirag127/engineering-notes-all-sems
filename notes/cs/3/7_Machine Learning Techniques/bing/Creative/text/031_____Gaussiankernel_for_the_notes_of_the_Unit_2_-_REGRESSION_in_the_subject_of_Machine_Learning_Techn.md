### Gaussian Kernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Kernel regression is a non-parametric method of estimating a function from a set of data points.
- Kernel regression uses a weighted average of the data points to approximate the function at a given point.
- The weights are determined by a kernel function, which measures the similarity or distance between the data points and the given point.
- A kernel function can have different shapes, such as linear, polynomial, sigmoid, or Gaussian.
- A Gaussian kernel is a kernel function that has the form of a Gaussian (or normal) distribution, also known as a bell-shaped curve.
- A Gaussian kernel is defined as:

$$
K(x^*, x_i) = \exp\left(-\frac{(x^* - x_i)^2}{2b^2}\right)
$$

- Where $x^*$ is the given point, $x_i$ is a data point, and $b$ is a parameter that controls the width or bandwidth of the kernel.
- A Gaussian kernel has the following properties:
  - It is symmetric, meaning that $K(x^*, x_i) = K(x_i, x^*)$.
  - It is positive, meaning that $K(x^*, x_i) \geq 0$ for any $x^*$ and $x_i$.
  - It is normalized, meaning that $\int K(x^*, x) dx = 1$ for any $x^*$.
  - It is smooth, meaning that it has no sharp edges or discontinuities.
  - It is local, meaning that it decays rapidly as the distance between $x^*$ and $x_i$ increases.
- A Gaussian kernel regression is a kernel regression that uses a Gaussian kernel as the kernel function.
- A Gaussian kernel regression can be expressed as:

$$
f(x^*) = \frac{\sum_{i=1}^n K(x^*, x_i) y_i}{\sum_{i=1}^n K(x^*, x_i)}
$$

- Where $f(x^*)$ is the estimated function value at $x^*$, $y_i$ is the function value at $x_i$, and $n$ is the number of data points.
- A Gaussian kernel regression has the following advantages:
  - It is simple and easy to implement, as it does not require any iterative learning or optimization.
  - It is flexible and adaptive, as it can capture nonlinear and complex patterns in the data.
  - It is robust and resistant to outliers, as it gives more weight to the nearby and similar data points.
- A Gaussian kernel regression has the following disadvantages:
  - It is computationally expensive, as it requires calculating the kernel function for every pair of points.
  - It is sensitive to the choice of the bandwidth parameter $b$, as it affects the smoothness and bias-variance trade-off of the regression.
  - It is prone to overfitting or underfitting, as it depends on the density and distribution of the data points.