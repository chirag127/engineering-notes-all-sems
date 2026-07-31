# Laplace equation in two dimensions

- Laplace equation is a second-order partial differential equation that describes the potential field of a system that is in equilibrium, such as heat, electrostatics, fluid flow, etc.
- Laplace equation in two dimensions in Cartesian coordinates is given by

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

where $u$ is the unknown function of $x$ and $y$.

- Laplace equation is linear, homogeneous and elliptic, which means that the superposition principle applies, the solutions are smooth and bounded, and the boundary conditions determine the solution uniquely.

- Laplace equation can be solved by various methods, such as separation of variables, Fourier series, conformal mapping, Green's functions, etc.

- Separation of variables is a method that assumes that the solution can be written as a product of functions of each variable, such as $u(x,y) = X(x)Y(y)$. Substituting this into the Laplace equation and dividing by $u$, we get

$$\frac{X''}{X} + \frac{Y''}{Y} = 0$$

where the prime denotes differentiation.

- Since the left-hand side depends only on $x$ and the right-hand side depends only on $y$, they must both be equal to a constant, say $-\lambda$. This gives two ordinary differential equations for $X$ and $Y$:

$$X'' + \lambda X = 0$$
$$Y'' - \lambda Y = 0$$

- The solutions of these equations depend on the value and sign of $\lambda$, and the boundary conditions of the problem. For example, if the boundary conditions are of Dirichlet type, meaning that the value of $u$ is given on the boundary, then the solutions are either sines or cosines, or a combination of them.

- Fourier series is a method that expresses the solution as an infinite sum of trigonometric functions, such as

$$u(x,y) = \sum_{n=0}^{\infty} a_n \cos \frac{n \pi x}{L} + \sum_{n=1}^{\infty} b_n \sin \frac{n \pi x}{L}$$

where $L$ is the length of the domain in the $x$-direction, and $a_n$ and $b_n$ are coefficients that depend on the boundary conditions and the initial condition (if any).

- Conformal mapping is a method that transforms the Laplace equation in a complex domain into a simpler one, where the solution can be found more easily. A conformal mapping is a function $f(z) = u(x,y) + iv(x,y)$ that preserves angles and ratios of lengths locally, where $z = x + iy$ is the complex variable. The real and imaginary parts of $f(z)$ satisfy the Laplace equation, and the mapping is determined by the Cauchy-Riemann equations:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

- Green's functions are solutions of the Laplace equation that satisfy a point source condition, such as

$$\nabla^2 G(x,y;x_0,y_0) = \delta(x-x_0,y-y_0)$$

where $\nabla^2$ is the Laplacian operator, and $\delta$ is the Dirac delta function. The general solution of the Laplace equation with a given boundary condition can be written as a superposition of Green's functions, weighted by the boundary values.

- These are some of the methods to solve the Laplace equation in two dimensions. For more details and examples, please refer to the sources  .