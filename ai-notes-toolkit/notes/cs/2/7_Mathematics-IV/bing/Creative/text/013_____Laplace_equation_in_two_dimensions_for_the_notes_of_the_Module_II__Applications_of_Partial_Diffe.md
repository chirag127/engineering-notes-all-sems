### Laplace equation in two dimensions

- Laplace equation is a second-order partial differential equation that describes the potential field of a system that is in equilibrium, such as heat, electrostatics, fluid flow, etc.
- Laplace equation in two dimensions in Cartesian coordinates is given by

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

where $u$ is the unknown function of $x$ and $y$.

- Laplace equation is linear, homogeneous and elliptic, which means that the superposition principle applies, the solutions are smooth and bounded, and the boundary conditions determine the solution uniquely.

- Laplace equation can be solved by various methods, such as separation of variables, Fourier series, conformal mapping, Green's functions, etc.

- Separation of variables is a method that assumes that the solution can be written as a product of functions of each variable, such as $u(x,y) = X(x)Y(y)$. Substituting this into the Laplace equation and dividing by $u$, we get

$$\frac{X''}{X} + \frac{Y''}{Y} = 0$$

where the prime denotes differentiation. Since the left-hand side depends only on $x$ and the right-hand side depends only on $y$, they must be equal to a constant, say $-\lambda$. This leads to two ordinary differential equations for $X$ and $Y$:

$$X'' + \lambda X = 0$$
$$Y'' - \lambda Y = 0$$

- The solutions of these equations depend on the value of $\lambda$ and the boundary conditions. For example, if the boundary conditions are of Dirichlet type, meaning that the value of $u$ is given on the boundary of the domain, then the possible values of $\lambda$ are positive and discrete, and the solutions are of the form

$$X(x) = A \cos(\sqrt{\lambda} x) + B \sin(\sqrt{\lambda} x)$$
$$Y(y) = C \cos(\sqrt{\lambda} y) + D \sin(\sqrt{\lambda} y)$$

where $A, B, C, D$ are constants determined by the boundary conditions.

- The general solution of the Laplace equation is then a linear combination of these separated solutions, such as

$$u(x,y) = \sum_{n=1}^{\infty} (a_n \cos(\sqrt{\lambda_n} x) + b_n \sin(\sqrt{\lambda_n} x))(c_n \cos(\sqrt{\lambda_n} y) + d_n \sin(\sqrt{\lambda_n} y))$$

where the coefficients $a_n, b_n, c_n, d_n$ are determined by the boundary conditions using Fourier series.

- Laplace equation is invariant under rigid motions, which are the translations and rotations. A translation is a transformation $x \to x_0$, which is given by $x_0 = x + a$ and $y_0 = y + b$ for some constants $a$ and $b$. A rotation is a transformation $x \to x_0$, which is given by

$$x_0 = x \cos \theta - y \sin \theta$$
$$y_0 = x \sin \theta + y \cos \theta$$

for some angle $\theta$. If $u(x,y)$ is a solution of the Laplace equation, then so is $u(x_0, y_0)$.

- Laplace equation can also be written in other coordinate systems, such as polar, cylindrical, spherical, etc. For example, in polar coordinates $(r, \theta)$, the Laplace equation is given by

$$\frac{1}{r} \frac{\partial}{\partial r} \left( r \frac{\partial u}{\partial r} \right) + \frac{1}{r^2} \frac{\partial^2 u}{\partial \theta^2} = 0$$

where $u$ is the unknown function of $r$ and $\theta$.

- Laplace equation can be solved by separation of variables in polar coordinates as well, by assuming that the solution can be written as a product of functions of each variable, such as $u(r, \theta) = R(r) \Theta(\theta)$. Substituting this into the Laplace equation and dividing by $