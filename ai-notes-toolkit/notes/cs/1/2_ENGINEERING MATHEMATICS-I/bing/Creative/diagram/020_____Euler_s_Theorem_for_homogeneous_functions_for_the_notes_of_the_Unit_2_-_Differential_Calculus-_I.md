### Euler’s Theorem for homogeneous functions

- A function f(x, y, z, ...) of several variables is said to be **homogeneous** of degree n if f(tx, ty, tz, ...) = t^n f(x, y, z, ...) for any positive scalar t.
- A homogeneous function of degree n has the property that multiplying each of its variables by a constant factor results in the function being multiplied by the n-th power of that factor.
- Examples of homogeneous functions are f(x, y) = x^2 + y^2 (degree 2), f(x, y, z) = x^3 + y^3 + z^3 (degree 3), f(x, y) = xy (degree 1), f(x, y) = x/y (degree 0).
- Euler's theorem for homogeneous functions states that if f(x, y, z, ...) is a homogeneous function of degree n, then the following relation holds :

    x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} + z \frac{\partial f}{\partial z} + ... = n f(x, y, z, ...)

- This theorem can be derived by differentiating both sides of the definition of a homogeneous function with respect to t and then setting t = 1 .
- Euler's theorem can be used to establish a relationship between the partial derivatives and the function product with its degree. It can also be used to simplify calculations involving homogeneous functions.
- A special case of Euler's theorem is when n = 0, which implies that f(x, y, z, ...) is a constant function.