# Cauchy Integral Formula

- The Cauchy integral formula is a central statement in complex analysis that relates the values of a holomorphic function inside a disk to the values of that function on the boundary of the disk.
- A function f(z) is holomorphic if it is complex differentiable at every point in its domain.
- The Cauchy integral formula can be stated as follows    :

  - If f(z) is holomorphic in a simply-connected domain U and γ is a positively oriented simple closed contour in U, then for any z_0 inside γ, we have

    f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

  - where the integral is a contour integral along γ.

- The Cauchy integral formula can be extended to higher derivatives of f(z) as follows :

  - If f(z) and γ satisfy the same hypotheses as above, then for any positive integer n, we have

    f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

  - where f^{(n)}(z) denotes the n-th derivative of f(z).

- The Cauchy integral formula has many important consequences and applications in complex analysis, such as the following    :

  - The identity theorem: If f(z) and g(z) are holomorphic in a domain U and agree on a set that has a limit point in U, then f(z) = g(z) for all z in U.
  - The maximum modulus principle: If f(z) is holomorphic in a domain U and continuous on its boundary, then |f(z)| attains its maximum value on the boundary of U.
  - The Liouville's theorem: If f(z) is holomorphic and bounded in the whole complex plane, then f(z) is a constant function.
  - The residue theorem: If f(z) is holomorphic in a simply-connected domain U except for a finite number of isolated singularities, then for any positively oriented simple closed contour γ in U that encloses all the singularities of f(z), we have

    \oint_\gamma f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)

  - where z_k are the singularities of f(z) and \text{Res}(f, z_k) are the residues of f(z) at z_k.