# Milne's Thompson Method for Complex Variable Differentiation

- Milne's Thompson method is a technique to find an analytic function $f(z) = u(x,y) + iv(x,y)$ from its real or imaginary part, when the latter is given as an analytic expression in terms of $x$ and $y$ .
- The method is based on the Cauchy-Riemann equations, which relate the partial derivatives of $u$ and $v$ as follows:
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$
- The method consists of three steps:
  - Step 1: Replace $x$ and $y$ by $\frac{z+\bar{z}}{2}$ and $\frac{z-\bar{z}}{2i}$ respectively in the given expression of $u$ or $v$, and simplify it to obtain a function of $z$ and $\bar{z}$, say $g(z,\bar{z})$.
  - Step 2: Differentiate $g(z,\bar{z})$ with respect to $\bar{z}$ and equate it to zero, since $f(z)$ is independent of $\bar{z}$. Solve for $\bar{z}$ in terms of $z$, say $\bar{z} = h(z)$.
  - Step 3: Substitute $\bar{z} = h(z)$ in $g(z,\bar{z})$ and simplify it to obtain a function of $z$ only, say $f(z)$. This is the analytic function that corresponds to the given real or imaginary part.
- The method can be applied to three cases, depending on whether the given expression of $u$ or $v$ is a polynomial, a rational function, or an irrational function of $x$ and $y$ .
  - Case 1: If the given expression is a polynomial of $x$ and $y$, then step 2 will result in a polynomial equation in $\bar{z}$, which can be solved by using the fundamental theorem of algebra or by factorization.
  - Case 2: If the given expression is a rational function of $x$ and $y$, then step 2 will result in a rational equation in $\bar{z}$, which can be solved by using the method of partial fractions or by cross-multiplication.
  - Case 3: If the given expression is an irrational function of $x$ and $y$, then step 2 will result in an irrational equation in $\bar{z}$, which can be solved by using the method of squaring or by substitution.
- The method can also be used to find the complex potential of a flow with no rigid boundaries, no singularities inside $|z|=a$, when introducing the solid cylinder $|z|=a$, by using the formula:
$$
w(z) = f(z) + \bar{f}\left(\frac{a^2}{z}\right)
$$
for $|z| \geq a$, where $f(z)$ is the complex potential of the original flow.