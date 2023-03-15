# Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function subject to one or more equality constraints    .
- The basic idea is to introduce a new variable, called the Lagrange multiplier, for each constraint, and form a new function, called the Lagrangian, that combines the original function and the constraints    .
- The Lagrangian is defined as:

$$
L(x,y,z,\lambda) = f(x,y,z) - \lambda (g(x,y,z) - k)
$$

where $f(x,y,z)$ is the original function, $g(x,y,z) = k$ is the constraint, and $\lambda$ is the Lagrange multiplier    .

- The method of Lagrange multipliers states that the local extrema of $f(x,y,z)$ subject to $g(x,y,z) = k$ occur at the points where the gradient of the Lagrangian is zero, i.e.,

$$
\nabla L(x,y,z,\lambda) = \begin{pmatrix} \frac{\partial L}{\partial x} \\ \frac{\partial L}{\partial y} \\ \frac{\partial L}{\partial z} \\ \frac{\partial L}{\partial \lambda} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

which is equivalent to the system of equations:

$$
\begin{aligned}
\frac{\partial f}{\partial x} - \lambda \frac{\partial g}{\partial x} &= 0 \\
\frac{\partial f}{\partial y} - \lambda \frac{\partial g}{\partial y} &= 0 \\
\frac{\partial f}{\partial z} - \lambda \frac{\partial g}{\partial z} &= 0 \\
g(x,y,z) - k &= 0
\end{aligned}
$$

- The Lagrange multiplier $\lambda$ can be interpreted as the rate of change of the optimal value of $f(x,y,z)$ as the constraint $g(x,y,z) = k$ is relaxed or tightened    .
- The method of Lagrange multipliers can be generalized to more than one constraint by introducing more Lagrange multipliers and adding them to the Lagrangian    .
- The method of Lagrange multipliers can also be applied to functions of more than three variables, by adding more partial derivatives to the system of equations    .
- The method of Lagrange multipliers is based on the assumption that the constraint function $g(x,y,z)$ is smooth and that its gradient is not zero at the points of interest    .
- The method of Lagrange multipliers does not guarantee that the solutions found are global extrema, only local ones. To determine the nature of the extrema, one can use the second derivative test or other methods    .