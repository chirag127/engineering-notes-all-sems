# Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- A complex function f(z) = u(x, y) + iv(x, y) is holomorphic if and only if it satisfies the Cauchy-Riemann equations in Cartesian form:
  - (1a) ∂u/∂x = ∂v/∂y
  - (1b) ∂u/∂y = -∂v/∂x
- The Cauchy-Riemann equations can also be written in polar form, using the polar coordinates z = r(cos θ + i sin θ) and f(z) = U(r, θ) + iV(r, θ):
  - (2a) ∂U/∂r = (1/r) ∂V/∂θ
  - (2b) ∂V/∂r = -(1/r) ∂U/∂θ
- The Cauchy-Riemann equations allow us to check if a complex function has a complex derivative and to compute that derivative .
- If f(z) = u(x, y) + iv(x, y) is holomorphic, then its complex derivative is given by:
  - f'(z) = ∂u/∂x + i ∂v/∂x = ∂v/∂y - i ∂u/∂y
- If f(z) = U(r, θ) + iV(r, θ) is holomorphic, then its complex derivative is given by:
  - f'(z) = e^(-iθ) (∂U/∂r + i ∂V/∂r) = (1/r) e^(-iθ) (∂V/∂θ - i ∂U/∂θ)
- The Cauchy-Riemann equations are useful for proving many properties and theorems in complex analysis, such as the Cauchy integral formula, the Cauchy integral theorem, and the maximum modulus principle .