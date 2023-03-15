# Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the x, y and z directions.
- The directional derivative of a function f(x,y,z) at a point P in the direction of a unit vector v is denoted by D_vf(P) or ∇_vf(P) and is defined as:

  D_vf(P) = ∇_vf(P) = lim_(h→0) [f(P+hv) - f(P)]/h

- Alternatively, the directional derivative can be expressed using the gradient of f, which is a vector that points in the direction of the greatest increase of f and has a magnitude equal to the rate of change in that direction. The gradient of f is denoted by ∇f or grad f and is defined as:

  ∇f = grad f = (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k

- The directional derivative can then be computed as the dot product of the gradient and the unit vector v:

  D_vf(P) = ∇_vf(P) = ∇f(P) ⋅ v

- The directional derivative has the following properties:

  - It is a scalar quantity, not a vector.
  - It is zero if v is perpendicular to the gradient of f at P, meaning that f does not change in that direction.
  - It is positive if v has an acute angle with the gradient of f at P, meaning that f increases in that direction.
  - It is negative if v has an obtuse angle with the gradient of f at P, meaning that f decreases in that direction.
  - It is equal to the magnitude of the gradient of f at P if v is parallel to the gradient of f at P, meaning that f changes at the maximum rate in that direction.

- Example: Find the directional derivative of the function f(x,y) = x^2 + y^2 at the point (1,1) in the direction of the vector v = 2i - j.

  - Solution: First, we need to find the gradient of f:

    ∇f = (∂f/∂x)i + (∂f/∂y)j = (2x)i + (2y)j

    At the point (1,1), the gradient is:

    ∇f(1,1) = (2)i + (2)j

  - Next, we need to normalize the vector v to get a unit vector:

    v = 2i - j

    |v| = √(2^2 + (-1)^2) = √5

    v/|v| = (2/√5)i - (1/√5)j

  - Finally, we can compute the directional derivative as the dot product of the gradient and the unit vector:

    D_vf(1,1) = ∇f(1,1) ⋅ v/|v|

    = [(2)i + (2)j] ⋅ [(2/√5)i - (1/√5)j]

    = (4/√5) - (2/√5)

    = 2/√5

    ≈ 0.8944

  - This means that the function f(x,y) increases at a rate of about 0.8944 units per unit distance in the direction of the vector v at the point (1,1).