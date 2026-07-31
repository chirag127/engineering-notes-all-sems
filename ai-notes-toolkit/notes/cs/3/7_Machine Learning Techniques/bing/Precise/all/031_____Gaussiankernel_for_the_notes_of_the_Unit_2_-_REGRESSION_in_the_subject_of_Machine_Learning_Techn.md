# Unit 2 - REGRESSION

### Gaussian Kernel

- Gaussian kernel, also known as the radial basis function (RBF) kernel, is a popular kernel function used in various kernelized learning algorithms.
- In particular, it is commonly used in support vector machine classification.
- The Gaussian kernel is defined as: K(x, y) = exp(-||x-y||^2 / (2σ^2))
- Where x and y are two feature vectors, and σ is a free parameter that controls the width of the Gaussian function.
- The Gaussian kernel is a measure of similarity between two feature vectors, with the value of the kernel decreasing as the distance between the two vectors increases.
- The choice of σ can have a significant impact on the performance of the kernelized learning algorithm, and is typically chosen through cross-validation.
- The Gaussian kernel is widely used due to its flexibility and ability to handle high-dimensional data.
