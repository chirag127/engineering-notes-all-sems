# Unit 2 - REGRESSION
## Polynomial Kernel

- A polynomial kernel is a kernel function commonly used in machine learning.
- It represents the similarity of vectors in a feature space over polynomials of the original variables, allowing learning of non-linear models.
- The polynomial kernel is defined as: K(x, y) = (x.y + c)^d, where x and y are vectors, c is a constant, and d is the degree of the polynomial.
- The constant c is usually chosen to avoid negative values in the kernel matrix.
- The degree of the polynomial determines the flexibility of the model, with higher degrees allowing for more complex decision boundaries.
- The polynomial kernel can be used in various machine learning algorithms, such as support vector machines and kernel principal component analysis.
- It is important to choose the right degree and constant for the polynomial kernel, as these hyperparameters can greatly affect the performance of the model.
