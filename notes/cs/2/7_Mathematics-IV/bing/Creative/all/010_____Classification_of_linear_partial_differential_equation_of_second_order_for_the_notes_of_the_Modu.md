# Classification of linear partial differential equation of second order

- A linear partial differential equation of second order is an equation of the form

$$
A(x,y)u_{xx} + 2B(x,y)u_{xy} + C(x,y)u_{yy} + D(x,y)u_{x} + E(x,y)u_{y} + F(x,y)u = G(x,y)
$$

where $A, B, C, D, E, F, G$ are given functions of $x$ and $y$, and $u$ is an unknown function of $x$ and $y$.

- The classification of such equations is based on the sign of the discriminant

$$
D(x,y) = B(x,y)^2 - A(x,y)C(x,y)
$$

- Depending on the sign of $D(x,y)$, the equation can be classified as:

  - Hyperbolic, if $D(x,y) > 0$ for all $(x,y)$ in the domain of interest. Examples of hyperbolic equations are the wave equation and the transport equation.

  - Parabolic, if $D(x,y) = 0$ for all $(x,y)$ in the domain of interest. Examples of parabolic equations are the heat equation and the diffusion equation.

  - Elliptic, if $D(x,y) < 0$ for all $(x,y)$ in the domain of interest. Examples of elliptic equations are the Laplace equation and the Poisson equation.

- The classification of linear partial differential equations of second order is important because it determines the type of solutions and the methods of solving them. For example, hyperbolic equations have solutions that propagate along characteristic curves, parabolic equations have solutions that evolve in time and smooth out, and elliptic equations have solutions that are harmonic and satisfy the maximum principle.

- The classification can also change depending on the coordinate system used. For example, the equation

$$
u_{xx} - u_{yy} = 0
$$

is hyperbolic in Cartesian coordinates, but elliptic in polar coordinates. To find the classification in any coordinate system, one can use the method of characteristics or the method of canonical forms. These methods transform the equation into a simpler form that reveals its classification.