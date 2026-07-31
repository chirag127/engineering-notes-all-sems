# Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space Rn equipped with the standard inner product .
- Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space spanned by the original vectors.
- An orthonormal basis is a basis that has the properties of being linearly independent, orthogonal, and normalized. This means that any vector in the space can be written as a linear combination of the basis vectors with unique coefficients, and that the inner product of any two basis vectors is zero (orthogonal) and the inner product of any basis vector with itself is one (normalized).
- The Gram-Schmidt process can be applied to any finite set of linearly independent vectors, and it can be done in two steps: orthogonalization and normalization.
- Orthogonalization is the process of making the vectors orthogonal to each other, by subtracting the projections of each vector onto the previous ones. Normalization is the process of making the vectors have unit length, by dividing each vector by its norm.
- The Gram-Schmidt process can be written as a formula for each vector in the orthonormal basis, as follows:

  - Let u1, u2, ..., un be the original set of linearly independent vectors, and let v1, v2, ..., vn be the orthonormal basis obtained by the Gram-Schmidt process.
  - Then, for each i from 1 to n, we have:

    - v1 = u1 / ||u1||
    - vi = (ui - projWi-1ui) / ||ui - projWi-1ui||, for i > 1, where Wi-1 is the space spanned by v1, v2, ..., vi-1, and projWi-1ui is the projection of ui onto Wi-1.

- The Gram-Schmidt process can be used to check whether vectors in a set are linearly independent, by applying the process and seeing if any of the resulting vectors is zero. If so, then the original set is linearly dependent, and the zero vector corresponds to the linear combination of the previous vectors that gives zero.
- The Gram-Schmidt process can also be used to find an orthonormal basis for a subspace of an inner product space, by applying the process to a basis of the subspace.
- The Gram-Schmidt process can be stabilized by a small modification, which reduces the errors introduced by finite-precision arithmetic. This version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic .
- The modified Gram-Schmidt process can be written as follows:

  - Let u1, u2, ..., un be the original set of linearly independent vectors, and let v1, v2, ..., vn be the orthonormal basis obtained by the modified Gram-Schmidt process.
  - Then, for each i from 1 to n, we have:

    - v1 = u1 / ||u1||
    - ui = ui - (vi * ui) vi, for i > 1 and for each j from 1 to i - 1, where * denotes the inner product.
    - vi = ui / ||ui||, for i > 1.

- The modified Gram-Schmidt process is more stable than the original one, because it avoids the accumulation of errors in the projections, and it updates the vectors as soon as they are orthogonalized.