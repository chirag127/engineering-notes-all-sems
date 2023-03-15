# Milne's Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function of a complex variable from its real or imaginary part, when the latter is given as an analytic expression in terms of the real and imaginary parts of the variable .
- An analytic function of a complex variable is a function that is differentiable at every point in its domain, and satisfies the Cauchy-Riemann equations.
- The method is based on the following theorem :

> If $f(z) = u(x,y) + iv(x,y)$ is an analytic function in a domain $D$, and $g(z) = \overline{f(\overline{z})} = u(x,-y) - iv(x,-y)$ is the conjugate function of $f(z)$, then $g(z)$ is also analytic in $D$, and $f(z) + g(z) = 2u(x,y)$ is a real-valued harmonic function in $D$.

- The theorem implies that if we know the real part $u(x,y)$ of an analytic function $f(z)$, we can find the imaginary part $v(x,y)$ by using the conjugate function $g(z)$ and the Cauchy-Riemann equations .
- The steps of the method are as follows :

  1. Given the real part $u(x,y)$ of an analytic function $f(z)$, find the conjugate function $g(z) = \overline{f(\overline{z})}$ by replacing $y$ with $-y$ in $u(x,y)$.
  2. Write $g(z) = U(x,y) + iV(x,y)$, where $U(x,y) = u(x,-y)$ and $V(x,y) = -v(x,-y)$.
  3. Apply the Cauchy-Riemann equations to $g(z)$, i.e., $U_x = V_y$ and $U_y = -V_x$.
  4. Solve the resulting partial differential equations for $V(x,y)$, using the boundary condition $V(x,0) = 0$.
  5. Find the imaginary part $v(x,y)$ of $f(z)$ by using the relation $v(x,y) = -V(x,-y)$.
  6. Write the analytic function $f(z) = u(x,y) + iv(x,y)$.

- The method can also be applied to find the real part $u(x,y)$ of an analytic function $f(z)$ from its imaginary part $v(x,y)$, by using the relation $u(x,y) = U(x,-y)$, where $U(x,y)$ is the real part of the conjugate function $g(z) = \overline{f(\overline{z})}$ .
- The method can be extended to find the analytic function $f(z)$ in a domain $D$ that contains a boundary curve $C$, by using the method of analytic continuation. The idea is to find the analytic function $f(z)$ in a larger domain $D'$ that does not contain $C$, and then restrict it to $D$.
- The method can also be used to find the complex potential of a fluid flow around a solid boundary, by adding the conjugate function of the complex potential of the free flow to the complex potential of the free flow .