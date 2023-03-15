## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The curve or contour can be either closed or open, and can be oriented in either direction.
- The basic formula for complex integration is:

$$\int_C f(z) dz = \int_a^b f[z(t)] z'(t) dt$$

where $C$ is the curve or contour, $f(z)$ is the complex function, $z(t)$ is the parametric representation of $C$, and $z'(t)$ is the derivative of $z(t)$ with respect to $t$.

- Some properties of complex integration are:

  - Linearity: $\int_C (\alpha f(z) + \beta g(z)) dz = \alpha \int_C f(z) dz + \beta \int_C g(z) dz$ for any constants $\alpha$ and $\beta$.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$ if $C$ is the union of two non-overlapping curves $C_1$ and $C_2$.
  - Independence of path: $\int_C f(z) dz$ is the same for any curve $C$ that connects two fixed points $z_1$ and $z_2$ if $f(z)$ is analytic in the region enclosed by $C$.
  - Cauchy's integral theorem: $\int_C f(z) dz = 0$ if $C$ is a closed curve and $f(z)$ is analytic in the region enclosed by $C$.
  - Cauchy's integral formula: $\int_C \frac{f(z)}{z-z_0} dz = 2\pi i f(z_0)$ if $C$ is a closed curve that encloses a point $z_0$ and $f(z)$ is analytic in the region enclosed by $C$.

- Some applications of complex integration are:

  - Evaluating real integrals using contour integration and residue theorem.
  - Finding the Laurent series expansion of a complex function using Cauchy's integral formula.
  - Solving boundary value problems in potential theory and fluid mechanics using conformal mapping and Green's theorem.
  - Computing the inverse Laplace transform of a complex function using Bromwich integral and residue theorem.