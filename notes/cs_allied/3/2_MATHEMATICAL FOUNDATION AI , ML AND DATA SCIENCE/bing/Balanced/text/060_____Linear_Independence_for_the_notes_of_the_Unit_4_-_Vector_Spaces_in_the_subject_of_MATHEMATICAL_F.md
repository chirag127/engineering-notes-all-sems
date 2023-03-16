### Linear Independence

- A set of vectors is said to be **linearly independent** if none of the vectors can be written as a linear combination of the others.
- In other words, a set of vectors is linearly independent if the only solution to the equation `c1v1 + c2v2 + ... + cnvn = 0` is `c1 = c2 = ... = cn = 0`, where `c1, c2, ..., cn` are scalars and `v1, v2, ..., vn` are vectors.
- A set of vectors is **linearly dependent** if it is not linearly independent, i.e., if there exists a non-trivial solution to the equation `c1v1 + c2v2 + ... + cnvn = 0`.
- Linear independence is a property of a set of vectors, not of a single vector. A single vector is linearly independent if and only if it is non-zero.
- Some examples of linearly independent and dependent sets of vectors are:

  - The set `{(1, 0), (0, 1)}` is linearly independent, because the only way to write `(1, 0)` as a linear combination of `(0, 1)` is to use zero coefficients, and vice versa.
  - The set `{(1, 2), (2, 4)}` is linearly dependent, because `(2, 4) = 2(1, 2)`, so there is a non-zero coefficient that makes the linear combination equal to zero.
  - The set `{(1, 0, 0), (0, 1, 0), (0, 0, 1)}` is linearly independent, because the only way to write any of these vectors as a linear combination of the others is to use zero coefficients.
  - The set `{(1, 0, 0), (0, 1, 0), (1, 1, 0)}` is linearly dependent, because `(1, 1, 0) = (1, 0, 0) + (0, 1, 0)`, so there are non-zero coefficients that make the linear combination equal to zero.

- Linear independence is related to the concepts of **span**, **basis**, and **dimension** of a vector space, which will be discussed in the next sections.