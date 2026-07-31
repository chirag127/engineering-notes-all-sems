### Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function subject to one or more equality constraints  .
- The basic idea is to introduce a new variable, called the Lagrange multiplier, for each constraint, and to construct a new function, called the Lagrangian, that incorporates the constraints into the objective function  .
- The Lagrangian is defined as:

$$
L(x,y,z,\lambda) = f(x,y,z) - \lambda (g(x,y,z) - k)
$$

where $f(x,y,z)$ is the objective function, $g(x,y,z) = k$ is the constraint, and $\lambda$ is the Lagrange multiplier .

- The method of Lagrange multipliers states that the local extrema of the objective function subject to the constraint are the solutions of the following system of equations :

$$
\nabla f(x,y,z) = \lambda \nabla g(x,y,z) \\
g(x,y,z) = k
$$

where $\nabla f$ and $\nabla g$ are the gradient vectors of $f$ and $g$, respectively .

- The geometric interpretation of this method is that at the optimal points, the gradient vectors of the objective function and the constraint are parallel, meaning that they point in the same or opposite directions  . This implies that the level surface of the objective function is tangent to the level surface of the constraint at the optimal points  .
- The method of Lagrange multipliers can be generalized to more than one constraint by introducing more Lagrange multipliers and adding more terms to the Lagrangian  . For example, if we have two constraints, $g_1(x,y,z) = k_1$ and $g_2(x,y,z) = k_2$, the Lagrangian becomes:

$$
L(x,y,z,\lambda_1,\lambda_2) = f(x,y,z) - \lambda_1 (g_1(x,y,z) - k_1) - \lambda_2 (g_2(x,y,z) - k_2)
$$

and the system of equations becomes:

$$
\nabla f(x,y,z) = \lambda_1 \nabla g_1(x,y,z) + \lambda_2 \nabla g_2(x,y,z) \\
g_1(x,y,z) = k_1 \\
g_2(x,y,z) = k_2
$$

- The method of Lagrange multipliers can also be applied to functions of more than three variables, as long as the number of variables is equal to or greater than the number of constraints  .
- To find the optimal values of the objective function, we need to plug in the solutions of the system of equations into the objective function and compare them  . The largest value is the maximum, and the smallest value is the minimum, provided they exist  .