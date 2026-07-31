# Taylor's and Laurent's series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a complex number.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a complex function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a complex function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients that can be obtained by integrating $f(z)$ along a closed contour in the annulus.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has singularities or is not analytic at a point.

- A Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$. The principal part is also called the **singular part** because it reflects the behavior of the function near the singularity at $z_0$.

- The **order** of a singularity at $z_0$ is the largest positive integer $m$ such that the coefficient $a_{-m}$ in the Laurent series is nonzero. The order of a singularity indicates how fast the function diverges near the singularity.

- A singularity at $z_0$ is called **isolated** if there is a disk around $z_0$ that contains no other singularities of the function. A singularity at $z_0$ is called **removable** if the function can be defined at $z_0$ in such a way that it becomes analytic in a disk around $z_0$. A removable singularity has a Laurent series with only the analytic part.

- A singularity at $z_0$ is called a **pole** if it is isolated and has a finite order. A pole of order $m$ has a Laurent series with a principal part of the form

$$\sum_{n=1}^{m} \frac{a_{-n}}{(z-z_0)^n}$$

where $a_{-m} \neq 0$. A pole of order $1$ is also called a **simple pole**.

- A singularity at $z_0$ is called **essential** if it is isolated and has an infinite order. An essential singularity has a Laurent series with an infinite number of nonzero terms in the principal part. An essential singularity has a very erratic behavior near $z_0$ and cannot be approximated by a polynomial or a rational function.