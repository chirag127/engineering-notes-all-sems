### Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space R^n equipped with the standard inner product .
- Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space spanned by the original vectors.
- An orthonormal basis is a basis that has the properties of being linearly independent, orthogonal, and normalized. This means that each vector in the basis has length one, and the dot product of any two distinct vectors in the basis is zero.
- The Gram-Schmidt process can be applied to any finite set of linearly independent vectors, and it produces a unique orthonormal basis for the same space.
- The Gram-Schmidt process can be described as follows  :

  - Let u_1, u_2, ..., u_k be a set of linearly independent vectors in R^n.
  - Let v_1, v_2, ..., v_k be the orthonormal vectors obtained by the Gram-Schmidt process.
  - Step 1: Let v_1 = u_1 / ||u_1||, where ||u_1|| is the length of u_1.
  - Step 2: Let v_2 = u_2 - proj_W1 u_2, where W_1 is the space spanned by v_1, and proj_W1 u_2 is the orthogonal projection of u_2 onto W_1. Then normalize v_2 by dividing it by its length.
  - Step 3: Let v_3 = u_3 - proj_W2 u_3, where W_2 is the space spanned by v_1 and v_2, and proj_W2 u_3 is the orthogonal projection of u_3 onto W_2. Then normalize v_3 by dividing it by its length.
  - Step k: Let v_k = u_k - proj_Wk-1 u_k, where W_k-1 is the space spanned by v_1, v_2, ..., v_k-1, and proj_Wk-1 u_k is the orthogonal projection of u_k onto W_k-1. Then normalize v_k by dividing it by its length.
  - The resulting vectors v_1, v_2, ..., v_k form an orthonormal basis for the space spanned by u_1, u_2, ..., u_k.

- The Gram-Schmidt process can be stabilized by a small modification; this version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic and introduces smaller errors in finite-precision arithmetic.
- The modified Gram-Schmidt process can be described as follows:

  - Let u_1, u_2, ..., u_k be a set of linearly independent vectors in R^n.
  - Let v_1, v_2, ..., v_k be the orthonormal vectors obtained by the modified Gram-Schmidt process.
  - Step 1: Let v_1 = u_1 / ||u_1||, where ||u_1|| is the length of u_1.
  - Step 2: For i = 2, 3, ..., k, do the following:
    - Let u_i = u_i - sum_{j=1}^{i-1} <u_i, v_j> v_j, where <u_i, v_j> is the dot product of u_i and v_j, and sum_{j=1}^{i-1} <u_i, v_j> v_j is the sum of the orthogonal projections of u_i onto v_1, v_2, ..., v_i-1.
    - Let v_i = u_i / ||u_i||, where ||u_i|| is the length of u_i.
  - The resulting vectors v_1, v_2, ..., v_k form an orthonormal basis for the space spanned by u_1, u_2, ..., u_k.

- The Gram-Schmidt process and the modified Gram-Schmidt process are useful for finding orthonormal bases, which have many applications in linear algebra, such as simplifying calculations, solving systems of linear equations, diagonalizing matrices, performing orthogonal transformations