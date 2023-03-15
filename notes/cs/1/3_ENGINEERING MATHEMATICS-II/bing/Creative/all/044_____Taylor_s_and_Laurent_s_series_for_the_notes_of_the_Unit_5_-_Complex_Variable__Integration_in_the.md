# Taylor's and Laurent's series

- Taylor's and Laurent's series are two types of power series that can be used to represent complex functions in the complex plane.
- A power series is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a fixed complex number.

- A power series with non-negative power terms is called a Taylor series. A Taylor series can be used to represent a complex function $f(z)$ that is analytic (i.e., differentiable) at a point $z_0$ and in some neighborhood of $z_0$. The coefficients of the Taylor series are given by

$$a_n = \frac{f^{(n)}(z_0)}{n!}$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A Taylor series converges to $f(z)$ in the largest disk centered at $z_0$ that does not contain any singularities (i.e., points where $f(z)$ is not analytic) of $f(z)$.

- A power series with both positive and negative power terms is called a Laurent series. A Laurent series can be used to represent a complex function $f(z)$ that is analytic in an annulus (i.e., a ring-shaped region) around a point $z_0$, but not necessarily at $z_0$. The coefficients of the Laurent series are given by

$$a_n = \frac{1}{2\pi i} \int_{C} \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a simple closed contour in the annulus that encloses $z_0$.

- A Laurent series converges to $f(z)$ in the annulus where $f(z)$ is analytic.

- A Laurent series can be written as the sum of two parts: a Taylor series and a principal part. The Taylor series is the part with non-negative power terms, and the principal part is the part with negative power terms. The principal part can be used to classify the type of singularity at $z_0$.

- If the principal part is zero, then $z_0$ is a removable singularity, meaning that $f(z)$ can be extended to be analytic at $z_0$ by defining $f(z_0)$ to be the value of the Taylor series at $z_0$.

- If the principal part has finitely many terms, then $z_0$ is a pole, meaning that $f(z)$ becomes unbounded as $z$ approaches $z_0$. The order of the pole is the largest negative power in the principal part.

- If the principal part has infinitely many terms, then $z_0$ is an essential singularity, meaning that $f(z)$ behaves erratically as $z$ approaches $z_0$ and cannot be extended to be analytic at $z_0$.

- Taylor's and Laurent's series are useful tools for studying the properties and behavior of complex functions, such as finding residues, evaluating integrals, computing limits, and finding zeros and singularities.