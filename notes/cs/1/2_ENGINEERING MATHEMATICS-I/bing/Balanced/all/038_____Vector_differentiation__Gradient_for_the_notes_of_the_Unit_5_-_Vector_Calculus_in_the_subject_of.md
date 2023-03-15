# Vector differentiation: Gradient

- The gradient of a scalar-valued function of several variables is a vector-valued function that measures the direction and rate of fastest increase of the function at a given point.
- The gradient is denoted by the symbol ∇ (nabla) and is defined as the vector of partial derivatives of the function with respect to each variable.
- For example, if f(x,y,z) is a scalar function of three variables, then the gradient of f is given by

∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

- The gradient can be interpreted geometrically as the normal vector to the level surface of the function at a given point. The magnitude of the gradient is equal to the slope of the tangent plane to the level surface at that point.
- The gradient can also be used to find the directional derivative of a function along any direction. The directional derivative of f at a point a in the direction of a unit vector u is given by

D_uf(a) = ∇f(a) · u

where · denotes the dot product of two vectors. The directional derivative measures the rate of change of the function along the direction of u at a.
- The gradient has several properties that follow from its definition and the properties of partial derivatives. Some of these properties are:

  - Linearity: ∇(af + bg) = a∇f + b∇g for any scalar functions f and g and any constants a and b.
  - Product rule: ∇(fg) = f∇g + g∇f for any scalar functions f and g.
  - Chain rule: ∇(f(g(x))) = (∇f)(g(x)) · (∇g)(x) for any scalar functions f and g of several variables.