### Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various settings, such as Euclidean spaces, complex vector spaces, and integrals.
- The inequality states that for any two vectors **x** and **y** of an inner product space, it is true that

$$|\langle x, y \rangle| \leq \|x\| \|y\|$$

where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

$$\|x\| = \sqrt{\langle x, x \rangle}$$

$$\|y\| = \sqrt{\langle y, y \rangle}$$

- The inequality can be interpreted geometrically as saying that the absolute value of the cosine of the angle between **x** and **y** is less than or equal to one, since

$$|\langle x, y \rangle| = \|x\| \|y\| \cos \theta$$

where $\theta$ is the angle between **x** and **y**.

- The inequality becomes an equality if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.

- The inequality can be proved in various ways, such as using the properties of the inner product, completing the square, or applying the more general Hölder's inequality.

- The inequality can be generalized to more than two vectors, such as

$$|\langle x_1, x_2, \dots, x_n \rangle| \leq \|x_1\| \|x_2\| \cdots \|x_n\|$$

where $\langle x_1, x_2, \dots, x_n \rangle$ is the n-linear extension of the inner product, and $\|x_i\|$ is the norm of $x_i$ for $i = 1, 2, \dots, n$.

- The inequality can also be extended to infinite-dimensional vector spaces, such as function spaces, where the inner product is defined as an integral, such as

$$\left|\int_a^b f(x) g(x) dx \right| \leq \sqrt{\int_a^b f(x)^2 dx} \sqrt{\int_a^b g(x)^2 dx}$$

where $f$ and $g$ are square-integrable functions on the interval $[a, b]$.

- The inequality has many applications in mathematics, such as in analysis, geometry, probability, statistics, optimization, and linear algebra. For example, it can be used to prove the triangle inequality, the Schwarz lemma, the Cauchy-Schwarz master class, the Gram-Schmidt orthogonalization, and the Hahn-Banach theorem.