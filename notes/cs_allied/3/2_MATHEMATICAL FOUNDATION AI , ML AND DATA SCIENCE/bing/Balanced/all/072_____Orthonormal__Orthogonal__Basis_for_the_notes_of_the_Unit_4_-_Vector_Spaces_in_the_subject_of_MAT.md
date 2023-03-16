# Orthonormal (Orthogonal) Basis

- A set of vectors is **orthonormal** if each vector is a **unit vector** (length or norm is equal to 1) and all vectors in the set are **orthogonal** to each other.
- A **basis** is a set of vectors that **spans** a vector space and is **linearly independent**.
- An **orthonormal basis** is a basis that is also orthonormal. Such a basis has the following properties:
  - The inner product of any two basis vectors is zero: <u,v> = 0 for u ≠ v.
  - The inner product of any basis vector with itself is one: <u,u> = 1 for any u.
  - The norm of any basis vector is one: ||u|| = 1 for any u.
  - The matrix formed by the basis vectors as columns is an **orthogonal matrix**, which means its inverse is equal to its transpose.
- An example of an orthonormal basis is the **standard basis** for Euclidean space, which consists of the vectors e1 = (1,0,0,...,0), e2 = (0,1,0,...,0), ..., en = (0,0,0,...,1) for n dimensions.
- Every finite-dimensional inner product space has an orthonormal basis, which may be obtained from an arbitrary basis using the **Gram–Schmidt process**. This process involves taking each vector in the original basis, subtracting its projection onto the previous vectors, and normalizing the result. The process can be summarized as follows:
  - Let v1, v2, ..., vn be a basis for a vector space V with an inner product.
  - Define u1 = v1 / ||v1||, which is a unit vector in the direction of v1.
  - For k = 2, 3, ..., n, define uk = vk - <vk, u1>u1 - <vk, u2>u2 - ... - <vk, uk-1>uk-1, which is the vector vk with the components parallel to the previous vectors removed.
  - Normalize each uk by dividing by its norm: uk = uk / ||uk||.
  - The vectors u1, u2, ..., un form an orthonormal basis for V.