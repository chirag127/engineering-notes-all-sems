## Unit 4 - Complex Variable–Differentiation

Complex differentiation is the extension of the concept of differentiation to complex-valued functions of a complex variable. The basic idea is the same as for real differentiation, but the algebra of complex numbers allows for more possibilities.

1. **Definition of Differentiability:** A complex function `f(z)` is said to be differentiable at a point `z0` if the limit `f'(z0) = lim (f(z) - f(z0)) / (z - z0)` as `z` approaches `z0` exists. This limit is called the derivative of `f` at `z0`.

2. **Cauchy-Riemann Equations:** If a complex function `f(z) = u(x,y) + iv(x,y)` is differentiable at a point `z0 = x0 + iy0`, then the partial derivatives of `u` and `v` with respect to `x` and `y` must satisfy the Cauchy-Riemann equations at `(x0, y0)`: `du/dx = dv/dy` and `du/dy = -dv/dx`.

3. **Analytic Functions:** A complex function `f(z)` is said to be analytic at a point `z0` if it is differentiable in some neighborhood of `z0`. A function that is analytic at every point in a domain is called an entire function.

4. **Harmonic Functions:** If a complex function `f(z) = u(x,y) + iv(x,y)` is analytic in a domain, then both `u` and `v` are harmonic functions, meaning that they satisfy Laplace's equation: `d^2u/dx^2 + d^2u/dy^2 = 0` and `d^2v/dx^2 + d^2v/dy^2 = 0`.

5. **Conformal Mapping:** A complex function `f(z)` is said to be conformal at a point `z0` if it preserves angles between curves passing through `z0`. If `f(z)` is analytic and its derivative `f'(z)` is nonzero at `z0`, then `f(z)` is conformal at `z0`.
