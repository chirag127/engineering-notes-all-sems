### Gram-Schmidt Process

The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space Rn equipped with the standard inner product. Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space.

The Gram-Schmidt process can be applied to any set of linearly independent vectors, and it produces an orthonormal basis that spans the same subspace as the original set. The process can be described as follows:

- Let u1, u2, ..., un be a set of linearly independent vectors in Rn.
- Let v1 = u1 / ||u1||, where ||u1|| is the norm of u1. This is the first orthonormal vector in the basis.
- For each i from 2 to n, do the following steps:
  - Let wi = ui - projWi-1ui, where projWi-1ui is the projection of ui onto the subspace Wi-1 spanned by v1, v2, ..., vi-1. This is the orthogonalization step, which makes wi orthogonal to all the previous vectors in the basis.
  - Let vi = wi / ||wi||, where ||wi|| is the norm of wi. This is the normalization step, which makes vi a unit vector.
- The resulting set of vectors v1, v2, ..., vn is an orthonormal basis for the subspace spanned by u1, u2, ..., un.

The Gram-Schmidt process can be used to check whether a set of vectors is linearly independent, by verifying that none of the wi vectors is zero. It can also be used to find the orthogonal complement of a subspace, by applying the process to a basis of the subspace and then taking the remaining vectors as a basis of the orthogonal complement.

The Gram-Schmidt process can be stabilized by a small modification; this version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic and introduces smaller errors in finite-precision arithmetic. The modification is to replace the projection step with the following:

- For each i from 2 to n, do the following steps:
  - Let wi = ui.
  - For each j from 1 to i-1, do the following:
    - Let wi = wi - <wi, vj> vj, where <wi, vj> is the inner product of wi and vj. This is the orthogonalization step, which makes wi orthogonal to all the previous vectors in the basis.
  - Let vi = wi / ||wi||, where ||wi|| is the norm of wi. This is the normalization step, which makes vi a unit vector.

The modified Gram-Schmidt process is more numerically stable because it avoids subtracting nearly parallel vectors, which can cause loss of precision. It also avoids computing the norms of the intermediate vectors, which can be expensive. However, it requires more inner product computations than the original process.