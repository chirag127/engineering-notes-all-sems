### Cauchy's Residue Theorem and its Application

- Cauchy's residue theorem is a powerful tool to evaluate line integrals of analytic functions over closed curves; it can often be used to compute real integrals and infinite series as well .
- It generalizes the Cauchy integral theorem and Cauchy's integral formula, which state that the integral of an analytic function over a simple closed curve is equal to 2πi times the sum of the values of the function at the interior points of the curve .
- The residue theorem extends this result to the case where the function has isolated singularities inside the curve, which are points where the function is not defined or not analytic .
- The residue of a function f at an isolated singularity z0 is defined as the coefficient of the (z-z0)^-1 term in the Laurent series expansion of f around z0 .
- The residue theorem states that the integral of f over a simple closed curve C that encloses the singularities of f is equal to 2πi times the sum of the residues of f at those singularities .
- The residue theorem can be used to compute real integrals and infinite series by applying it to suitable complex functions and contours .
- For example, to compute the integral of a rational function of sine and cosine over the interval [0, 2π], one can use the residue theorem on the function f(z) = P(e^iz) / Q(e^iz), where P and Q are polynomials, and the contour C is the unit circle .
- Similarly, to compute the sum of an infinite series of the form ∑n=1∞ a_n / n^s, where s is a positive integer and a_n are constants, one can use the residue theorem on the function f(z) = πcot(πz) a_z / z^s, and the contour C is a large rectangle with vertices at ±(N+1/2) ± iR, where N and R are large positive numbers .