### Gram-Schmidt Process

The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space Rn equipped with the standard inner product. Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space.

The Gram-Schmidt process can be applied to any set of linearly independent vectors, and it works by iteratively subtracting the projections of each vector onto the previous ones, and then normalizing the result. The process can be summarized as follows :

- Let u1, u2, ..., un be a set of linearly independent vectors in Rn.
- Let v1, v2, ..., vn be the orthonormal vectors obtained by the Gram-Schmidt process.
- Step 1: Let v1 = u1 / ||u1||, where ||u1|| is the norm of u1.
- Step 2: Let v2 = (u2 - projW1u2) / ||u2 - projW1u2||, where W1 is the space spanned by v1, and projW1u2 is the projection of u2 onto W1, given by projW1u2 = (u2 . v1) / ||v1||^2 * v1, where . denotes the dot product.
- Step 3: Let v3 = (u3 - projW2u3) / ||u3 - projW2u3||, where W2 is the space spanned by v1 and v2, and projW2u3 is the projection of u3 onto W2, given by projW2u3 = (u3 . v1) / ||v1||^2 * v1 + (u3 . v2) / ||v2||^2 * v2.
- Step 4: Repeat the same procedure for the remaining vectors, until vn is obtained.

The Gram-Schmidt process can be stabilized by a small modification; this version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic and introduces smaller errors in finite-precision arithmetic . The modified Gram-Schmidt process can be summarized as follows:

- Let u1, u2, ..., un be a set of linearly independent vectors in Rn.
- Let v1, v2, ..., vn be the orthonormal vectors obtained by the modified Gram-Schmidt process.
- Step 1: Let v1 = u1 / ||u1||.
- Step 2: For i = 2, 3, ..., n, do the following:
  - Let ui = ui - (ui . v1) * v1.
  - Let vi = ui / ||ui||.
- Step 3: For i = 2, 3, ..., n, do the following:
  - For j = i + 1, i + 2, ..., n, do the following:
    - Let uj = uj - (uj . vi) * vi.

The Gram-Schmidt process is useful for finding orthonormal bases for vector spaces, which can simplify many calculations involving inner products, norms, angles, and orthogonality. It can also be used to construct orthogonal polynomials, orthogonal matrices, and QR decomposition .