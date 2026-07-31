# Gaussian Kernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Gaussian Kernel Regression is a **non-parametric** regression technique that uses a **weighted average** of the observed data points to estimate the value of a new point.
- The weight of each observed point is determined by a **kernel function**, which is a function that assigns higher values to points that are closer to the query point and lower values to points that are farther away.
- One such kernel function is the **Gaussian kernel**, which has the form:

$$
K(x^*, x_i) = \exp\left(-\frac{(x^* - x_i)^2}{2b^2}\right)
$$

where $x^*$ is the query point, $x_i$ is an observed point, and $b$ is a **bandwidth** parameter that controls the smoothness of the kernel .

- The Gaussian kernel can also be interpreted as a **normal distribution** with mean $x_i$ and standard deviation $b$, which means that the kernel assigns higher probability to points that are closer to the mean.
- The estimated value of the query point $y^*$ is given by:

$$
y^* = \frac{\sum_{i=1}^n K(x^*, x_i) y_i}{\sum_{i=1}^n K(x^*, x_i)}
$$

where $n$ is the number of observed points and $y_i$ is the corresponding label of $x_i$ .

- Gaussian Kernel Regression has some advantages and disadvantages:
  - Advantages:
    - It does not require any **iterative learning** or **model selection**, as it directly uses the observed data to estimate the new point.
    - It can capture **non-linear** relationships between the input and output variables, as it does not assume any parametric form of the regression function.
    - It can be easily **generalized** to higher dimensions and different types of kernels, such as polynomial, sigmoid, etc.
  - Disadvantages:
    - It can be **computationally expensive**, as it requires calculating the kernel function for every pair of points.
    - It can be **sensitive** to the choice of the bandwidth parameter $b$, which affects the smoothness and bias-variance trade-off of the kernel .
    - It can suffer from **overfitting** or **underfitting** if the bandwidth parameter is too small or too large, respectively .