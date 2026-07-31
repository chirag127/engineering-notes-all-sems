Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your notes.

### Classification of linear partial differential equation of second order

- A linear partial differential equation (PDE) of second order is an equation of the form

$$
A(x,y)u_{xx} + 2B(x,y)u_{xy} + C(x,y)u_{yy} + D(x,y)u_{x} + E(x,y)u_{y} + F(x,y)u = G(x,y)
$$

where $u$ is the unknown function of $x$ and $y$, and $A, B, C, D, E, F, G$ are given functions of $x$ and $y$.

- The classification of a linear PDE of second order depends on the sign of the discriminant

$$
D(x,y) = B(x,y)^2 - A(x,y)C(x,y)
$$

- There are three main types of linear PDEs of second order:

  - **Hyperbolic**: If $D(x,y) > 0$ for all $(x,y)$ in the domain of interest, then the PDE is hyperbolic. An example of a hyperbolic PDE is the wave equation

  $$
  u_{tt} - c^2 u_{xx} = 0
  $$

  where $c$ is a constant.

  - **Parabolic**: If $D(x,y) = 0$ for all $(x,y)$ in the domain of interest, then the PDE is parabolic. An example of a parabolic PDE is the heat equation

  $$
  u_{t} - k u_{xx} = 0
  $$

  where $k$ is a constant.

  - **Elliptic**: If $D(x,y) < 0$ for all $(x,y)$ in the domain of interest, then the PDE is elliptic. An example of an elliptic PDE is the Laplace equation

  $$
  u_{xx} + u_{yy} = 0
  $$

- The classification of a linear PDE of second order is important because it determines the nature of the solutions and the methods of solving the PDE. For example, hyperbolic PDEs typically have solutions that propagate waves, parabolic PDEs typically have solutions that diffuse heat, and elliptic PDEs typically have solutions that are harmonic functions.

- The classification of a linear PDE of second order may vary depending on the point $(x,y)$ in the domain. For example, the Tricomi equation

$$
u_{xx} + x u_{yy} = 0
$$

is hyperbolic when $x > 0$, parabolic when $x = 0$, and elliptic when $x < 0$.

- The classification of a linear PDE of second order can be changed by applying a suitable change of variables. For example, the PDE

$$
u_{xx} - 2u_{xy} + u_{yy} = 0
$$

is hyperbolic, but by using the change of variables $x = \xi + \eta$, $y = \xi - \eta$, it can be transformed to

$$
u_{\xi\xi} + u_{\eta\eta} = 0
$$

which is elliptic. This process of transforming a PDE to a simpler form is called finding the canonical form of the PDE.