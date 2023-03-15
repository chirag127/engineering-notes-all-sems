Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on Taylor's and Laurent's series for complex variable integration.

### Taylor's and Laurent's series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a complex number.

- A power series with non-negative power terms is called a **Taylor series**. It can be used to represent a complex function $f(z)$ that is **analytic** (differentiable) in a disk around $z_0$.

- The Taylor series of $f(z)$ at $z_0$ is given by

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ is the $n$-th derivative of $f(z)$ at $z_0$.

- The Taylor series converges to $f(z)$ in the largest disk centered at $z_0$ that does not contain any **singularities** (points where $f(z)$ is not analytic) of $f(z)$.

- A power series with both positive and negative power terms is called a **Laurent series**. It can be used to represent a complex function $f(z)$ that is analytic in an **annulus** (ring-shaped region) around $z_0$.

- The Laurent series of $f(z)$ at $z_0$ is given by

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients that can be computed by the formula

$$a_n = \frac{1}{2\pi i} \int_C \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a positively oriented simple closed contour in the annulus that encloses $z_0$.

- The Laurent series converges to $f(z)$ in the largest annulus centered at $z_0$ that does not contain any singularities of $f(z)$.

- The Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$.

- The principal part of the Laurent series is also called the **singular part** because it reveals the nature of the singularity at $z_0$. The analytic part of the Laurent series is also called the **regular part** because it coincides with the Taylor series of $f(z)$ in a disk around $z_0$.

- The Laurent series is useful for studying the **residues** of complex functions, which are the coefficients of the $-1$ power term in the Laurent series. The residues can be used to evaluate complex integrals using the **residue theorem**.