### Polynomial kernel

- A polynomial kernel is a kernel function that represents the similarity of vectors in a feature space over polynomials of the original variables, allowing learning of non-linear models.
- A kernel function is a function that maps the input data into a higher-dimensional space, where it is easier to separate the classes using a linear classifier.
- A polynomial kernel is defined as:

$$
K(x,y)=(x^Ty+c)^d
$$

where $x$ and $y$ are vectors in the input space, $c \geq 0$ is a free parameter trading off the influence of higher-order versus lower-order terms in the polynomial, and $d$ is the degree of the polynomial.

- A polynomial kernel can capture the interactions between the original features up to the specified degree. For example, if $d=2$, the polynomial kernel can model the quadratic terms of the form $x_i^2$, $x_i x_j$, and $x_j^2$.
- A polynomial kernel can be derived from another kernel function $\kappa_1$ by applying a polynomial function to it. For example, if $\kappa_1$ is the linear kernel, then the polynomial kernel is:

$$
K(x,y)=p(\kappa_1(x,y))=(\kappa_1(x,y)+c)^d=(x^Ty+c)^d
$$

where $p$ is a polynomial function with positive coefficients.

- A polynomial kernel can be computed using the sklearn.metrics.pairwise.polynomial_kernel function in Python, which takes the input data $X$ and $Y$, the degree $d$, the coefficient $c$, and the scaling factor $\gamma$ as parameters. The scaling factor $\gamma$ is optional and defaults to $1/n\_features$ where $n\_features$ is the number of features in the input data.