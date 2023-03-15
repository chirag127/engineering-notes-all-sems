### Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function of several variables subject to one or more equality constraints .
- The basic idea is to construct a new function, called the Lagrangian, that combines the original function and the constraint function(s) using some constants, called the Lagrange multipliers  .
- The Lagrangian is defined as:

$$
L(x,y,z,\lambda) = f(x,y,z) - \lambda g(x,y,z)
$$

where $\lambda$ is the Lagrange multiplier and $g(x,y,z) = k$ is the constraint function.

- The method of Lagrange multipliers states that if $(x_0,y_0,z_0)$ is a local extremum of $f(x,y,z)$ subject to $g(x,y,z) = k$, then there exists a constant $\lambda_0$ such that $(x_0,y_0,z_0,\lambda_0)$ is a stationary point of $L(x,y,z,\lambda)$, i.e.,

$$
\nabla L(x_0,y_0,z_0,\lambda_0) = \vec{0}
$$

where $\nabla L$ is the gradient vector of $L$  .

- To find the local extrema of $f(x,y,z)$ subject to $g(x,y,z) = k$, we need to solve the following system of equations:

$$
\begin{aligned}
\frac{\partial L}{\partial x} &= \frac{\partial f}{\partial x} - \lambda \frac{\partial g}{\partial x} = 0 \\
\frac{\partial L}{\partial y} &= \frac{\partial f}{\partial y} - \lambda \frac{\partial g}{\partial y} = 0 \\
\frac{\partial L}{\partial z} &= \frac{\partial f}{\partial z} - \lambda \frac{\partial g}{\partial z} = 0 \\
\frac{\partial L}{\partial \lambda} &= -g(x,y,z) + k = 0
\end{aligned}
$$

- The solutions of this system are the candidates for the local extrema of $f(x,y,z)$ subject to $g(x,y,z) = k$. To determine whether they are maxima, minima, or saddle points, we can use the second derivative test or compare the values of $f(x,y,z)$ at these points  .
- If there are more than one constraint functions, we can use more than one Lagrange multiplier and construct the Lagrangian as:

$$
L(x,y,z,\lambda_1,\lambda_2) = f(x,y,z) - \lambda_1 g_1(x,y,z) - \lambda_2 g_2(x,y,z)
$$

where $g_1(x,y,z) = k_1$ and $g_2(x,y,z) = k_2$ are the constraint functions. The method of Lagrange multipliers can be generalized to any number of variables and constraints .