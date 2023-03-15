## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The curve or contour can be either closed or open, and can be oriented in either direction.
- The basic formula for complex integration is:

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

where $C$ is the curve or contour, $f(z)$ is the complex function, $z(t)$ is the parametric representation of the curve, and $z'(t)$ is the derivative of $z(t)$ with respect to $t$.

- Some properties of complex integration are:

  - Linearity: $\int_C (af(z) + bg(z)) dz = a \int_C f(z) dz + b \int_C g(z) dz$, where $a$ and $b$ are constants.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$, where $C_1$ and $C_2$ are two subcontours of $C$.
  - Independence of path: $\int_C f(z) dz$ is the same for any two curves $C_1$ and $C_2$ that have the same endpoints and lie in the same domain where $f(z)$ is analytic (i.e., has a derivative at every point).
  - Cauchy's integral theorem: If $f(z)$ is analytic in a simply connected domain $D$, then $\int_C f(z) dz = 0$ for any closed contour $C$ in $D$.
  - Cauchy's integral formula: If $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a positively oriented simple closed contour in $D$ that encloses a point $z_0$, then $f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$.
  - Residue theorem: If $f(z)$ is analytic in a simply connected domain $D$ except for a finite number of isolated singularities, and $C$ is a positively oriented simple closed contour in $D$ that encloses all the singularities, then $\int_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$, where $\text{Res}(f, z_k)$ is the residue of $f(z)$ at the singularity $z_k$.

- Some applications of complex integration are:

  - Evaluating real integrals using contour integration, such as $\int_{-\infty}^{\infty} \frac{p(x)}{q(x)} dx$, where $p(x)$ and $q(x)$ are polynomials and $q(x)$ has no real roots.
  - Solving boundary value problems in potential theory, such as Laplace's equation, using the method of conformal mapping, which transforms a complex domain into a simpler one where the solution can be found easily.
  - Computing Fourier and Laplace transforms of complex functions using contour integration, such as $\mathcal{F}(f)(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$ and $\mathcal{L}(f)(s) = \int_{0}^{\infty} f(t) e^{-st} dt$, where $f(t)$ is a complex function of a real variable $t$.
  - Finding the zeros and poles of complex functions using the argument principle, which relates the change in the argument of a function along a contour to the number of zeros and poles inside the contour.
  - Studying the asymptotic behavior of complex functions using the method of steepest descent, which approximates the integral of a function along a contour by the value of the function at the saddle point of the contour.