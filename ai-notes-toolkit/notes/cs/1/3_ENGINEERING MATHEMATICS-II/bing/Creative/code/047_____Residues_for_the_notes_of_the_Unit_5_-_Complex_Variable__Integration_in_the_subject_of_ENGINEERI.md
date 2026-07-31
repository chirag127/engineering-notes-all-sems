### Residues

- A residue is a complex number that measures the behavior of a meromorphic function near an isolated singularity .
- A meromorphic function is a function that is analytic (holomorphic) everywhere except for a set of isolated points, called poles, where the function becomes infinite .
- An isolated singularity is a point where a function is not defined or not analytic, but it is analytic in some neighborhood around the point .
- The residue of a function f at a point c is the coefficient of the term (z-c)^(-1) in the Laurent series expansion of f around c  .
- The Laurent series is a generalization of the Taylor series that allows negative powers of (z-c) in the expansion  .
- The residue of a function f at a point c can be calculated by various methods, depending on the nature of the singularity and the form of the function  .
- Some common methods are:
  - The residue formula: Res(f,c) = lim_(z->c) (z-c) f(z) if c is a simple pole  .
  - The residue theorem: Res(f,c) = 1/(2 pi i) int_C f(z) dz if C is a small positively oriented circle around c   .
  - The residue at infinity: Res(f,infty) = - Res(f,0) if f is a rational function  .
- The residue of a function f at a point c is important because it determines the value of the contour integral of f along a path enclosing c  .
- The Cauchy residue theorem states that if f is a meromorphic function on a simply connected domain D, and C is a positively oriented simple closed contour in D that encloses a finite number of singularities of f, then int_C f(z) dz = 2 pi i sum_(k=1)^n Res(f,c_k) where c_k are the singularities of f inside C  .
- The Cauchy residue theorem is a powerful tool for evaluating contour integrals that are otherwise difficult or impossible to compute  .