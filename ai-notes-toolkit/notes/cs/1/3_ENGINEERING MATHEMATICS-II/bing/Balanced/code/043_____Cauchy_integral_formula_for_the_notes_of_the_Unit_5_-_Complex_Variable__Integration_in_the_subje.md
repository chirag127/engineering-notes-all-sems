### Cauchy integral formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the value of a holomorphic function at a point to its values on a circle around that point.
- The formula can be stated as follows: If f(z) is a holomorphic function on a domain U and γ is a positively oriented simple closed contour in U that encloses a point z_0, then

f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be generalized to higher derivatives of f(z) as well:

f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

- The formula can also be extended to any simply connected domain U by using the homotopy principle: If f(z) is holomorphic on U and γ_1 and γ_2 are two homotopic simple closed contours in U that enclose a point z_0, then

\oint_{\gamma_1} \frac{f(z)}{z-z_0} dz = \oint_{\gamma_2} \frac{f(z)}{z-z_0} dz

- The Cauchy integral formula has many important consequences, such as:

  - The identity theorem: If f(z) and g(z) are holomorphic on a domain U and agree on a set that has a limit point in U, then f(z) = g(z) on U.
  - The maximum modulus principle: If f(z) is holomorphic on a domain U and |f(z)| attains a maximum value on U, then f(z) is constant on U.
  - The Liouville's theorem: If f(z) is holomorphic and bounded on the entire complex plane, then f(z) is constant.
  - The Morera's theorem: If f(z) is continuous on a domain U and satisfies

\oint_\gamma f(z) dz = 0

for any simple closed contour γ in U, then f(z) is holomorphic on U.
  - The Taylor series expansion: If f(z) is holomorphic on a disk D(z_0, r), then f(z) can be expressed as a power series around z_0:

f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n

for any z in D(z_0, r).
  - The residue theorem: If f(z) is holomorphic on a domain U except for a finite number of isolated singularities z_1, z_2, ..., z_n, and γ is a positively oriented simple closed contour in U that encloses all the singularities, then

\oint_\gamma f(z) dz = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, z_k)

where \operatorname{Res}(f, z_k) is the residue of f(z) at z_k, defined as

\operatorname{Res}(f, z_k) = \frac{1}{2\pi i} \oint_{\gamma_k} f(z) dz

where γ_k is a small positively oriented circle around z_k.