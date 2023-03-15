### Cauchy- Integral theorem

- The Cauchy- Integral theorem is a fundamental result in complex analysis that relates the line integral of a holomorphic function over a closed curve to the values of the function inside the curve.
- The theorem states that if f(z) is a holomorphic function defined on a simply connected domain D, and C is a piecewise smooth, simple closed curve in D, then

$$\oint_C f(z) dz = 0$$

- This means that the line integral of f(z) over C does not depend on the choice of C, as long as C is contained in D and does not enclose any singularities of f(z).
- The theorem can be generalized to multiply connected domains by using the concept of homology. A curve C is said to be homologous to zero in D if it is the boundary of a surface contained in D. Then the theorem states that if f(z) is a holomorphic function defined on a domain D, and C is a piecewise smooth, closed curve in D that is homologous to zero, then

$$\oint_C f(z) dz = 0$$

- The theorem can also be extended to functions that are holomorphic on D except for a finite number of isolated singularities. In that case, the theorem states that if f(z) is a holomorphic function defined on a domain D except for a finite number of isolated singularities, and C is a piecewise smooth, simple closed curve in D that does not pass through any singularities of f(z), then

$$\oint_C f(z) dz = 2\pi i \sum_{k=1}^n n(C, a_k) \text{Res}(f, a_k)$$

- where n(C, a_k) is the winding number of C around a_k, and Res(f, a_k) is the residue of f(z) at a_k.
- The Cauchy- Integral theorem can be proved using the Cauchy-Riemann equations, the Green's theorem, or the Stokes' theorem. It is a powerful tool for evaluating contour integrals and finding properties of analytic functions, such as their derivatives, Taylor series, Laurent series, and singularities.