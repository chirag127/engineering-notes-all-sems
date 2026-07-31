# Milne's Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function $f(z)$ from its real or imaginary part, when the latter is given as an analytic expression in terms of $x$ and $y$.
- The method is based on the following theorem :

> If $f(z) = u(x,y) + iv(x,y)$ is an analytic function in a domain $D$, then $\overline{f(\overline{z})} = u(x,-y) - iv(x,-y)$ is also an analytic function in $D$.

- The theorem implies that if we know $u(x,y)$, we can find $v(x,y)$ by the following steps:
  - Replace $y$ by $-y$ in $u(x,y)$ to get $u(x,-y)$.
  - Find an analytic function $g(z)$ such that $g(z) = u(x,-y) + iv(x,-y)$ in $D$.
  - Then $f(z) = u(x,y) + iv(x,y) = \overline{g(\overline{z})}$ in $D$.
- Similarly, if we know $v(x,y)$, we can find $u(x,y)$ by the following steps:
  - Replace $y$ by $-y$ in $v(x,y)$ to get $v(x,-y)$.
  - Find an analytic function $g(z)$ such that $g(z) = u(x,-y) + iv(x,-y)$ in $D$.
  - Then $f(z) = u(x,y) + iv(x,y) = g(z) - iv(x,-y)$ in $D$.
- The method can be applied to different cases depending on the form of $u(x,y)$ or $v(x,y)$. Some examples are :
  - Case I: $u(x,y)$ or $v(x,y)$ is a polynomial in $x$ and $y$.
  - Case II: $u(x,y)$ or $v(x,y)$ is a rational function in $x$ and $y$.
  - Case III: $u(x,y)$ or $v(x,y)$ is a function of $x^2 + y^2$ and $x^2 - y^2$.
  - Case IV: $u(x,y)$ or $v(x,y)$ is a function of $x^2 + y^2$ and $xy$.
  - Case V: $u(x,y)$ or $v(x,y)$ is a function of $e^{x+iy}$ and $e^{x-iy}$.
- The method can also be used to find the complex potential of a flow with no rigid boundaries, no singularities inside $|z|=a$, when introducing the solid cylinder $|z|=a$, by the formula:

$$w(z) = f(z) + \overline{f\left(\frac{a^2}{z}\right)}$$

for $|z| \geq a$.