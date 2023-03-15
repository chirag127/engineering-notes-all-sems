# Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function of several variables subject to one or more equality constraints  .
- The basic idea is to construct a new function, called the Lagrangian, that combines the original function and the constraint function using a constant, called the Lagrange multiplier  .
- The Lagrangian is defined as:

$$L(x,y,z,\lambda) = f(x,y,z) - \lambda (g(x,y,z) - k)$$

where $f(x,y,z)$ is the original function, $g(x,y,z) = k$ is the constraint, and $\lambda$ is the Lagrange multiplier .

- The method of Lagrange multipliers states that the local extrema of $f(x,y,z)$ subject to $g(x,y,z) = k$ occur at the points where the gradient of the Lagrangian is zero, i.e.,

$$\nabla L(x,y,z,\lambda) = 0$$

This means that the partial derivatives of $L$ with respect to $x$, $y$, $z$, and $\lambda$ are all zero  .

- The above equation implies that the gradient of $f$ is parallel to the gradient of $g$, i.e.,

$$\nabla f(x,y,z) = \lambda \nabla g(x,y,z)$$

This means that the level curves of $f$ and $g$ are tangent at the points of extrema  .

- To find the local extrema of $f(x,y,z)$ subject to $g(x,y,z) = k$, the following steps are followed  :

  - Step 1: Construct the Lagrangian function $L(x,y,z,\lambda)$ as shown above.
  - Step 2: Solve the system of equations $\nabla L(x,y,z,\lambda) = 0$ for $x$, $y$, $z$, and $\lambda$.
  - Step 3: Plug in the solutions from Step 2 into $f(x,y,z)$ and compare the values to identify the maximum and minimum values, if they exist.

- Example: Find the maximum and minimum values of $f(x,y) = x^2 + y^2$ subject to the constraint $g(x,y) = x + y - 1 = 0$.

  - Step 1: The Lagrangian function is

  $$L(x,y,\lambda) = x^2 + y^2 - \lambda (x + y - 1)$$

  - Step 2: The system of equations $\nabla L(x,y,\lambda) = 0$ is

  $$\begin{aligned}
  \frac{\partial L}{\partial x} &= 2x - \lambda = 0 \\
  \frac{\partial L}{\partial y} &= 2y - \lambda = 0 \\
  \frac{\partial L}{\partial \lambda} &= x + y - 1 = 0
  \end{aligned}$$

  Solving for $x$, $y$, and $\lambda$, we get

  $$x = y = \frac{1}{2}, \lambda = 1$$

  - Step 3: Plugging in the solution into $f(x,y)$, we get

  $$f\left(\frac{1}{2}, \frac{1}{2}\right) = \frac{1}{2}$$

  This is the only possible value of $f$ subject to the constraint, so it is both the maximum and minimum value. The point $(1/2, 1/2)$ is the only point of extrema.