### Triangle Inequality

- The triangle inequality is a property of vectors that states that the norm (or length) of the sum of two vectors is less than or equal to the sum of their norms.
- Mathematically, for any two vectors **u** and **v** in a vector space, we have:

  `||u + v|| ≤ ||u|| + ||v||`

- The equality holds if and only if **u** and **v** are linearly dependent, that is, one is a scalar multiple of the other.
- The triangle inequality can be derived from the Cauchy-Schwarz inequality, which states that for any two vectors **u** and **v** in an inner product space, we have:

  `|<u, v>| ≤ ||u|| ||v||`

- The Cauchy-Schwarz inequality implies that the angle between two vectors is always less than or equal to 90 degrees, and the equality holds if and only if the vectors are orthogonal, that is, their inner product is zero.
- To prove the triangle inequality, we can use the following steps:

  1. Square both sides of the inequality and expand the norms using the definition of the inner product:

     `||u + v||^2 ≤ (||u|| + ||v||)^2`

     `||u||^2 + 2<u, v> + ||v||^2 ≤ ||u||^2 + 2||u|| ||v|| + ||v||^2`

  2. Subtract `||u||^2 + ||v||^2` from both sides and rearrange the terms:

     `2<u, v> ≤ 2||u|| ||v||`

     `<u, v> ≤ ||u|| ||v||`

  3. Apply the Cauchy-Schwarz inequality to the right-hand side and obtain the desired result:

     `<u, v> ≤ |<u, v>| ≤ ||u|| ||v||`

- The triangle inequality can be interpreted geometrically as follows: if we consider **u** and **v** as two sides of a triangle, then the third side is **u + v**, and the length of the third side is always less than or equal to the sum of the lengths of the other two sides. This is illustrated in the figure below:

  ```
  u
  /\
 /  \
/    \ v
\    /
 \  /
  \/
  u + v
  ```

- The triangle inequality is useful for measuring distances and angles between vectors, as well as for proving other properties of vector spaces, such as the Cauchy-Schwarz inequality itself, the parallelogram law, and the Pythagorean theorem.