## Unit 5 - Complex Variable –Integration

- Complex variable integration is the process of finding the value of a complex function along a curve in the complex plane.
- The curve can be either closed or open, and can be defined by a parametric equation or a function of a real variable.
- The basic formula for complex variable integration is:

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

where $C$ is the curve, $f(z)$ is the complex function, $z(t)$ is the parametric equation of the curve, and $z'(t)$ is the derivative of $z(t)$ with respect to $t$.

- Some properties of complex variable integration are:

  - Linearity: $\int_C (af(z) + bg(z)) dz = a \int_C f(z) dz + b \int_C g(z) dz$ for any constants $a$ and $b$.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$ if $C$ is the union of two curves $C_1$ and $C_2$ that do not overlap except at their endpoints.
  - Independence of path: $\int_C f(z) dz$ is the same for any curve $C$ that connects two fixed points $z_1$ and $z_2$ in a domain $D$ where $f(z)$ is analytic (i.e., has a derivative at every point).
  - Cauchy's integral theorem: $\int_C f(z) dz = 0$ for any closed curve $C$ in a domain $D$ where $f(z)$ is analytic.
  - Cauchy's integral formula: $\int_C \frac{f(z)}{z-z_0} dz = 2\pi i f(z_0)$ for any closed curve $C$ that encloses a point $z_0$ in a domain $D$ where $f(z)$ is analytic.
  - Residue theorem: $\int_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$ for any closed curve $C$ that encloses $n$ isolated singularities $z_1, z_2, ..., z_n$ of $f(z)$ in a domain $D$ where $f(z)$ is analytic except at those points. The residue of $f(z)$ at $z_k$ is denoted by $\text{Res}(f, z_k)$ and is defined as the coefficient of $\frac{1}{z-z_k}$ in the Laurent series expansion of $f(z)$ around $z_k$.

- Some applications of complex variable integration are:

  - Evaluating real integrals using contour integration and the residue theorem, such as $\int_{-\infty}^{\infty} \frac{\cos x}{x^2 + a^2} dx = \frac{\pi}{a} e^{-a}$ for any positive constant $a$.
  - Finding the inverse Laplace transform of a function using the Bromwich integral, such as $\mathcal{L}^{-1}\left\{\frac{1}{s^2 + a^2}\right\} = \frac{1}{a} \sin at$ for any positive constant $a$.
  - Solving boundary value problems in potential theory and fluid mechanics using the method of conformal mapping, such as finding the potential function and the stream function for the flow around a cylinder.