### Residues

In the context of complex analysis, a residue is a complex number that describes the behavior of line integrals of a meromorphic function around a singularity. More specifically, the residue of a meromorphic function at an isolated singularity is the unique complex number such that the function can be written as the sum of its Laurent series and a principal part, which is a finite sum of terms of the form $c_k/(z-z_0)^k$ for positive integers $k$.

Some important properties and results related to residues are:

1. The residue of a function at a pole of order $n$ is equal to the coefficient of the $(n-1)$-th term in the Laurent series expansion of the function around the pole.
2. The residue theorem states that if $f$ is a meromorphic function inside and on a positively oriented simple closed contour $C$, and $a_1, a_2, \dots, a_n$ are the singularities of $f$ inside $C$, then
$$
\oint_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, a_k),
$$
where $\text{Res}(f, a_k)$ denotes the residue of $f$ at $a_k$.
3. The argument principle relates the change in the argument of a meromorphic function along a closed contour to the number of zeros and poles of the function inside the contour. Specifically, if $f$ is a meromorphic function inside and on a positively oriented simple closed contour $C$, and $N$ and $P$ denote the number of zeros and poles of $f$ inside $C$, respectively, counted with multiplicity, then
$$
\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} dz = N - P.
$$
4. The residue calculus can be used to evaluate real integrals using complex analysis. For example, the integral of a real-valued function $f(x)$ over the real line can be expressed as a contour integral over a suitable contour in the complex plane, and the value of the integral can be computed using the residue theorem.
