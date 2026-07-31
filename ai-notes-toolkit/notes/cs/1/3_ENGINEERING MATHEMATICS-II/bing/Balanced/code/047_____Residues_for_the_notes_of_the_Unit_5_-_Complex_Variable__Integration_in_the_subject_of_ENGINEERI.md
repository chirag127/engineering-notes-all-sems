### Residues

- A residue is a complex number that measures the behavior of a meromorphic function near an isolated singularity.
- A meromorphic function is a function that is analytic (holomorphic) except for a set of isolated points, called poles, where the function may have a finite or infinite order of singularity.
- A singularity is a point where a function is not defined or not analytic.
- A Laurent series is a power series expansion of a function that may have both positive and negative powers of the variable.
- The residue of a function f at a point c is the coefficient of the term (z-c)^(-1) in the Laurent series expansion of f around c.
- The residue of a function f at a point c is denoted by Res(f,c) or Res_z=c f.
- The residue of a function f at a point c can be calculated by various methods, depending on the nature of the singularity and the function.
- Some common methods are:
  - If f has a simple pole at c, then Res(f,c) = lim_(z->c) (z-c)f(z).
  - If f has a pole of order n at c, then Res(f,c) = (1/(n-1)!) lim_(z->c) d^(n-1)/dz^(n-1) [(z-c)^n f(z)].
  - If f and g are analytic at c, and g(c) = 0 and g'(c) != 0, then Res(f/g,c) = f(c)/g'(c).
  - If f can be written as a ratio of two analytic functions f = P/Q, where P and Q have no common factors, and Q has a simple zero at c, then Res(f,c) = P(c)/Q'(c).
- The residue of a function f at a point c is important because it determines the value of the contour integral of f along a path enclosing c.
- The Cauchy residue theorem states that if f is a meromorphic function on a simply connected domain D, and C is a positively oriented simple closed contour in D that does not pass through any singularity of f, then [integral_C f(z) dz] = 2 pi i [sum_Res(f,c)], where the sum is taken over all the singularities of f inside C.
- The Cauchy residue theorem is a powerful tool for evaluating contour integrals that would otherwise be difficult or impossible to compute.