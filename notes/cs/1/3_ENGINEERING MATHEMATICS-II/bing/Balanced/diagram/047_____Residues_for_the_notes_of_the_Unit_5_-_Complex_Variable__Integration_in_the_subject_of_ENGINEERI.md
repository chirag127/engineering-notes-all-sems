### Residues

- A residue is a complex number that measures the behavior of a meromorphic function near a singularity.
- A meromorphic function is a function that is analytic everywhere except for a set of isolated singularities.
- A singularity is a point where a function is not defined or not analytic.
- A residue can be computed from the Laurent series expansion of a function around a singularity.
- A Laurent series is a series of the form

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-c)^n$$

where $c$ is the center of the series and $a_n$ are the coefficients.
- The residue of $f$ at $c$ is the coefficient of the term $(z-c)^{-1}$ in the Laurent series, denoted by $\operatorname{Res}(f,c)$ or $\operatorname{Res}_{z=c} f$.
- The residue can be used to evaluate contour integrals of meromorphic functions using the Cauchy residue theorem .
- The Cauchy residue theorem states that if $f$ is a meromorphic function on a simply connected domain $D$ and $\gamma$ is a closed contour in $D$ that does not pass through any singularity of $f$, then

$$\oint_{\gamma} f(z) dz = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, z_k)$$

where $z_k$ are the singularities of $f$ inside $\gamma$ .
- The residue can also be used to evaluate improper integrals of real functions using the method of residues.
- The method of residues involves extending the real function to a complex function, choosing a suitable contour that encloses the real interval of integration, and applying the Cauchy residue theorem.
- The residue can also be used to study the asymptotic behavior of functions and sequences using the residue at infinity.
- The residue at infinity is defined as the negative of the coefficient of the term $z^{-1}$ in the Laurent series of $f(1/z)$ around $z=0$.
- The residue at infinity can be used to determine the order of growth of a function or a sequence as $z \to \infty$.