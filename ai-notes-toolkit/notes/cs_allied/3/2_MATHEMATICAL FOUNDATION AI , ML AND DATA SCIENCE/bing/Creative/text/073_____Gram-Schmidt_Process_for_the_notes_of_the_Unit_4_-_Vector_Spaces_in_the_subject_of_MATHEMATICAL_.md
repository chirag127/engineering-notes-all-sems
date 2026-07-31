### Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space Rn equipped with the standard inner product .
- Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space spanned by the original vectors.
- An orthonormal basis is a basis that has the properties of being linearly independent, orthogonal, and normalized. This means that any vector in the space can be written as a linear combination of the basis vectors with unique coefficients, and that the inner product of any two basis vectors is zero (orthogonal) and the inner product of any basis vector with itself is one (normalized).
- The Gram-Schmidt process can be applied to any finite set of linearly independent vectors, and it can be done in two steps: orthogonalization and normalization.
- Orthogonalization is the process of making the vectors orthogonal to each other, by subtracting the projections of each vector onto the previous ones. Normalization is the process of making the vectors have unit length, by dividing each vector by its norm.
- The Gram-Schmidt process can be written as a formula for each vector in the orthonormal basis, given a set of linearly independent vectors {u1, u2, ..., un}:

  - v1 = u1 / ||u1||
  - v2 = (u2 - <u2, v1>v1) / ||u2 - <u2, v1>v1||
  - v3 = (u3 - <u3, v1>v1 - <u3, v2>v2) / ||u3 - <u3, v1>v1 - <u3, v2>v2||
  - ...
  - vn = (un - <un, v1>v1 - ... - <un, vn-1>vn-1) / ||un - <un, v1>v1 - ... - <un, vn-1>vn-1||

- The Gram-Schmidt process can be used to check whether a set of vectors is linearly independent, by applying the orthogonalization step and seeing if any of the resulting vectors is zero. If so, then the original set of vectors is linearly dependent, and the zero vector can be removed to obtain a linearly independent set.
- The Gram-Schmidt process can also be used to find an orthonormal basis for a subspace of an inner product space, by applying the process to a basis of the subspace. For example, if W is a subspace of Rn, and {w1, w2, ..., wk} is a basis for W, then applying the Gram-Schmidt process to this set will yield an orthonormal basis {v1, v2, ..., vk} for W .
- The Gram-Schmidt process can be stabilized by a small modification; this version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic and introduces smaller errors in finite-precision arithmetic. The modified Gram-Schmidt process can be written as follows:

  - v1 = u1 / ||u1||
  - for i = 2 to n:
    - vi = ui
    - for j = 1 to i-1:
      - vi = vi - <vi, vj>vj
    - vi = vi / ||vi||