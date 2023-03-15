# Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

- where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The general solution of such an equation consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$.

- The particular integral is a particular solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$.

- To find the complementary function, we use the method of characteristic equation, which is similar to the method used for ordinary differential equations.

- We assume a solution of the form $u = e^{rx}$ and substitute it into the homogeneous equation. We get:

$$
a_0 r^n e^{rx} + a_1 r^{n-1} e^{rx} + \cdots + a_n e^{rx} = 0
$$

- Dividing by $e^{rx}$, we obtain the characteristic equation:

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

- The roots of this equation are called the characteristic roots, and they determine the form of the complementary function.

- Depending on the nature and multiplicity of the roots, the complementary function may have different forms. Some possible cases are:

  - If the characteristic equation has $n$ distinct real roots $r_1, r_2, \ldots, r_n$, then the complementary function is:

  $$
  u_c = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
  $$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants.

  - If the characteristic equation has a repeated real root $r$ of multiplicity $m$, then the complementary function is:

  $$
  u_c = (c_1 + c_2 x + \cdots + c_m x^{m-1}) e^{rx}
  $$

  where $c_1, c_2, \ldots, c_m$ are arbitrary constants.

  - If the characteristic equation has a pair of complex conjugate roots $r = \alpha \pm i \beta$, then the complementary function is:

  $$
  u_c = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)
  $$

  where $c_1$ and $c_2$ are arbitrary constants.

- To find the particular integral, we use the method of undetermined coefficients, which is also similar to the method used for ordinary differential equations.

- We assume a solution of the form $u_p = A g(x)$, where $A$ is an unknown constant and $g(x)$ is a function that has the same form as $f(x)$.

- We substitute $u_p$ into the non-homogeneous equation and solve for $A$.

- The particular integral may have different forms depending on the form of $f(x)$. Some possible cases are:

  - If $f(x) = e^{kx}$, where $k$ is a constant, then we assume $u_p = A e^{kx}$ and solve for $A$.

  - If $f(x) = a \cos kx + b \sin kx$, where $a, b, k$ are constants, then we assume $u_p = A \cos kx + B \sin kx$ and solve for $A$ and $B$.

  - If $f(x) = P(x)$, where $P(x)$ is a polynomial of degree $m$, then we assume $u_p = Q(x)$, where $Q(x)$ is a polynomial of degree $m$ and solve for the coefficients of $Q(x)$.

- The general solution of the non-homogeneous equation is then given by:

$$
u = u_c + u_p
$$

- where $u_c$ is