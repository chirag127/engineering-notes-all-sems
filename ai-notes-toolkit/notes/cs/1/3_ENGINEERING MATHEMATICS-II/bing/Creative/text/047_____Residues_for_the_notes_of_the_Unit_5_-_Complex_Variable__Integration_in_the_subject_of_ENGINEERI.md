### Residues

- A residue is a complex number that measures the behavior of a meromorphic function near an isolated singularity .
- A meromorphic function is a function that is analytic (holomorphic) everywhere except for a set of isolated points, called poles, where the function becomes infinite .
- An isolated singularity is a point where a function is not defined or not analytic, but it is analytic in some neighborhood around the point .
- The residue of a function f at a point c is denoted by Res(f, c) or Res<sub>c</sub>f  .
- The residue of a function f at a point c is the coefficient of (z - c)<sup>-1</sup> in the Laurent series expansion of f around c  .
- The Laurent series expansion of a function f around a point c is a series of the form f(z) = &Sigma;<sub>n = -&infin;</sub><sup>&infin;</sup> a<sub>n</sub>(z - c)<sup>n</sup>, where a<sub>n</sub> are complex numbers  .
- The residue of a function f at a point c can be calculated by various methods, depending on the nature of the singularity and the form of the function  .
- One method is to find the Laurent series expansion of f around c and identify the coefficient of (z - c)<sup>-1</sup>  .
- Another method is to use the formula Res(f, c) = lim<sub>z &rarr; c</sub> (z - c)f(z), if c is a simple pole of f, i.e. a pole of order one  .
- A third method is to use the formula Res(f, c) = lim<sub>z &rarr; c</sub> d/dz [(z - c)<sup>n</sup>f(z)], if c is a pole of order n of f, i.e. a pole where (z - c)<sup>n</sup>f(z) has a removable singularity  .
- The residue of a function f at a point c is important because it is related to the contour integral of f along a path enclosing c by the Cauchy residue theorem   .
- The Cauchy residue theorem states that if f is a meromorphic function on a simply connected domain D, and &gamma; is a simple closed contour in D that does not pass through any pole of f, then &int;<sub>&gamma;</sub> f(z) dz = 2&pi;i &Sigma;<sub>k = 1</sub><sup>n</sup> Res(f, c<sub>k</sub>), where c<sub>k</sub> are the poles of f inside &gamma;   .
- The Cauchy residue theorem can be used to evaluate contour integrals of meromorphic functions, especially when the contour is a circle or a semicircle   .
- The Cauchy residue theorem can also be extended to the case where the contour is not closed, but has endpoints at infinity, by introducing the concept of residue at infinity   .