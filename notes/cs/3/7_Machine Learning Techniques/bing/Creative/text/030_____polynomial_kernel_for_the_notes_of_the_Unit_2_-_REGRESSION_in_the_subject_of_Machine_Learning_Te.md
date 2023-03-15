### Polynomial kernel

- A polynomial kernel is a kernel function that represents the similarity of vectors in a feature space over polynomials of the original variables, allowing learning of non-linear models.
- A kernel function is a function that maps the input data into a higher-dimensional space, where it is easier to separate the data using a linear classifier.
- A polynomial kernel of degree d is defined as:

$$
K(x,y) = (x^T y + c)^d
$$

where x and y are vectors in the input space, i.e. vectors of features computed from training or test samples and c ≥ 0 is a free parameter trading off the influence of higher-order versus lower-order terms in the polynomial.

- A polynomial kernel can capture the interactions between the original features up to the specified degree.
- A polynomial kernel can be derived from another kernel κ1 by applying a polynomial function with positive coefficients to it, such as:

$$
K(x,y) = p(\kappa_1(x,y)) = (\alpha \kappa_1(x,y) + \beta)^d
$$

where α, β and d are positive constants.

- A polynomial kernel can be computed in different ways, such as:

  - Full expansion of the kernel prior to training/testing with a linear SVM, i.e. full computation of the mapping φ as in:

  $$
  K(x,y) = \phi(x)^T \phi(y) = (x^T y + c)^d
  $$

  - Approximate expansion of the kernel using random features, i.e. sampling a finite number of features from the mapping φ as in:

  $$
  K(x,y) \approx z(x)^T z(y) = \sum_{i=1}^m \cos(w_i^T x + b_i) \cos(w_i^T y + b_i)
  $$

  where wi and bi are random vectors and scalars drawn from appropriate distributions.

  - Direct computation of the kernel using the kernel trick, i.e. avoiding the explicit mapping φ and using the kernel function directly as in:

  $$
  K(x,y) = (x^T y + c)^d
  $$

  - This can reduce the computational complexity and memory requirements of the SVM algorithm.