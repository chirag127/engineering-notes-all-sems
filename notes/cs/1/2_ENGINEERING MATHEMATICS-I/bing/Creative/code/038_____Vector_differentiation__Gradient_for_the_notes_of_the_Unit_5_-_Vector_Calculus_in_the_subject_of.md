# Vector differentiation: Gradient

- The gradient of a scalar-valued function of several variables is a vector that points in the direction of the maximum rate of change of the function at a given point.
- The gradient is denoted by the symbol ∇ (nabla) and is defined as the vector of partial derivatives of the function with respect to each variable.
- For example, if f(x,y,z) is a scalar function of three variables, then the gradient of f is given by

```math
\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)
```

- The gradient can be interpreted geometrically as the normal vector to the level surface of the function at a given point.
- The gradient can also be used to find the directional derivative of a function along any direction, by taking the dot product of the gradient and the unit vector of the direction.
- The gradient has the following properties:

  - Linearity: ∇(af+bg) = a∇f + b∇g, where a and b are constants and f and g are scalar functions.
  - Product rule: ∇(fg) = f∇g + g∇f, where f and g are scalar functions.
  - Chain rule: ∇(f(g(x,y,z))) = (∇f)(g(x,y,z))⋅∇g, where f and g are scalar functions and ∇f is evaluated at g(x,y,z).
  - Divergence theorem: ∫∫∫V ∇⋅F dV = ∫∫S F⋅n dS, where F is a vector field, V is a closed region, S is the boundary surface of V, and n is the outward unit normal vector to S.
  - Curl theorem: ∫∫S ∇×F⋅n dS = ∫C F⋅dr, where F is a vector field, S is an oriented surface, n is the unit normal vector to S, and C is the boundary curve of S.