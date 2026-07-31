### Milne’s Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function $f(z) = u(x,y) + iv(x,y)$ in a region $R$ of the complex plane, if either the real part $u(x,y)$ or the imaginary part $v(x,y)$ is known as an analytic expression in terms of $x$ and $y$ .
- The method is based on the Cauchy-Riemann equations, which relate the partial derivatives of $u$ and $v$ as follows:
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$
- The method consists of three steps:
  - Step 1: Find the harmonic conjugate of the given function, i.e., the function that satisfies the Cauchy-Riemann equations with the given function. For example, if $u(x,y)$ is given, find $v(x,y)$ such that $u$ and $v$ are harmonic conjugates.
  - Step 2: Express $u$ and $v$ in terms of $z$ and $\bar{z}$, where $z = x + iy$ and $\bar{z} = x - iy$. This can be done by using the identities:
  $$
  x = \frac{z + \bar{z}}{2}, \quad y = \frac{z - \bar{z}}{2i}, \quad \frac{\partial}{\partial x} = \frac{1}{2}\left(\frac{\partial}{\partial z} + \frac{\partial}{\partial \bar{z}}\right), \quad \frac{\partial}{\partial y} = \frac{1}{2i}\left(\frac{\partial}{\partial z} - \frac{\partial}{\partial \bar{z}}\right)
  $$
  - Step 3: Eliminate $\bar{z}$ from the expressions of $u$ and $v$ by using the fact that $f(z)$ is analytic in $R$, which implies that $\frac{\partial f}{\partial \bar{z}} = 0$ in $R$. This gives $f(z) = u(z,\bar{z}) + iv(z,\bar{z})$ as a function of $z$ only.
- The method can be applied to different cases depending on the form of the given function:
  - Case I: The given function is a polynomial in $x$ and $y$. In this case, the harmonic conjugate can be found by integrating the Cauchy-Riemann equations and using the fact that the constant of integration must be a polynomial of the same degree as the given function.
  - Case II: The given function is a product of a polynomial and an exponential function in $x$ and $y$. In this case, the harmonic conjugate can be found by using the method of undetermined coefficients, i.e., assuming that the harmonic conjugate has the same form as the given function and solving for the coefficients by equating the partial derivatives.
  - Case III: The given function is a function of $x^2 + y^2$ and $x^2 - y^2$. In this case, the harmonic conjugate can be found by using the method of substitution, i.e., letting $r^2 = x^2 + y^2$ and $s^2 = x^2 - y^2$ and solving for the harmonic conjugate in terms of $r$ and $s$ by integrating the Cauchy-Riemann equations. Then, the expressions of $u$ and $v$ in terms of $z$ and $\bar{z}$ can be obtained by using the identities:
  $$
  r^2 = \frac{z\bar{z}}{2}, \quad s^2 = \frac{z^2 + \bar{z}^2}{4}, \quad \frac{\partial}{\partial r} = \frac{z}{2r}\frac{\partial}{\partial z} + \frac{\bar{z}}{2r}\frac{\partial}{\partial \bar{z}},