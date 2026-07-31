### Analytic functions

- A function $f(z)$ of a complex variable $z = x + iy$ is **analytic** if it has a complex derivative $f'(z)$ at every point in its domain.
- A complex derivative $f'(z)$ is defined as the limit of the difference quotient $\frac{f(z+h)-f(z)}{h}$ as $h \to 0$, where $h$ is a complex number.
- A function $f(z)$ is analytic if and only if it is **holomorphic**, i.e., it satisfies the **Cauchy-Riemann equations**:
  - $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$, where $f(z) = u(x,y) + iv(x,y)$.
- A function $f(z)$ is analytic if and only if its **Taylor series** about $z_0$ converges to the function in some neighborhood for every $z_0$ in its domain:
  - $f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$, where $f^{(n)}(z_0)$ is the $n$-th derivative of $f(z)$ at $z_0$.
- Analytic functions have many remarkable properties that do not generally hold for real differentiable functions, such as:
  - **Identity theorem**: If two analytic functions $f(z)$ and $g(z)$ agree on a set of points that has a limit point, then they are equal everywhere in their common domain.
  - **Maximum modulus principle**: If $f(z)$ is a non-constant analytic function in a domain $D$, then $|f(z)|$ attains its maximum value only on the boundary of $D$.
  - **Liouville's theorem**: If $f(z)$ is a bounded entire function (i.e., analytic in the whole complex plane), then $f(z)$ is constant.
  - **Fundamental theorem of algebra**: If $p(z)$ is a non-constant polynomial with complex coefficients, then $p(z)$ has at least one complex root.