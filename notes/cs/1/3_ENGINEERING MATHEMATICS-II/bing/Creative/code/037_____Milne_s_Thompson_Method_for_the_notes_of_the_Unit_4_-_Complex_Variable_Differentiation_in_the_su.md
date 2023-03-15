### Milne’s Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function $f(z)$ from its real or imaginary part, when the latter is given as an analytic expression in terms of $x$ and $y$.
- An analytic function is a complex function that is differentiable at every point in its domain.
- The method is based on the Cauchy-Riemann equations, which relate the partial derivatives of the real and imaginary parts of an analytic function.
- The method consists of the following steps :
  - Step 1: Write the given real or imaginary part of $f(z)$ as $u(x,y)$ or $v(x,y)$, respectively.
  - Step 2: Find the other part of $f(z)$ by using the Cauchy-Riemann equations: $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
  - Step 3: Integrate the partial derivatives to obtain $u(x,y)$ or $v(x,y)$, up to an arbitrary constant of integration.
  - Step 4: Eliminate the constant of integration by using the boundary condition, if given, or by setting it to zero.
  - Step 5: Write the analytic function as $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$.
- The method can be applied to three cases, depending on the form of the given real or imaginary part:
  - Case I: The given part is a function of $x$ or $y$ only, such as $u(x,y) = x^2$ or $v(x,y) = y^3$.
  - Case II: The given part is a function of $x + iy$ or $x - iy$, such as $u(x,y) = e^{x+iy}$ or $v(x,y) = \sin(x-iy)$.
  - Case III: The given part is a function of $x^2 + y^2$ or $x^2 - y^2$, such as $u(x,y) = \log(x^2 + y^2)$ or $v(x,y) = \sqrt{x^2 - y^2}$.
- The method can be used to solve various problems in complex analysis, such as finding the complex potential of a flow, the conformal mapping of a region, or the harmonic conjugate of a function .