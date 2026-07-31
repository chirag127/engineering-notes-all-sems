# Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- Orthogonal vectors are those that are perpendicular to each other, meaning their dot product is zero.
- Orthogonal vectors have the property that they are linearly independent and form a basis for the subspace they span.
- Orthogonalization is useful for many applications, such as solving linear systems, finding least squares solutions, computing eigenvalues and eigenvectors, and performing principal component analysis.
- One method for performing orthogonalization is the Householder transformation, which uses reflection to transform a vector into another vector that is orthogonal to a given subspace  .
- A Householder transformation is an orthogonal matrix of the form H = I - 2vv^T, where v is a unit vector and I is the identity matrix.
- A Householder transformation reflects any vector x across the hyperplane that is orthogonal to v, such that Hx = -x if x is parallel to v, and Hx = x if x is orthogonal to v.
- A Householder transformation preserves the length of any vector, since H^T H = I, and thus H is an isometry.
- A Householder transformation can be used to zero out the elements below the diagonal of a matrix A, by choosing v such that Hv = ||v||e_1, where e_1 is the first standard basis vector.
- By applying Householder transformations to each column of A, we can obtain an upper triangular matrix R, such that A = QR, where Q is the product of the Householder transformations and is an orthogonal matrix.
- This is called the QR decomposition of A, and it can be used to solve linear systems, find least squares solutions, and compute eigenvalues and eigenvectors.
- The Householder transformation is preferred over other methods of orthogonalization, such as the Gram-Schmidt process, because it is more numerically stable and less affected by rounding errors  .
- However, the Householder transformation does not produce the orthogonal vectors directly, but rather in a factored form, which requires additional computations to extract them .