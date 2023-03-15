### Laplace equation in two dimensions

- Laplace equation is a second-order partial differential equation that describes the potential function in a region where there is no source or sink of the potential.
- Laplace equation in two dimensions in Cartesian coordinates is given by

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

where $u$ is the potential function that depends on $x$ and $y$.

- Laplace equation can be solved by using the method of separation of variables, which assumes that the solution can be written as a product of two functions, one depending on $x$ and the other depending on $y$.

$$u(x,y) = X(x)Y(y)$$

- Substituting this form of solution into the Laplace equation and dividing by $XY$, we get

$$\frac{1}{X}\frac{d^2 X}{dx^2} + \frac{1}{Y}\frac{d^2 Y}{dy^2} = 0$$

- Since the left-hand side of this equation depends only on $x$ and the right-hand side depends only on $y$, they must both be equal to a constant, say $-\lambda^2$.

$$\frac{1}{X}\frac{d^2 X}{dx^2} = -\lambda^2$$

$$\frac{1}{Y}\frac{d^2 Y}{dy^2} = \lambda^2$$

- These are two ordinary differential equations that can be solved by using standard methods, such as the characteristic equation or the power series method.

- The general solution of the Laplace equation in two dimensions is then given by a linear combination of the solutions of the separated equations, which depend on the boundary conditions of the problem.

- Some examples of applications of Laplace equation in two dimensions are:

  - Heat conduction in a rectangular plate with fixed boundary temperatures.
  - Electrostatic potential in a region with fixed boundary charges.
  - Fluid flow in an incompressible and irrotational fluid with fixed boundary velocities.
  - Harmonic functions and complex analytic functions.