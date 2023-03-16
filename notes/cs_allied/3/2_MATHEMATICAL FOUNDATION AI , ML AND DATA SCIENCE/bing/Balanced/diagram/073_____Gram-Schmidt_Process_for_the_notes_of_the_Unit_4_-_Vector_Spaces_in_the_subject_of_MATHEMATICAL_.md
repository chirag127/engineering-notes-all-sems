### Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space R^n equipped with the standard inner product.
- Orthonormalizing means transforming a set of linearly independent vectors into a set of orthogonal vectors with unit length, forming an orthonormal basis.
- An orthonormal basis is a basis that is both orthogonal and normalized, meaning that the vectors are perpendicular to each other and have a magnitude of one.
- The Gram-Schmidt process can be used to check whether vectors in a set are linearly independent, to find the orthogonal complement of a subspace, and to simplify calculations involving inner products and norms.
- The Gram-Schmidt process can be stabilized by a small modification, sometimes referred to as modified Gram-Schmidt or MGS, which introduces smaller errors in finite-precision arithmetic.

#### Algorithm

- Given a set of linearly independent vectors {u_1, u_2, ..., u_k} in an inner product space, the Gram-Schmidt process produces a set of orthonormal vectors {v_1, v_2, ..., v_k} that span the same subspace as the original set  .
- The algorithm is as follows:

  - Step 1: Let v_1 = u_1 / ||u_1||, where ||u_1|| is the norm of u_1.
  - Step 2: For each i from 2 to k, do the following:
    - Step 2.1: Let w_i = u_i - proj_W_(i-1) u_i, where W_(i-1) is the subspace spanned by {v_1, v_2, ..., v_(i-1)} and proj_W_(i-1) u_i is the orthogonal projection of u_i onto W_(i-1).
    - Step 2.2: Let v_i = w_i / ||w_i||, where ||w_i|| is the norm of w_i.
  - Step 3: Return the set {v_1, v_2, ..., v_k} as the orthonormal basis.

#### Example

- Suppose we want to orthonormalize the set of vectors {u_1, u_2, u_3} in R^3, where u_1 = (1, 1, 1), u_2 = (1, 0, 1), and u_3 = (0, 1, 1).
- Using the Gram-Schmidt process, we get the following steps:

  - Step 1: Let v_1 = u_1 / ||u_1|| = (1, 1, 1) / sqrt(3) = (1/sqrt(3), 1/sqrt(3), 1/sqrt(3)).
  - Step 2: For i = 2, we have:
    - Step 2.1: Let w_2 = u_2 - proj_W_1 u_2 = (1, 0, 1) - (v_1 * u_2) v_1 = (1, 0, 1) - (2/sqrt(3)) (1/sqrt(3), 1/sqrt(3), 1/sqrt(3)) = (-1/3, -2/3, 1/3).
    - Step 2.2: Let v_2 = w_2 / ||w_2|| = (-1/3, -2/3, 1/3) / sqrt(6/9) = (-sqrt(2)/2, -sqrt(2)/2, sqrt(2)/2).
  - Step 3: For i = 3, we have:
    - Step 3.1: Let w_3 = u_3 - proj_W_2 u_3 = (0, 1, 1) - (v_1 * u_3) v_1 - (v_2 * u_3) v_2 = (0, 1, 1) - (2/sqrt(3)) (1/sqrt(3), 1/sqrt(3), 1/sqrt(3)) - (-1/sqrt(2)) (-sqrt(2)/2,