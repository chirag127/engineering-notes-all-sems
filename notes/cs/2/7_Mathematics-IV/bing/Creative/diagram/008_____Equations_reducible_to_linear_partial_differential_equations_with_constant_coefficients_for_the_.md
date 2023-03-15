### Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) with constant coefficients is an equation of the form
$$
a_0 u + a_1 u_x + a_2 u_y + a_3 u_{xx} + a_4 u_{xy} + a_5 u_{yy} + \cdots = f(x,y)
$$
where $a_0, a_1, \ldots$ are constants and $u$ is an unknown function of $x$ and $y$.
- A PDE is said to be reducible to a linear PDE with constant coefficients if it can be transformed into such an equation by a change of variables or by some other method.
- Some examples of equations reducible to linear PDEs with constant coefficients are:

  - The Lagrange equation
  $$
  P(x,y) u_x + Q(x,y) u_y = R(x,y)
  $$
  where $P, Q, R$ are given functions of $x$ and $y$. This equation can be reduced to a linear PDE with constant coefficients by the method of characteristics, which involves finding a pair of functions $\xi(x,y)$ and $\eta(x,y)$ such that
  $$
  P \frac{\partial \xi}{\partial x} + Q \frac{\partial \xi}{\partial y} = 0 \quad \text{and} \quad P \frac{\partial \eta}{\partial x} + Q \frac{\partial \eta}{\partial y} = 1
  $$
  and then using the substitution $u(x,y) = v(\xi, \eta)$, where $v$ is a new unknown function. The equation then becomes
  $$
  v_\eta = R(x,y)
  $$
  which is a linear PDE with constant coefficients.

  - The Monge-Ampère equation
  $$
  u_{xx} u_{yy} - u_{xy}^2 = F(x,y,u,u_x,u_y)
  $$
  where $F$ is a given function of $x, y, u, u_x, u_y$. This equation can be reduced to a linear PDE with constant coefficients by the Legendre transformation, which involves finding a pair of functions $p(x,y,u)$ and $q(x,y,u)$ such that
  $$
  p = u_x \quad \text{and} \quad q = u_y
  $$
  and then using the substitution $u(x,y) = w(p,q)$, where $w$ is a new unknown function. The equation then becomes
  $$
  w_{pp} w_{qq} - w_{pq}^2 = F(x,y,w,p,q)
  $$
  which is a linear PDE with constant coefficients.

  - The Cauchy-Riemann equations
  $$
  u_x = v_y \quad \text{and} \quad u_y = -v_x
  $$
  where $u$ and $v$ are unknown functions of $x$ and $y$. These equations can be reduced to a linear PDE with constant coefficients by the complex variable substitution $u(x,y) + i v(x,y) = w(z)$, where $w$ is a new unknown function of the complex variable $z = x + i y$. The equations then become
  $$
  w_z = 0
  $$
  which is a linear PDE with constant coefficients.