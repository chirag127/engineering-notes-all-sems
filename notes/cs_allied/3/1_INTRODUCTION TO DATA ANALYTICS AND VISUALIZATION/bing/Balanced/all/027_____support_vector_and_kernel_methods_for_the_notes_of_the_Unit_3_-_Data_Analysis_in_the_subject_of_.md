# Support Vector and Kernel Methods

## Support Vector Machines (SVMs)

- SVMs are a type of supervised learning algorithm that can perform classification and regression tasks.
- SVMs aim to find an optimal hyperplane that separates the data into different classes or predicts the output value.
- SVMs use the concept of margin, which is the distance between the hyperplane and the closest data points (called support vectors).
- SVMs try to maximize the margin while minimizing the classification or regression error.
- SVMs can handle linearly separable and non-linearly separable data by using different types of kernels.

## Kernel Methods

- Kernel methods are a way of transforming the data into a higher-dimensional feature space where linear methods can be applied.
- Kernel methods use a function called a kernel, which computes the similarity or inner product between two data points in the feature space.
- Kernel methods avoid the explicit computation of the feature space, which can be costly or infeasible, by using the kernel trick.
- The kernel trick is a technique that allows linear algorithms to operate on the kernel matrix, which contains the pairwise kernel values of the data points.
- Kernel methods can be used with various algorithms, such as SVMs, Gaussian processes, PCA, ridge regression, etc.

## Types of Kernels

- There are many types of kernels that can be used for different purposes and data types.
- Some common types of kernels are:

  - Linear kernel: the simplest kernel, which computes the dot product between two vectors.
  - Polynomial kernel: a kernel that computes a polynomial function of the dot product between two vectors, with a degree and a bias parameter.
  - Radial basis function (RBF) kernel: a kernel that computes the exponential of the negative squared Euclidean distance between two vectors, with a bandwidth parameter.
  - Sigmoid kernel: a kernel that computes the hyperbolic tangent of the dot product between two vectors, with a slope and a constant parameter.
  - Laplacian kernel: a kernel that computes the exponential of the negative L1 norm (Manhattan distance) between two vectors, with a bandwidth parameter.
  - Chi-squared kernel: a kernel that computes the similarity between two histograms, based on the chi-squared distance.
  - Cosine similarity kernel: a kernel that computes the cosine of the angle between two vectors.

## Advantages and Disadvantages of Kernel Methods

- Kernel methods have some advantages, such as:

  - They can handle non-linear and complex data by using appropriate kernels.
  - They can improve the performance and generalization of linear methods by mapping the data to a higher-dimensional space.
  - They can exploit the prior knowledge or domain-specific information by using custom kernels.
  - They can reduce the computational complexity by using the kernel trick.

- Kernel methods also have some disadvantages, such as:

  - They can suffer from the curse of dimensionality, which means that the feature space can become too large or sparse for some kernels.
  - They can be sensitive to the choice of the kernel and its parameters, which can affect the results and require tuning.
  - They can be prone to overfitting, especially with high-degree polynomial or RBF kernels, which can fit the noise in the data.
  - They can be difficult to interpret, as the feature space and the kernel function may not have a clear meaning.

: https://medium.com/geekculture/kernel-methods-in-support-vector-machines-bb9409342c49
: https://www.educba.com/kernel-methods/
: https://www.sciencedirect.com/topics/neuroscience/support-vector-machine
: https://en.wikipedia.org/wiki/Kernel_method
: https://direct.mit.edu/books/book/1821/Learning-with-KernelsSupport-Vector-Machines
: https://medium.com/analytics-vidhya/introduction-to-svm-and-kernel-trick-part-1-theory-d990e2872ace