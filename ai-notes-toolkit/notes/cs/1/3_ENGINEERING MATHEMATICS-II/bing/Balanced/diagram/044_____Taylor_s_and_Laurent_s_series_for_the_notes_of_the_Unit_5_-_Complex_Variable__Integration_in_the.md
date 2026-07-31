### Taylor’s and Laurent’s series

- A power series is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ and $z_0$ are complex constants and $z$ is a complex variable.

- A power series with non-negative power terms is called a **Taylor series**. It can be used to represent a complex function that is analytic (has a derivative) at a point and in a neighborhood around that point.

- A Taylor series of a function $f(z)$ about a point $z_0$ is given by

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. It can be used to represent a complex function that is analytic in an annular region (a ring-shaped region) around a point, but not necessarily at that point.

- A Laurent series of a function $f(z)$ about a point $z_0$ is given by

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients that can be obtained by integrating $f(z)$ along a closed contour in the annular region.

- A Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$.

- The principal part of a Laurent series is also called the **singular part** because it reveals the nature of the singularity (a point where the function is not analytic) at $z_0$. The analytic part of a Laurent series is also called the **regular part** because it coincides with the Taylor series of the function in the annular region.

- The Laurent series is unique for a given function and a given annular region. It converges absolutely and uniformly in the annular region.

- The Laurent series is useful for studying the properties of complex functions, such as residues, poles, zeros, and integrals. It also helps to work around the singularities of complex functions.