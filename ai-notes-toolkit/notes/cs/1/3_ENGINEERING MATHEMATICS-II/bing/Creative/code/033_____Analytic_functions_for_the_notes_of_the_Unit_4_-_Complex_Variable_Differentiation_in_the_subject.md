# Analytic functions

- A function `f(z)` of a complex variable `z = x + iy` is **analytic** if it has a **complex derivative** `f'(z)` at every point in its domain.
- A complex derivative `f'(z)` is defined as the limit of the difference quotient `f(z+h) - f(z) / h` as `h` approaches zero, where `h` is also a complex number.
- A function `f(z)` is analytic if and only if it is **holomorphic**, i.e., it satisfies the **Cauchy-Riemann equations**:
  - `u_x = v_y` and `u_y = -v_x`, where `u` and `v` are the real and imaginary parts of `f(z)`, respectively, and `u_x` denotes the partial derivative of `u` with respect to `x`, etc.
- A function `f(z)` is analytic if and only if it is equal to its **Taylor series** about any point `z_0` in its domain, i.e., `f(z) = sum_{n=0}^infty a_n (z - z_0)^n`, where `a_n = f^(n)(z_0) / n!` are the **Taylor coefficients**.
- Analytic functions have many remarkable properties that do not hold for real differentiable functions, such as:
  - **Identity theorem**: If two analytic functions `f(z)` and `g(z)` agree on a set of points that has a limit point, then they are equal everywhere in their common domain.
  - **Maximum modulus principle**: If `f(z)` is analytic and non-constant in a domain `D`, then `|f(z)|` cannot attain a maximum value in `D`.
  - **Liouville's theorem**: If `f(z)` is analytic and bounded in the entire complex plane, then `f(z)` is constant.
  - **Fundamental theorem of algebra**: If `p(z)` is a non-constant polynomial with complex coefficients, then `p(z)` has at least one complex root.
  - **Residue theorem**: If `f(z)` is analytic in a simply connected domain except for a finite number of isolated singularities, then the integral of `f(z)` around any closed contour in the domain is equal to `2 pi i` times the sum of the **residues** of `f(z)` at the singularities.