### Classification of linear partial differential equation of second order

- A linear partial differential equation of second order is an equation of the form

$$
A(x,y)u_{xx} + 2B(x,y)u_{xy} + C(x,y)u_{yy} + D(x,y)u_{x} + E(x,y)u_{y} + F(x,y)u = G(x,y)
$$

where $A, B, C, D, E, F, G$ are given functions of $x$ and $y$, and $u$ is an unknown function of $x$ and $y$.

- The classification of such an equation depends on the sign of the discriminant

$$
D(x,y) = B(x,y)^2 - A(x,y)C(x,y)
$$

at each point $(x,y)$.

- There are three main types of linear partial differential equations of second order:

  - **Hyperbolic**: If $D(x,y) > 0$ for all $(x,y)$, then the equation is hyperbolic. This type of equation describes wave phenomena, such as sound, light, or water waves. An example of a hyperbolic equation is the wave equation

  $$
  u_{tt} - c^2 u_{xx} = 0
  $$

  where $c$ is a constant.

  - **Parabolic**: If $D(x,y) = 0$ for all $(x,y)$, then the equation is parabolic. This type of equation describes diffusion phenomena, such as heat, mass, or electric potential. An example of a parabolic equation is the heat equation

  $$
  u_{t} - k u_{xx} = 0
  $$

  where $k$ is a constant.

  - **Elliptic**: If $D(x,y) < 0$ for all $(x,y)$, then the equation is elliptic. This type of equation describes equilibrium phenomena, such as electrostatics, gravity, or elasticity. An example of an elliptic equation is the Laplace equation

  $$
  u_{xx} + u_{yy} = 0
  $$

- The classification of a linear partial differential equation of second order may vary from point to point, depending on the sign of the discriminant. For example, the Tricomi equation

$$
u_{xx} + x u_{yy} = 0
$$

is hyperbolic when $x > 0$, parabolic when $x = 0$, and elliptic when $x < 0$.

- The classification of a linear partial differential equation of second order determines the nature of its solutions and the methods of solving it. For example, hyperbolic equations can be solved by the method of characteristics, parabolic equations can be solved by the method of separation of variables, and elliptic equations can be solved by the method of Green's functions.