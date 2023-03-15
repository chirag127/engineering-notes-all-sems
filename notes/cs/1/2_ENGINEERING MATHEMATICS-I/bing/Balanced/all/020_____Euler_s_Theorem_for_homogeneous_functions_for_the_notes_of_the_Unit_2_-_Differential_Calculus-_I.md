# Euler’s Theorem for homogeneous functions

- A function f(x, y, z, ...) of several variables is said to be **homogeneous** of degree n if f(tx, ty, tz, ...) = t^n f(x, y, z, ...) for any positive scalar t.
- A homogeneous function of degree n has the property that multiplying all its arguments by the same factor results in the function value being multiplied by that factor raised to the power of n.
- Examples of homogeneous functions are f(x, y) = x^2 + y^2 (degree 2), f(x, y, z) = x^3 + y^3 + z^3 (degree 3), f(x, y) = xy (degree 1), f(x, y) = x/y (degree 0).
- Euler's theorem states that if f(x, y, z, ...) is a homogeneous function of degree n, then the following relation holds :

  x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} + z \frac{\partial f}{\partial z} + ... = n f(x, y, z, ...)

- This can be proved by differentiating both sides of the definition of a homogeneous function with respect to t and then setting t = 1 .
- Euler's theorem can be used to simplify the calculation of partial derivatives of homogeneous functions, or to find the degree of homogeneity of a given function .
- Euler's theorem can also be applied to functions that are homogeneous in some of their arguments, but not all. For example, if f(x, y, z) is homogeneous of degree n in x and y, but not in z, then the following relation holds:

  x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = n f(x, y, z)