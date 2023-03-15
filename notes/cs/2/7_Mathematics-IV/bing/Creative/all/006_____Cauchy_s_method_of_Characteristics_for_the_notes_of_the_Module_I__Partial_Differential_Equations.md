# Cauchy's method of characteristics

- Cauchy's method of characteristics is a technique for solving partial differential equations (PDEs) of the form
$$
a(x,y,u)u_x + b(x,y,u)u_y = c(x,y,u)
$$
subject to a boundary condition (BC) of the form
$$
u(x,y) = f(x,y) \quad \text{on} \quad \Gamma
$$
where $\Gamma$ is a curve in the $xy$-plane.
- The method is based on geometric considerations and transforms the PDE into a system of ordinary differential equations (ODEs) along certain curves called characteristics.
- The characteristics are curves in the $xyz$-space that satisfy the following system of ODEs:
$$
\frac{dx}{a(x,y,u)} = \frac{dy}{b(x,y,u)} = \frac{du}{c(x,y,u)}
$$
- The characteristics can be parametrized by a parameter $s$ and written as
$$
x = x(s), \quad y = y(s), \quad u = u(s)
$$
- The method consists of the following steps:

  1. Find the characteristic equations by solving the system of ODEs for $x$, $y$, and $u$ in terms of $s$.
  2. Find the initial curve $\Gamma$ in the $s$-coordinate by substituting the boundary condition into the characteristic equations.
  3. Eliminate the parameter $s$ from the characteristic equations and the initial curve to obtain the solution $u(x,y)$ in terms of $x$ and $y$.
  4. Check the domain of validity of the solution and the compatibility condition for the boundary condition.