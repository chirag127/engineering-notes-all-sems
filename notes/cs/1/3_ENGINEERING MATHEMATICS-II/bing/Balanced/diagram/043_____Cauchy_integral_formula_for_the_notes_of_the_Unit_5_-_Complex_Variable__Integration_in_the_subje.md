### Cauchy integral formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the value of a holomorphic function at a point to its values on a circle around that point.
- The formula can be stated as follows: If f(z) is a holomorphic function on a simply-connected domain U, and γ is a positively oriented simple closed curve in U that encloses a point z_0, then

f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be generalized to higher derivatives of f(z), as follows: If f(z) is n times continuously differentiable on U, then

f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

- The Cauchy integral formula has many important consequences, such as:

  - The identity theorem: If f(z) and g(z) are holomorphic functions on U that agree on a set with an accumulation point, then f(z) = g(z) for all z in U.
  - The maximum modulus principle: If f(z) is a non-constant holomorphic function on U, then |f(z)| attains its maximum only on the boundary of U.
  - The Liouville's theorem: If f(z) is a bounded entire function, then f(z) is constant.
  - The Morera's theorem: If f(z) is a continuous function on U such that the integral of f(z) along any closed curve in U is zero, then f(z) is holomorphic on U.
  - The Taylor series expansion: If f(z) is holomorphic on a disk centered at z_0, then f(z) can be expressed as a power series in z - z_0 with coefficients given by

  f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

  - The residue theorem: If f(z) is a meromorphic function on U, and γ is a positively oriented simple closed curve in U that encloses only isolated singularities of f(z), then

  \oint_\gamma f(z) dz = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, z_k)

  where z_k are the singularities of f(z) inside γ, and Res(f, z_k) are the residues of f(z) at z_k.