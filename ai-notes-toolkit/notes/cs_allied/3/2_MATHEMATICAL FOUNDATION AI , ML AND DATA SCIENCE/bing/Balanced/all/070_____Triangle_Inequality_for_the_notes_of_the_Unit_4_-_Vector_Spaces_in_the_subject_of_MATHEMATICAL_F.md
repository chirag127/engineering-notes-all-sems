# Triangle Inequality

- The triangle inequality is a property of vectors that states that the norm (or length) of the sum of two vectors is less than or equal to the sum of their norms.
- Mathematically, for any two vectors **u** and **v** in a vector space, we have:

  `||u + v|| ≤ ||u|| + ||v||`

- The equality holds if and only if **u** and **v** are linearly dependent, that is, one is a scalar multiple of the other.
- The triangle inequality can be derived from the Cauchy-Schwarz inequality, which states that for any two vectors **u** and **v** in an inner product space, we have:

  `|<u, v>| ≤ ||u|| ||v||`

- The Cauchy-Schwarz inequality can be proved by using the fact that the inner product is positive definite, that is, for any non-zero vector **x**, we have:

  `<x, x> > 0`

- To prove the triangle inequality, we can use the following steps:

  - Square both sides of the inequality and expand the terms using the properties of the norm and the inner product:

    `||u + v||^2 = <u + v, u + v> = ||u||^2 + 2<u, v> + ||v||^2`

    `(||u|| + ||v||)^2 = ||u||^2 + 2||u|| ||v|| + ||v||^2`

  - Subtract `||u||^2 + ||v||^2` from both sides and rearrange the terms:

    `||u + v||^2 - (||u|| + ||v||)^2 = -2(<u, v> - ||u|| ||v||)`

  - Apply the Cauchy-Schwarz inequality to the right-hand side:

    `||u + v||^2 - (||u|| + ||v||)^2 ≤ -2(|<u, v>| - ||u|| ||v||) ≤ 0`

  - Take the square root of both sides and reverse the inequality sign:

    `||u + v|| ≥ ||u|| + ||v||`

- The triangle inequality can be interpreted geometrically as follows:

  - If we consider **u** and **v** as two sides of a triangle, then **u + v** is the third side of the triangle.
  - The triangle inequality says that the length of the third side is always less than or equal to the sum of the lengths of the other two sides.
  - This is a basic property of any triangle in Euclidean geometry.
  - The equality holds if and only if the triangle is degenerate, that is, the three sides are collinear.