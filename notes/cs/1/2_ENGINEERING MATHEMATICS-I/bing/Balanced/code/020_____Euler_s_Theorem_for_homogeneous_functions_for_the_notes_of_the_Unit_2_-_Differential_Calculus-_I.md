### Euler’s Theorem for homogeneous functions

- A function f(x, y, z, ...) of several variables is said to be **homogeneous** of degree n if f(tx, ty, tz, ...) = t^n f(x, y, z, ...) for any positive scalar t.
- A homogeneous function of degree n has the property that multiplying all its arguments by the same factor results in the function value being multiplied by that factor raised to the power n.
- Examples of homogeneous functions are f(x, y) = x^2 + y^2 (degree 2), f(x, y, z) = xyz (degree 3), f(x, y) = x/y (degree 0).
- Euler's theorem states that if f(x, y, z, ...) is a homogeneous function of degree n, then the following relation holds :

  x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} + z \frac{\partial f}{\partial z} + ... = n f(x, y, z, ...)

- This theorem can be proved by differentiating both sides of the definition of a homogeneous function with respect to t and then setting t = 1.
- Euler's theorem can be used to simplify the calculation of partial derivatives of homogeneous functions, or to establish a relationship between the function and its partial derivatives .