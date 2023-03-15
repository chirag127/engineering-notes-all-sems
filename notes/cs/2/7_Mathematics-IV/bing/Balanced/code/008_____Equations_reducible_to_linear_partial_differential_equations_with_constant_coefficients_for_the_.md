### Equations reducible to linear partial differential equations with constant coefficients

- A partial differential equation (PDE) is an equation that involves partial derivatives of an unknown function of two or more variables.
- A linear PDE is one that is linear in the unknown function and its partial derivatives, i.e., it has the form
$$
a_0(x,y)u+a_1(x,y)u_x+a_2(x,y)u_y+a_3(x,y)u_{xx}+a_4(x,y)u_{xy}+a_5(x,y)u_{yy}+...=f(x,y)
$$
where $u$ is the unknown function, $u_x$, $u_y$, $u_{xx}$, etc. are its partial derivatives, and $a_0$, $a_1$, ..., $f$ are given functions of $x$ and $y$.
- A linear PDE with constant coefficients is a special case of a linear PDE where the coefficients $a_0$, $a_1$, ..., $a_5$ are constants, i.e., they do not depend on $x$ and $y$.
- Some PDEs that are not linear or not with constant coefficients can be reduced to linear PDEs with constant coefficients by using some transformations of variables or functions. For example, the following PDEs can be reduced to linear PDEs with constant coefficients by using the indicated transformations:

  - The heat equation
  $$
  u_t=k u_{xx}
  $$
  where $k$ is a constant, can be reduced to
  $$
  v_{\xi \eta}=0
  $$
  by using the transformation $v=u$, $\xi=x+\sqrt{k}t$, $\eta=x-\sqrt{k}t$.
  - The wave equation
  $$
  u_{tt}=c^2 u_{xx}
  $$
  where $c$ is a constant, can be reduced to
  $$
  v_{\xi \eta}=0
  $$
  by using the transformation $v=u$, $\xi=x+ct$, $\eta=x-ct$.
  - The Laplace equation
  $$
  u_{xx}+u_{yy}=0
  $$
  can be reduced to
  $$
  v_{\xi \xi}=0
  $$
  by using the transformation $v=u$, $\xi=x+iy$, where $i$ is the imaginary unit.
  - The Monge-Ampère equation
  $$
  u_{xx}u_{yy}-u_{xy}^2=1
  $$
  can be reduced to
  $$
  v_{\xi \xi}+v_{\eta \eta}=0
  $$
  by using the transformation $v=u$, $\xi=u_x$, $\eta=u_y$.

- The general method of solving linear PDEs with constant coefficients is to use the method of characteristics, which involves finding the characteristic curves or surfaces of the PDE, along which the solution is constant or satisfies an ordinary differential equation (ODE). The solution can then be obtained by integrating the ODE along the characteristic curves or surfaces, and imposing the boundary or initial conditions.