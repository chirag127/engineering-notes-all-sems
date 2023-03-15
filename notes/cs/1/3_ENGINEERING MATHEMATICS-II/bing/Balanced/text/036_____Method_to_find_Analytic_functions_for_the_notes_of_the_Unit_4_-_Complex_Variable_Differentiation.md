### Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is said to be **analytic** in a region of the complex plane if it has a derivative at each point of the region and if it is single valued.
- A function of a complex variable is also called **holomorphic** or **complex analytic** if it is analytic in the whole complex plane or in an open subset of it .
- A function of a complex variable is analytic if and only if it satisfies the **Cauchy-Riemann equations** in the region of analyticity .
- The Cauchy-Riemann equations are a pair of partial differential equations that relate the real and imaginary parts of a complex function. If $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ and $u$ and $v$ are real functions, then the Cauchy-Riemann equations are:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

- A function of a complex variable is analytic if and only if it is **conformal**, meaning that it preserves the angles between curves at each point of the region of analyticity .
- A function of a complex variable is analytic if and only if it has a **power series expansion** in a neighborhood of each point of the region of analyticity .
- A power series expansion of a complex function is a series of the form:

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a fixed point in the region of analyticity.

- A function of a complex variable is analytic if and only if it satisfies the **Cauchy integral formula**, which relates the value of the function at a point to the values of the function on a closed contour around the point .
- The Cauchy integral formula is:

$$f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} dz$$

where $C$ is a simple closed curve that encloses $z_0$ and is oriented counterclockwise, and $f(z)$ is analytic inside and on $C$.

- A function of a complex variable is analytic if and only if it satisfies the **Morera's theorem**, which states that if the integral of the function along any closed curve in a region is zero, then the function is analytic in that region .
- The Morera's theorem is:

$$\oint_C f(z) dz = 0 \implies f(z) \text{ is analytic in } R$$

where $C$ is any simple closed curve in a region $R$ and $f(z)$ is continuous in $R$.