### Analytic functions

- A function `f(z)` of a complex variable `z = x + iy` is **analytic** if it has a complex derivative `f'(z)` at every point in its domain.
- A complex derivative `f'(z)` is defined as the limit of the difference quotient `f(z+h) - f(z) / h` as `h` approaches zero.
- A function `f(z)` is analytic if and only if it is **holomorphic**, i.e., it satisfies the **Cauchy-Riemann equations**:
  - `u_x = v_y` and `u_y = -v_x`, where `u` and `v` are the real and imaginary parts of `f(z)`, respectively.
- A function `f(z)` is analytic if and only if it is equal to its **Taylor series** in some neighborhood of every point in its domain:
  - `f(z) = f(z_0) + f'(z_0)(z-z_0) + f''(z_0)(z-z_0)^2 / 2! + ...`, where `z_0` is any point in the domain of `f(z)`.
- Analytic functions have many remarkable properties that do not hold for real differentiable functions, such as:
  - **Identity theorem**: If two analytic functions `f(z)` and `g(z)` agree on a set of points that has a limit point, then they are equal everywhere in their common domain.
  - **Maximum modulus principle**: If `f(z)` is a non-constant analytic function in a domain `D`, then `|f(z)|` cannot attain a maximum value in `D`.
  - **Liouville's theorem**: If `f(z)` is a bounded entire function (analytic in the whole complex plane), then `f(z)` is constant.
  - **Fundamental theorem of algebra**: If `p(z)` is a non-constant polynomial with complex coefficients, then `p(z)` has at least one complex root.
  - **Residue theorem**: If `f(z)` is an analytic function in a simply connected domain `D` except for a finite number of isolated singularities, then the integral of `f(z)` along any closed contour in `D` is equal to `2πi` times the sum of the residues of `f(z)` at the singularities.