# Types of support vector kernel

- Support vector machines (SVMs) are supervised learning algorithms that can be used for classification or regression problems.
- SVMs use a technique called the kernel trick to transform the input data into a higher dimensional space where a linear decision boundary can be found.
- A kernel function is a function that computes the similarity between two data points in the transformed space.
- Different kernel functions can produce different decision boundaries and have different properties and parameters.
- Some of the popular kernel functions used in SVMs are:

  - **Linear kernel**: This is the simplest kernel function, which is just the dot product of the input vectors. It produces a linear decision boundary and does not have any parameters. It is suitable for linearly separable data or when the number of features is large compared to the number of samples.
  - **Polynomial kernel**: This kernel function computes the dot product of the input vectors raised to some power, plus a constant term. It produces a polynomial decision boundary and has two parameters: the degree of the polynomial and the constant term. It can model non-linear relationships, but it may also overfit the data if the degree is too high or the constant term is too large.
  - **Radial basis function (RBF) kernel**: This kernel function computes the exponential of the negative squared distance between the input vectors. It produces a non-linear decision boundary that depends on the distance from a center point. It has one parameter: the gamma value, which controls the width of the kernel. It can fit any data, but it may also overfit the data if the gamma value is too small or underfit the data if the gamma value is too large.
  - **Sigmoid kernel**: This kernel function computes the hyperbolic tangent of the dot product of the input vectors plus a constant term. It produces a non-linear decision boundary that resembles a sigmoid function. It has two parameters: the slope and the constant term. It can model non-linear relationships, but it may also suffer from numerical instability or poor performance if the parameters are not chosen carefully.