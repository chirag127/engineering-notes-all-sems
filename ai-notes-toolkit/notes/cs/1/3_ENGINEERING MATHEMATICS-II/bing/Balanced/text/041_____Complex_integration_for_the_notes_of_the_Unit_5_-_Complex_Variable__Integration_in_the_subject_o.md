### Complex integration for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- Complex integration is an intuitive extension of real integration. It involves integrating a complex-valued function along a path in the complex plane.
- A complex-valued function of a real variable, such as $f(t) = u(t) + iv(t)$, can be integrated as a vector function, by integrating its real and imaginary parts separately.
- A complex-valued function of a complex variable, such as $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$, can be integrated along a curve $C$ in the complex plane, by using the parametric representation of the curve and the chain rule.
- The complex integral of $f(z)$ along $C$ is denoted by $\int_C f(z) dz$, and it is defined as the limit of the Riemann sums of $f(z)$ over the subintervals of $C$.
- The complex integral of $f(z)$ along $C$ depends on the path $C$, not just the endpoints of $C$. However, if $f(z)$ is analytic in a simply connected domain $D$, then the complex integral of $f(z)$ along any closed curve in $D$ is zero.
- The Cauchy integral theorem states that if $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a simple closed curve in $D$, then the complex integral of $f(z)$ along $C$ is zero.
- The Cauchy integral formula states that if $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a simple closed curve in $D$ that encloses a point $z_0$, then $f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$.
- The Cauchy integral formula can be used to find the derivatives of analytic functions, as well as to evaluate complex integrals that involve rational functions or trigonometric functions.
- The residue theorem states that if $f(z)$ is analytic in a simply connected domain $D$, except for a finite number of isolated singularities, and $C$ is a simple closed curve in $D$ that encloses all the singularities, then $\int_C f(z) dz = 2\pi i \sum_{k=1}^n Res(f, z_k)$, where $Res(f, z_k)$ is the residue of $f(z)$ at the singularity $z_k$.
- The residue theorem can be used to evaluate complex integrals that involve functions with poles, branch points, or essential singularities.
- The principal value of a complex integral is defined as the limit of the integral over a symmetric interval around the singularity, as the interval shrinks to zero.
- The principal value of a complex integral can be used to deal with integrals that have singularities on the real axis.