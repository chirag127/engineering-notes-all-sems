# Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- Orthogonal vectors are those that are perpendicular to each other, i.e. their dot product is zero.
- Orthogonal vectors have the property that they are linearly independent and form a basis for the subspace they span.
- Orthogonalization is useful for many applications, such as solving linear systems, finding least squares solutions, computing eigenvalues and eigenvectors, etc.
- One method for performing orthogonalization is the Householder transformation, which uses reflection .
- A Householder transformation is an orthogonal transformation that reflects a vector across a plane or a hyperplane.
- A Householder transformation can be expressed in matrix form as H = I - 2vv^T, where v is a unit normal vector to the plane or hyperplane, and I is the identity matrix.
- A Householder transformation preserves the length of any vector, i.e. ||Hx|| = ||x|| for any vector x.
- A Householder transformation can be used to introduce zeros into a matrix by choosing v such that Hv = ||v||e_1, where e_1 is the first standard basis vector.
- By applying a sequence of Householder transformations to a matrix A, we can obtain a matrix R that is upper triangular, i.e. A = QR, where Q is the product of the Householder matrices, and Q is orthogonal.
- This is called the QR decomposition of A, and it can be used to solve linear systems, find least squares solutions, etc.
- The Householder transformation is usually preferred over another method of orthogonalization, the Gram-Schmidt process, because it is more numerically stable, i.e. rounding errors tend to have less serious effects  .
- The Gram-Schmidt process uses projection to orthogonalize a set of vectors, but it can suffer from loss of orthogonality due to finite precision arithmetic.
- The Householder transformation, on the other hand, does not lose orthogonality, but it requires more computation and storage, and it does not produce the orthogonal vectors directly, but in a factored form .