### Vector differentiation: Gradient

- The gradient of a scalar-valued function of several variables is a vector-valued function that measures the direction and rate of fastest increase of the function at a given point.
- The gradient is denoted by the symbol ∇ (nabla) and is defined as the vector of partial derivatives of the function with respect to each variable.
- For example, if f(x,y,z) is a scalar function of three variables, then the gradient of f is given by

∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

- The gradient can be interpreted geometrically as the normal vector to the level surface of the function at a given point. The magnitude of the gradient is equal to the slope of the tangent plane to the level surface at that point.
- The gradient can also be used to find the directional derivative of a function along any direction. The directional derivative of f at a point a in the direction of a unit vector u is given by

D_uf(a) = ∇f(a) · u

where · denotes the dot product of two vectors. The directional derivative measures the rate of change of the function in the direction of u at a.

- The gradient has several properties that follow from its definition and the properties of partial derivatives. Some of these properties are:

  - Linearity: ∇(cf + g) = c∇f + ∇g for any scalar function f and g and any constant c.
  - Product rule: ∇(fg) = f∇g + g∇f for any scalar function f and g.
  - Chain rule: ∇(f(g(x,y,z))) = (∇f)(g(x,y,z)) · ∇g for any scalar function f and g of three variables.
  - Divergence theorem: ∫∫_S ∇f · n dS = ∫∫∫_V ∇ · ∇f dV for any scalar function f and any closed surface S enclosing a volume V, where n is the outward unit normal vector to S and ∇ · denotes the divergence operator.