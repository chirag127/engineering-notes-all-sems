### Milne's Thompson Method

- Milne's Thompson method is a method for finding a holomorphic function whose real or imaginary part is given.
- A holomorphic function is a complex-valued function that is differentiable at every point in its domain.
- A holomorphic function can be written as $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ is a complex variable, and $u$ and $v$ are real-valued functions of $x$ and $y$.
- The real part $u$ and the imaginary part $v$ of a holomorphic function satisfy the Cauchy-Riemann equations: $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$.
- The Milne's Thompson method consists of the following steps:

  1. Given the real part $u(x,y)$ or the imaginary part $v(x,y)$ of a holomorphic function, find the other part by integrating the Cauchy-Riemann equations, using an arbitrary constant of integration.
  2. Substitute $x = \frac{z + \bar{z}}{2}$ and $y = \frac{z - \bar{z}}{2i}$ in the expressions of $u$ and $v$, where $\bar{z}$ is the complex conjugate of $z$.
  3. Eliminate $\bar{z}$ from the expressions of $u$ and $v$ by using the identity $\bar{z} = \frac{2u - z}{2iv}$, which follows from $u = \frac{z + \bar{z}}{2}$ and $v = \frac{z - \bar{z}}{2i}$.
  4. The resulting expression of $u + iv$ is the holomorphic function $f(z)$.

- Example: Find the holomorphic function $f(z)$ whose real part is $u(x,y) = x^2 - y^2$.

  1. To find the imaginary part $v(x,y)$, we integrate the Cauchy-Riemann equations: $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$. We get: $v(x,y) = 2xy + c$, where $c$ is an arbitrary constant.
  2. Substituting $x = \frac{z + \bar{z}}{2}$ and $y = \frac{z - \bar{z}}{2i}$, we get: $u(z,\bar{z}) = \frac{z^2 + \bar{z}^2}{4}$ and $v(z,\bar{z}) = \frac{z^2 - \bar{z}^2}{4i} + c$.
  3. Eliminating $\bar{z}$ by using the identity $\bar{z} = \frac{2u - z}{2iv}$, we get: $v(z) = \frac{z^2 - (2u - z)^2}{4i(2iv)} + c = \frac{z^2 - 4u^2 + 4uz}{-16v^2} + c = \frac{z^2 - (z^2 + \bar{z}^2) + 4z\frac{z + \bar{z}}{2}}{-16(\frac{z - \bar{z}}{2i})^2} + c = \frac{z^2 - \bar{z}^2}{4i} + c$.
  4. The holomorphic function is $f(z) = u(z) + iv(z) = \frac{z^2 + \bar{z}^2}{4} + i(\frac{z^2 - \bar{z}^2}{4i} + c) = \frac{z^2}{2} + c$.