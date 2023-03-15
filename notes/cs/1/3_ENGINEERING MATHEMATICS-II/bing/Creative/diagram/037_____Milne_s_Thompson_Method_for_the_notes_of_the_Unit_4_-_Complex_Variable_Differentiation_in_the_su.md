### Milne's Thompson Method

Milne's Thompson method is a technique for finding an analytic function whose real or imaginary part is given. It is based on the following theorem:

> If $f(z) = u(x,y) + iv(x,y)$ is an analytic function in a domain $D$, then $u$ and $v$ satisfy the Cauchy-Riemann equations and Laplace's equation in $D$. Conversely, if $u$ and $v$ are harmonic functions in $D$ that satisfy the Cauchy-Riemann equations, then $f(z)$ is an analytic function in $D$.

The method consists of the following steps:

1. Given the real or imaginary part of $f(z)$, say $u(x,y)$, find the harmonic conjugate of $u$, say $v(x,y)$, by integrating the Cauchy-Riemann equations:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

2. Add a constant of integration to $v(x,y)$, if necessary, to make $f(z) = u(x,y) + iv(x,y)$ satisfy the given boundary conditions.

3. Express $f(z)$ in terms of $z = x + iy$ by using the following identities:

$$x = \frac{z + \bar{z}}{2} \quad \text{and} \quad y = \frac{z - \bar{z}}{2i}$$

4. Simplify the expression for $f(z)$ and check that it is indeed an analytic function in $D$.

Here are some examples of applying the Milne's Thompson method :

- Example 1: Find an analytic function $f(z)$ whose real part is $u(x,y) = x^2 - y^2$.

  - Solution: The harmonic conjugate of $u$ is $v(x,y) = 2xy + c$, where $c$ is a constant. Therefore, $f(z) = u(x,y) + iv(x,y) = x^2 - y^2 + i(2xy + c)$. Using the identities for $x$ and $y$, we get:

  $$f(z) = \frac{z^2 + \bar{z}^2}{2} + i\left(z^2 - \bar{z}^2 + 2c\right) = z^2 + ic$$

  - The constant $c$ can be chosen arbitrarily. The function $f(z) = z^2 + ic$ is analytic in the whole complex plane.

- Example 2: Find an analytic function $f(z)$ whose imaginary part is $v(x,y) = \sin x \cosh y$.

  - Solution: The harmonic conjugate of $v$ is $u(x,y) = -\cos x \sinh y + c$, where $c$ is a constant. Therefore, $f(z) = u(x,y) + iv(x,y) = -\cos x \sinh y + c + i\sin x \cosh y$. Using the identities for $x$ and $y$, we get:

  $$f(z) = -\frac{e^z + e^{-z}}{2} + c + i\frac{e^z - e^{-z}}{2} = -e^z + c + ie^z = (i-1)e^z + c$$

  - The constant $c$ can be chosen arbitrarily. The function $f(z) = (i-1)e^z + c$ is analytic in the whole complex plane.