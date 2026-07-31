# Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various settings, such as sums, integrals, and matrices.
- The inequality states that for any two vectors **x** and **y** in an inner product space, it is true that

$$|\langle x, y \rangle| \leq \|x\| \|y\|$$

where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

$$\|x\| = \sqrt{\langle x, x \rangle}$$

$$\|y\| = \sqrt{\langle y, y \rangle}$$

- The inequality can be interpreted geometrically as saying that the absolute value of the cosine of the angle between **x** and **y** is less than or equal to one, or equivalently, that the angle between **x** and **y** is acute or right.

$$|\langle x, y \rangle| = \|x\| \|y\| |\cos \theta| \leq \|x\| \|y\|$$

- The inequality becomes an equality if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.

$$|\langle x, y \rangle| = \|x\| \|y\| \iff x = \lambda y \text{ or } y = \lambda x \text{ for some scalar } \lambda$$

- The inequality can be proved in various ways, such as using the properties of the inner product, the Pythagorean theorem, or the quadratic formula. One common proof is as follows:

  - Let **x** and **y** be any two vectors in an inner product space. If **y** is the zero vector, then the inequality is trivially true, since both sides are zero. So assume that **y** is not the zero vector.
  - Consider the vector **z** = **x** - $\lambda$**y**, where $\lambda$ is any scalar. Then, by the properties of the inner product, we have

  $$\langle z, z \rangle = \langle x - \lambda y, x - \lambda y \rangle = \langle x, x \rangle - 2 \lambda \langle x, y \rangle + \lambda^2 \langle y, y \rangle$$

  - Since the inner product is always non-negative, we have

  $$\langle z, z \rangle \geq 0$$

  - This implies that the quadratic polynomial in $\lambda$,

  $$\lambda^2 \langle y, y \rangle - 2 \lambda \langle x, y \rangle + \langle x, x \rangle$$

  has either no real roots or one repeated root. By the discriminant of the quadratic formula, this means that

  $$\Delta = b^2 - 4ac \leq 0$$

  where $a = \langle y, y \rangle$, $b = -2 \langle x, y \rangle$, and $c = \langle x, x \rangle$. Simplifying, we get

  $$4 \langle x, y \rangle^2 - 4 \langle x, x \rangle \langle y, y \rangle \leq 0$$

  Dividing by 4 and taking the square root of both sides, we obtain the Cauchy-Schwarz inequality:

  $$|\langle x, y \rangle| \leq \|x\| \|y\|$$

  - Moreover, the equality holds if and only if the discriminant is zero, which means that the quadratic polynomial has a repeated root, which means that **z** is the zero vector, which means that **x** and **y** are linearly dependent. This completes the proof.