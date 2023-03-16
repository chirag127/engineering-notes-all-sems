# Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space Rn equipped with the standard inner product .
- Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space spanned by the original vectors .
- An orthonormal basis is a basis that has two properties: orthogonality and normality. Orthogonality means that any two vectors in the basis are perpendicular to each other, i.e., their inner product is zero. Normality means that each vector in the basis has unit length, i.e., its norm is one .
- The Gram-Schmidt process can be applied to any set of linearly independent vectors, i.e., vectors that are not scalar multiples of each other or linear combinations of each other .
- The Gram-Schmidt process can be used to check whether vectors in a set are linearly independent, to create an orthonormal basis for a subspace, to find the orthogonal complement of a subspace, and to perform orthogonal projection of a vector onto a subspace  .
- The Gram-Schmidt process can be performed in two ways: the classical Gram-Schmidt or the modified Gram-Schmidt. The classical Gram-Schmidt is simpler and more intuitive, but it can introduce numerical errors in finite-precision arithmetic. The modified Gram-Schmidt is more stable and accurate, but it requires more computations .

## Classical Gram-Schmidt

- The classical Gram-Schmidt process takes a set of linearly independent vectors {u1, u2, ..., un} and produces a set of orthonormal vectors {v1, v2, ..., vn} that span the same space as the original vectors .
- The process works as follows:

  - Step 1: Let v1 = u1 / ||u1||, where ||u1|| is the norm of u1. This ensures that v1 is a unit vector in the same direction as u1 .
  - Step 2: Let v2 = u2 - projW1u2, where W1 is the space spanned by v1, and projW1u2 is the orthogonal projection of u2 onto W1. This ensures that v2 is orthogonal to v1. Then, normalize v2 by dividing it by its norm, i.e., v2 = v2 / ||v2|| .
  - Step 3: Let v3 = u3 - projW2u3, where W2 is the space spanned by v1 and v2, and projW2u3 is the orthogonal projection of u3 onto W2. This ensures that v3 is orthogonal to v1 and v2. Then, normalize v3 by dividing it by its norm, i.e., v3 = v3 / ||v3|| .
  - Step 4: Repeat the same procedure for the remaining vectors, i.e., let vk = uk - projWk-1uk, where Wk-1 is the space spanned by v1, v2, ..., vk-1, and projWk-1uk is the orthogonal projection of uk onto Wk-1. Then, normalize vk by dividing it by its norm, i.e., vk = vk / ||vk|| .
  - Step 5: The resulting set of vectors {v1, v2, ..., vn} is an orthonormal basis for the space spanned by {u1, u2, ..., un} .

## Modified Gram-Schmidt

- The modified Gram-Schmidt process is a variation of the classical Gram-Schmidt process that avoids the accumulation of numerical errors due to finite-precision arithmetic .
- The modified Gram-Schmidt process works as follows:

  - Step 1: Let v1 = u1 / ||u1||, where ||u1|| is the norm of u1. This ensures that v1 is a unit vector in