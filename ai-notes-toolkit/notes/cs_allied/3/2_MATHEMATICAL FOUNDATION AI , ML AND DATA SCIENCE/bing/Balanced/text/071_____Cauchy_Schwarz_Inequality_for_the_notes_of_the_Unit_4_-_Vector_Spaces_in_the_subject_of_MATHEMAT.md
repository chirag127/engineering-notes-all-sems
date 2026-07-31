### Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various fields such as geometry, analysis, probability, and linear algebra.
- The inequality states that for any two vectors **x** and **y** in an inner product space, it is true that

  $$|\langle x, y \rangle| \leq \|x\| \|y\|$$

  where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

  $$\|x\| = \sqrt{\langle x, x \rangle}$$

  $$\|y\| = \sqrt{\langle y, y \rangle}$$

- The equality holds if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.
- The inequality can be proved by using the fact that the inner product is bilinear, symmetric, and positive definite, and by considering the following expression for any scalar $\lambda$:

  $$\langle x - \lambda y, x - \lambda y \rangle \geq 0$$

  Expanding and simplifying, we get

  $$\lambda^2 \|y\|^2 - 2 \lambda \langle x, y \rangle + \|x\|^2 \geq 0$$

  This is a quadratic equation in $\lambda$, and it has at most one real root, since its discriminant is

  $$\Delta = 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2$$

  To ensure that $\Delta \leq 0$, we must have

  $$\langle x, y \rangle^2 \leq \|x\|^2 \|y\|^2$$

  Taking the square root of both sides, we obtain the Cauchy-Schwarz inequality.
- The inequality can be generalized to other settings, such as sums, integrals, and matrices. For example, if **a** and **b** are two vectors in $\mathbb{R}^n$, then

  $$\left| \sum_{i=1}^n a_i b_i \right| \leq \sqrt{\sum_{i=1}^n a_i^2} \sqrt{\sum_{i=1}^n b_i^2}$$

  where the inner product is defined as

  $$\langle a, b \rangle = \sum_{i=1}^n a_i b_i$$

  and the norm is defined as

  $$\|a\| = \sqrt{\langle a, a \rangle}$$

  This is a special case of the more general Hölder's inequality, which applies to any positive exponents $p$ and $q$ such that $\frac{1}{p} + \frac{1}{q} = 1$.