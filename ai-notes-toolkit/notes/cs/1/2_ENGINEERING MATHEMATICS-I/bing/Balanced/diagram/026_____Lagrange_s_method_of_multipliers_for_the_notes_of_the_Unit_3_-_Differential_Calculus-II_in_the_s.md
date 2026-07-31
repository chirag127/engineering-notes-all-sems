### Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function of several variables subject to one or more equality constraints  .
- The basic idea is to introduce a new variable, called a Lagrange multiplier, for each constraint, and to construct a new function, called the Lagrangian, that incorporates the constraints into the objective function  .
- The Lagrangian is defined as:

  $$L(x,y,z,\lambda) = f(x,y,z) - \lambda (g(x,y,z) - k)$$

  where $f(x,y,z)$ is the objective function, $g(x,y,z) = k$ is the constraint, and $\lambda$ is the Lagrange multiplier .

- The method of Lagrange multipliers states that the local extrema of the objective function subject to the constraint are the solutions of the following system of equations :

  $$\nabla f(x,y,z) = \lambda \nabla g(x,y,z)$$
  $$g(x,y,z) = k$$

  where $\nabla f$ and $\nabla g$ are the gradient vectors of $f$ and $g$, respectively .

- The geometric interpretation of this method is that at the optimal points, the gradient vectors of the objective function and the constraint are parallel, meaning that they point in the same or opposite directions  .
- The Lagrange multiplier $\lambda$ can be interpreted as the rate of change of the optimal value of the objective function as the constraint is relaxed or tightened  .
- The method of Lagrange multipliers can be generalized to handle multiple constraints of the form $g_i(x,y,z) = k_i$, for $i = 1, 2, \dots, m$, by introducing a Lagrange multiplier $\lambda_i$ for each constraint and forming the Lagrangian as:

  $$L(x,y,z,\lambda_1,\lambda_2,\dots,\lambda_m) = f(x,y,z) - \sum_{i=1}^m \lambda_i (g_i(x,y,z) - k_i)$$

  The optimal points are then the solutions of the system of equations:

  $$\nabla f(x,y,z) = \sum_{i=1}^m \lambda_i \nabla g_i(x,y,z)$$
  $$g_i(x,y,z) = k_i, \quad i = 1, 2, \dots, m$$

- The method of Lagrange multipliers can also be applied to functions of more than three variables, or to inequality constraints, with some modifications  .
- The method of Lagrange multipliers is useful for solving optimization problems in engineering, economics, physics, and other fields  .

- Here is an example of how to apply the method of Lagrange multipliers to find the maximum and minimum values of a function of two variables subject to a constraint:

  - Find the maximum and minimum values of $f(x,y) = x^2 + y^2$ subject to the constraint $g(x,y) = x + y - 1 = 0$.

  - Solution:

    - Step 1: Define the Lagrangian function as:

      $$L(x,y,\lambda) = f(x,y) - \lambda g(x,y) = x^2 + y^2 - \lambda (x + y - 1)$$

    - Step 2: Find the partial derivatives of the Lagrangian function and set them equal to zero:

      $$\frac{\partial L}{\partial x} = 2x - \lambda = 0 \implies x = \frac{\lambda}{2}$$
      $$\frac{\partial L}{\partial y} = 2y - \lambda = 0 \implies y = \frac{\lambda}{2}$$
      $$\frac{\partial L}{\partial \lambda} = - (x + y - 1) = 0 \implies x + y =