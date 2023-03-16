### Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various settings, such as sums, integrals, and matrices.
- The inequality states that for any two vectors **x** and **y** of an inner product space, it is true that

$$|\langle x, y \rangle| \leq \|x\| \|y\|$$

where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

$$\|x\| = \sqrt{\langle x, x \rangle}$$

$$\|y\| = \sqrt{\langle y, y \rangle}$$

- The inequality can be interpreted geometrically as saying that the absolute value of the cosine of the angle between **x** and **y** is at most one, or equivalently, that the angle between **x** and **y** is at most 90 degrees.

$$|\langle x, y \rangle| = \|x\| \|y\| |\cos \theta| \leq \|x\| \|y\|$$

- The inequality becomes an equality if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.

$$|\langle x, y \rangle| = \|x\| \|y\| \iff x = \lambda y \text{ or } y = \lambda x \text{ for some scalar } \lambda$$

- The inequality can be proved in various ways, such as using the properties of the inner product, the quadratic formula, or the more general Hölder's inequality. A common proof is as follows:

  - Let **x** and **y** be any two vectors of an inner product space. If either of them is the zero vector, then the inequality is trivially true, so assume that they are both nonzero.
  - Consider the vector **z** = **x** - $\lambda$**y**, where $\lambda$ is any scalar. Then, by the properties of the inner product, we have

  $$\langle z, z \rangle = \langle x - \lambda y, x - \lambda y \rangle = \langle x, x \rangle - 2 \lambda \langle x, y \rangle + \lambda^2 \langle y, y \rangle$$

  - Since the inner product is always nonnegative, we have

  $$\langle z, z \rangle \geq 0$$

  - This implies that the quadratic polynomial in $\lambda$,

  $$\lambda^2 \langle y, y \rangle - 2 \lambda \langle x, y \rangle + \langle x, x \rangle$$

  has at most one real root, or equivalently, its discriminant is nonpositive. That is,

  $$(2 \langle x, y \rangle)^2 - 4 \langle y, y \rangle \langle x, x \rangle \leq 0$$

  - Simplifying and taking square roots, we get

  $$|\langle x, y \rangle| \leq \|x\| \|y\|$$

  as desired.

- The inequality can be generalized to other settings, such as:

  - Finite sums: If $a_1, a_2, \dots, a_n$ and $b_1, b_2, \dots, b_n$ are real or complex numbers, then

  $$\left| \sum_{i=1}^n a_i b_i \right| \leq \sqrt{\sum_{i=1}^n |a_i|^2} \sqrt{\sum_{i=1}^n |b_i|^2}$$

  where the inner product is defined as $\langle a, b \rangle = \sum_{i=1}^n a_i \overline{b_i}$, and the norm is defined as $\|a\| = \sqrt{\langle a, a \rangle}$.

  - Integrals: If $f$ and $g$ are real or complex-valued functions on an interval $[a, b]$, then

  $$\left| \int_a^b f(x) g(x) dx