### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex function can be written as $w(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ is the complex variable, $w = u + iv$ is the complex value, and $u$ and $v$ are real functions of $x$ and $y$.
- A complex function is said to be differentiable at a point $z_0$ if the limit $\lim_{\Delta z \to 0} \frac{w(z_0 + \Delta z) - w(z_0)}{\Delta z}$ exists and is independent of the direction of $\Delta z$.
- A complex function that is differentiable at every point in a domain is called holomorphic or analytic in that domain.
- A holomorphic function satisfies the Cauchy-Riemann equations, which relate the partial derivatives of $u$ and $v$ as follows: $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = - \frac{\partial v}{\partial x}$.
- A holomorphic function has many remarkable properties, such as the following:
  - It is infinitely differentiable and has a convergent power series expansion around any point in its domain.
  - It satisfies the maximum modulus principle, which states that the modulus of a holomorphic function cannot have a local maximum in its domain.
  - It satisfies the Cauchy integral formula, which relates the value of a holomorphic function at a point to its values along a closed contour enclosing that point.
  - It satisfies the residue theorem, which relates the integral of a holomorphic function along a closed contour to the sum of its residues at the isolated singularities inside the contour.
  - It satisfies the open mapping theorem, which states that a non-constant holomorphic function maps open sets to open sets.
  - It satisfies the identity theorem, which states that if two holomorphic functions agree on a set that has a limit point in their domain, then they agree on their entire domain.
- A function of several complex variables is a function that maps $n$-tuples of complex numbers to complex numbers, where $n > 1$.
- A function of several complex variables can be written as $w(z_1, z_2, \dots, z_n) = u(x_1, y_1, x_2, y_2, \dots, x_n, y_n) + iv(x_1, y_1, x_2, y_2, \dots, x_n, y_n)$, where $z_k = x_k + iy_k$ are the complex variables, $w = u + iv$ is the complex value, and $u$ and $v$ are real functions of $2n$ real variables.
- A function of several complex variables is said to be holomorphic at a point $(z_1, z_2, \dots, z_n)$ if it is differentiable with respect to each variable $z_k$ while holding the other variables fixed, and the partial derivatives are continuous and satisfy the Cauchy-Riemann equations in each variable.
- A function of several complex variables that is holomorphic at every point in a domain is called holomorphic or analytic in that domain.
- A holomorphic function of several complex variables has some of the properties of a holomorphic function of one complex variable, such as the power series expansion, the Cauchy integral formula, and the residue theorem, but not all of them, such as the maximum modulus principle, the open mapping theorem, and the identity theorem.