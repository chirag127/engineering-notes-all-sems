### Gaussian kernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Gaussian kernel regression is a non-parametric method of estimating the conditional expectation of a random variable given some observations.
- It is based on the idea of weighting the observations according to their similarity or distance to the query point, and then taking the average of the weighted observations as the prediction.
- The similarity or distance is measured by a kernel function, which is a symmetric and positive definite function that satisfies some properties. One such kernel function is the Gaussian kernel, which has the form:

$$
K(x, x') = \exp\left(-\frac{(x - x')^2}{2\sigma^2}\right)
$$

- where $\sigma$ is a parameter that controls the width or smoothness of the kernel. A smaller $\sigma$ means a narrower kernel, which gives more weight to the nearby observations and less weight to the faraway ones. A larger $\sigma$ means a wider kernel, which gives more uniform weight to all observations and results in a smoother prediction.
- The prediction of Gaussian kernel regression for a query point $x^*$ is given by:

$$
\hat{y}(x^*) = \frac{\sum_{i=1}^n K(x^*, x_i) y_i}{\sum_{i=1}^n K(x^*, x_i)}
$$

- where $n$ is the number of observations, $x_i$ and $y_i$ are the input and output of the $i$-th observation, and $K(x^*, x_i)$ is the kernel value between the query point and the $i$-th observation.
- Gaussian kernel regression can be seen as a special case of kernel ridge regression, which is a regularized version of linear regression with a kernel trick. The kernel trick allows us to implicitly map the inputs to a high-dimensional feature space, where the linear regression can capture the nonlinear patterns in the data. The regularization term helps to avoid overfitting and improve the generalization performance.
- Gaussian kernel regression can also be seen as a connection between solving kernel regression and training the last layer of an infinitely wide neural network. Such a connection will lead naturally into the development of Neural Network Gaussian Processes (NNGP) and the Neural Tangent Kernel.