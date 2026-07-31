### Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various settings, such as sums, integrals, and matrices.
- The inequality states that for any two vectors **x** and **y** of an inner product space, it is true that

$$|\langle x, y \rangle| \leq \|x\| \|y\|$$

where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

$$\|x\| = \sqrt{\langle x, x \rangle}$$

$$\|y\| = \sqrt{\langle y, y \rangle}$$

- The inequality is an equality if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.
- The inequality can be proved in various ways, such as using the properties of the inner product, the Pythagorean theorem, or the quadratic formula. One possible proof is as follows:

Let $\theta$ be the angle between **x** and **y**. Then, by the definition of the inner product, we have

$$\langle x, y \rangle = \|x\| \|y\| \cos \theta$$

Taking the absolute value of both sides, we get

$$|\langle x, y \rangle| = \|x\| \|y\| |\cos \theta|$$

Since $|\cos \theta| \leq 1$ for any angle $\theta$, we have

$$|\langle x, y \rangle| \leq \|x\| \|y\|$$

which is the Cauchy-Schwarz inequality.

- The inequality can be generalized to other settings, such as sums of real or complex numbers, integrals of functions, or matrices of numbers. For example, if $a_1, a_2, \dots, a_n$ and $b_1, b_2, \dots, b_n$ are real or complex numbers, then

$$\left| \sum_{i=1}^n a_i b_i \right| \leq \sqrt{\sum_{i=1}^n |a_i|^2} \sqrt{\sum_{i=1}^n |b_i|^2}$$

which can be seen as a special case of the Cauchy-Schwarz inequality with the inner product defined as

$$\langle a, b \rangle = \sum_{i=1}^n a_i \overline{b_i}$$

where $\overline{b_i}$ is the complex conjugate of $b_i$.

- The Cauchy-Schwarz inequality has many applications in mathematics, such as proving the triangle inequality, the arithmetic-geometric mean inequality, the Hölder's inequality, the Minkowski inequality, and the Cauchy-Bunyakovsky-Schwarz inequality. It is also useful in fields such as analysis, geometry, probability, statistics, and optimization.