```markdown
### Lagrange's method of multipliers

- Lagrange's method of multipliers is a technique for finding the local maxima and minima of a function subject to one or more equality constraints  .
- The basic idea is to introduce a new variable, called the Lagrange multiplier, for each constraint, and to construct a new function, called the Lagrangian, that incorporates the constraints into the objective function  .
- The Lagrangian is defined as:

  L(x, y, z, λ) = f(x, y, z) - λ(g(x, y, z) - k)

  where f(x, y, z) is the objective function, g(x, y, z) is the constraint function, k is a constant, and λ is the Lagrange multiplier  .

- The method of Lagrange multipliers states that the local extrema of f(x, y, z) subject to g(x, y, z) = k occur at the points where the gradient of the Lagrangian is zero, i.e.,

  ∇L(x, y, z, λ) = 0

  or equivalently,

  ∇f(x, y, z) = λ∇g(x, y, z)

  and

  g(x, y, z) = k

  where ∇ denotes the gradient operator   .

- The steps to apply the method of Lagrange multipliers are:

  1. Write down the Lagrangian function using the objective function and the constraint function(s).
  2. Find the partial derivatives of the Lagrangian with respect to each variable and the Lagrange multiplier(s), and set them equal to zero.
  3. Solve the system of equations for the variables and the Lagrange multiplier(s).
  4. Plug in the solutions into the objective function and compare the values to find the maximum and minimum, if they exist .

- The method of Lagrange multipliers can be generalized to more than one constraint by introducing more Lagrange multipliers and adding them to the Lagrangian function  .
- The method of Lagrange multipliers can also be interpreted geometrically as finding the points where the level curves of the objective function and the constraint function are tangent to each other, meaning that their gradients are parallel  .
```