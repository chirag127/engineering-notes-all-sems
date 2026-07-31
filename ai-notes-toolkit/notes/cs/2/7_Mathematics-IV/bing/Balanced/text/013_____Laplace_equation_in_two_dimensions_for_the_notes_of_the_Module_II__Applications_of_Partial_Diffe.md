### Laplace equation in two dimensions

- Laplace equation is a second-order partial differential equation that describes the potential field in a region where there are no sources or sinks of the potential.
- Laplace equation in two dimensions in Cartesian coordinates is given by

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

where $u$ is the potential function that depends on $x$ and $y$.

- Laplace equation can be solved by using the method of separation of variables, which assumes that the solution can be written as a product of two functions, one depending on $x$ and the other depending on $y$.

$$u(x,y) = X(x)Y(y)$$

- Substituting this form of solution into the Laplace equation and dividing by $XY$, we get

$$\frac{1}{X}\frac{d^2 X}{dx^2} + \frac{1}{Y}\frac{d^2 Y}{dy^2} = 0$$

- Since the left-hand side depends only on $x$ and the right-hand side depends only on $y$, they must both be equal to a constant, say $-\lambda^2$.

$$\frac{1}{X}\frac{d^2 X}{dx^2} = -\lambda^2$$

$$\frac{1}{Y}\frac{d^2 Y}{dy^2} = \lambda^2$$

- These are two ordinary differential equations that can be solved by using standard techniques, such as the characteristic equation method or the power series method.

- The general solution for $X(x)$ is

$$X(x) = A\cos(\lambda x) + B\sin(\lambda x)$$

where $A$ and $B$ are arbitrary constants.

- The general solution for $Y(y)$ is

$$Y(y) = C\exp(\lambda y) + D\exp(-\lambda y)$$

where $C$ and $D$ are arbitrary constants.

- Therefore, the general solution for $u(x,y)$ is

$$u(x,y) = (A\cos(\lambda x) + B\sin(\lambda x))(C\exp(\lambda y) + D\exp(-\lambda y))$$

- To find the particular solution that satisfies the boundary conditions, we need to determine the values of the constants $A$, $B$, $C$, $D$, and $\lambda$.

- The boundary conditions may be of Dirichlet type, which specify the value of $u$ on the boundary, or of Neumann type, which specify the normal derivative of $u$ on the boundary.

- Depending on the shape and orientation of the boundary, the boundary conditions may be homogeneous or non-homogeneous, and the solution may involve trigonometric or hyperbolic functions.

- Some examples of boundary value problems for Laplace equation in two dimensions are:

  - A rectangular plate with fixed temperatures on the edges.
  - A circular disk with a hole in the center and given temperatures on the inner and outer boundaries.
  - A two-dimensional fluid flow with incompressible and irrotational conditions.

- Laplace equation has many applications in physics, engineering, and mathematics, such as heat conduction, electrostatics, gravity, harmonic functions, and complex analysis.