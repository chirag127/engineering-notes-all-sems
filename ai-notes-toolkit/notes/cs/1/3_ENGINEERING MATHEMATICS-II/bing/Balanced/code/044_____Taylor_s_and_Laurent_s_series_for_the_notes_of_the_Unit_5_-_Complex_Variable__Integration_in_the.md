### Taylor’s and Laurent’s series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ and $z_0$ are complex constants and $z$ is a complex variable.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ is the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients given by

$$a_n = \frac{1}{2\pi i} \int_C \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a simple closed contour in the annulus that encloses $z_0$.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has a singularity at $z_0$.

- A Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$. The principal part has a finite number of terms and the analytic part is a Taylor series.

- The principal part of a Laurent series can be used to classify the type of singularity of a function at $z_0$. If the principal part is zero, then the function has a **removable singularity** at $z_0$. If the principal part has a finite number of non-zero terms, then the function has a **pole** of order equal to the highest power of $(z-z_0)$ in the principal part. If the principal part has an infinite number of non-zero terms, then the function has an **essential singularity** at $z_0$.