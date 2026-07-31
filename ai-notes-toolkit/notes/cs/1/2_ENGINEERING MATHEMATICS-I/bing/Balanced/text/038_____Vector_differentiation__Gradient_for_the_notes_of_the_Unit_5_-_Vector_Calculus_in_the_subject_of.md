### Vector differentiation: Gradient

- The gradient of a scalar-valued function of several variables is a vector-valued function that measures the direction and rate of fastest increase of the function at a given point.
- The gradient is denoted by the symbol ∇ (nabla) and is defined as the vector of partial derivatives of the function with respect to each variable.
- For example, if f(x,y,z) is a scalar-valued function of three variables, then the gradient of f is given by

∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

- The gradient can be interpreted geometrically as the normal vector to the level surface of the function at a given point. The magnitude of the gradient is equal to the slope of the tangent plane to the level surface at that point.
- The gradient can also be used to find the directional derivative of a function along any direction. The directional derivative of f at a point a in the direction of a unit vector u is given by

D_uf(a) = ∇f(a) · u

where · denotes the dot product of two vectors. The directional derivative measures the rate of change of the function along the direction of u at a.

- The gradient has several properties that follow from the properties of partial derivatives and vector operations. Some of these properties are:

∇(f+g) = ∇f + ∇g

∇(cf) = c∇f

∇(fg) = f∇g + g∇f

∇(f/g) = (g∇f - f∇g)/g^2

∇(f^g) = g(f^(g-1))∇f + f^g ln(f)∇g

- The gradient can also be generalized to vector-valued functions of several variables using the multivariable chain rule. For example, if f(x,y,z) is a scalar-valued function and g(t) = (x(t), y(t), z(t)) is a vector-valued function, then the gradient of f along the curve g(t) is given by

∇f(g(t)) = (∂f/∂x, ∂f/∂y, ∂f/∂z) · (x'(t), y'(t), z'(t))

where · denotes the dot product of two vectors and ' denotes the derivative with respect to t.