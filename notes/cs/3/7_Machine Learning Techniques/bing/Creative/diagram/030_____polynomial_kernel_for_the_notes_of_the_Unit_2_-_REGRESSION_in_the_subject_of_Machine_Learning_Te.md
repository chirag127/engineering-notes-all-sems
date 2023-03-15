### Polynomial kernel

- A polynomial kernel is a kernel function that represents the similarity of vectors in a feature space over polynomials of the original variables, allowing learning of non-linear models.
- A kernel function is a function that maps the input data into a higher-dimensional space, where linear methods can be applied to separate the data.
- A polynomial kernel of degree d is defined as:

$$
K(x,y) = (x^Ty + c)^d
$$

where x and y are vectors in the input space, i.e. vectors of features computed from training or test samples and c ≥ 0 is a free parameter trading off the influence of higher-order versus lower-order terms in the polynomial.

- A polynomial kernel can capture the interactions between the original features up to the specified degree.
- A polynomial kernel can be used with support vector machines (SVMs) and other kernelized models, such as kernel ridge regression, kernel principal component analysis, and kernel k-means .
- A polynomial kernel can be computed in different ways, such as full expansion of the kernel prior to training/testing with a linear SVM, or using an approximate kernel matrix based on low-rank approximations.
- A polynomial kernel can have different properties depending on the choice of the parameters, such as symmetry, positive definiteness, and smoothness.
- A polynomial kernel can be suitable for problems where the data is not linearly separable, but can be separated by a polynomial function.