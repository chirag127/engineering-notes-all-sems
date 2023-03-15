## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The curve or contour can be either closed or open, and can be oriented in a clockwise or counterclockwise direction.
- The basic formula for complex integration is:

$$\int_C f(z) dz = \int_a^b f[z(t)] z'(t) dt$$

where $C$ is the curve or contour, $f(z)$ is the complex function, $z(t)$ is the parametric representation of the curve, and $a$ and $b$ are the limits of the parameter.

- There are some important properties and theorems of complex integration, such as:

  - Linearity: $\int_C (\alpha f(z) + \beta g(z)) dz = \alpha \int_C f(z) dz + \beta \int_C g(z) dz$ for any constants $\alpha$ and $\beta$.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$ if $C$ is the union of two curves $C_1$ and $C_2$ that do not overlap except at their endpoints.
  - Independence of path: $\int_C f(z) dz$ is the same for any curve $C$ that connects two fixed points $z_1$ and $z_2$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Cauchy's integral theorem: $\int_C f(z) dz = 0$ for any closed curve $C$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Cauchy's integral formula: $f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$ for any point $z_0$ inside a closed curve $C$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Residue theorem: $\int_C f(z) dz = 2\pi i \sum_{k=1}^n Res(f, z_k)$ for any closed curve $C$ that encloses $n$ isolated singularities $z_1, z_2, ..., z_n$ of $f(z)$ in a domain $D$ if $f(z)$ is analytic in $D$ except at those singularities. The residue of $f(z)$ at $z_k$ is denoted by $Res(f, z_k)$ and can be computed by various methods depending on the type of singularity.