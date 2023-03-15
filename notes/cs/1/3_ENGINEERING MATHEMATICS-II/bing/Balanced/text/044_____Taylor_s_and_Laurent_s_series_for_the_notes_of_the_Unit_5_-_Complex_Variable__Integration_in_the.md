### Taylor’s and Laurent’s series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ and $z_0$ are complex constants and $z$ is a complex variable.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients given by

$$a_n = \frac{1}{2\pi i} \int_C \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a simple closed contour in the annulus that encloses $z_0$.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has a singularity at $z_0$.

- A Laurent series can be divided into two parts: the **principal part**, which contains the negative power terms, and the **analytic part**, which contains the non-negative power terms. The principal part can be written as

$$\sum_{n=1}^{\infty} a_{-n} (z-z_0)^{-n}$$

and the analytic part can be written as

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

- The principal part of a Laurent series is also called the **residue series**, because the coefficient $a_{-1}$ is equal to the **residue** of $f(z)$ at $z_0$, denoted by $\text{Res}(f,z_0)$. The residue is a useful quantity for evaluating complex integrals using the **residue theorem**.