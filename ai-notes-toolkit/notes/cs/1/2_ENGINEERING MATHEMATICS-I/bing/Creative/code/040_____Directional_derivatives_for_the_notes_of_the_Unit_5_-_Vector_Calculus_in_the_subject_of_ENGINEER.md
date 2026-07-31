# Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the x, y and z directions.
- It can be used to find the slope of a surface or the gradient of a scalar field in any direction.

## Definition and formula

- Let f(x,y,z) be a scalar function of three variables, and let P(x0,y0,z0) be a point in its domain.
- Let v = ai + bj + ck be a unit vector that represents the direction of interest.
- The directional derivative of f at P in the direction of v, denoted by Dvf(P), is defined as the limit:

Dvf(P) = lim(h->0) [f(x0+ha, y0+hb, z0+hc) - f(x0,y0,z0)] / h

- Alternatively, the directional derivative can be expressed using the gradient of f, denoted by ∇f, which is a vector of partial derivatives:

∇f = (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k

- The directional derivative is then the dot product of the gradient and the unit vector:

Dvf(P) = ∇f(P) · v

## Properties and examples

- The directional derivative has some basic properties, such as:

  - Dvf(P) = 0 if v is perpendicular to ∇f(P), meaning that the function does not change in that direction.
  - Dvf(P) = |∇f(P)| if v is parallel to ∇f(P), meaning that the function changes at the maximum rate in that direction.
  - Dvf(P) = -|∇f(P)| if v is antiparallel to ∇f(P), meaning that the function changes at the minimum rate in that direction.

- For example, consider the function f(x,y) = x^2 + y^2, and the point P(1,1). The gradient of f is:

∇f = (2x)i + (2y)j

- At P, the gradient is:

∇f(P) = 2i + 2j

- The magnitude of the gradient is:

|∇f(P)| = √(2^2 + 2^2) = 2√2

- If we want to find the directional derivative of f at P in the direction of v = (1/√2)i + (1/√2)j, which is a unit vector, we can use the dot product formula:

Dvf(P) = ∇f(P) · v

= (2i + 2j) · [(1/√2)i + (1/√2)j]

= 2(1/√2) + 2(1/√2)

= 2√2

- This means that the function f increases at the maximum rate of 2√2 in the direction of v at P.

- If we want to find the directional derivative of f at P in the direction of w = -(1/√2)i - (1/√2)j, which is also a unit vector, we can use the same formula:

Dwf(P) = ∇f(P) · w

= (2i + 2j) · [-(1/√2)i - (1/√2)j]

= -2(1/√2) - 2(1/√2)

= -2√2

- This means that the function f decreases at the minimum rate of -2√2 in the direction of w at P.