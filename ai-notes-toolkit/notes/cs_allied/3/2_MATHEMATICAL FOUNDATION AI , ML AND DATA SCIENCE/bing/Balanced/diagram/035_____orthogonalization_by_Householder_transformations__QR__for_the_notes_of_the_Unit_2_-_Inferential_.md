### Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- Orthogonal vectors are those that are perpendicular to each other, i.e. their dot product is zero.
- Orthogonal vectors have the property that they are linearly independent and form a basis for the subspace they span.
- Orthogonalization is useful for many applications, such as solving linear systems, finding eigenvalues and eigenvectors, and performing least squares regression.
- One method for performing orthogonalization is the Householder transformation, which uses reflection across a plane to transform a vector into another vector that is orthogonal to a given subspace .
- The Householder transformation can be expressed in matrix form as H = I - 2vv^T, where v is a unit normal vector to the plane of reflection, and I is the identity matrix.
- The Householder transformation is an orthogonal matrix, i.e. H^T = H^-1, and it preserves the length of any vector, i.e. ||Hx|| = ||x|| for any x.
- The Householder transformation can be used to perform QR decomposition, which is the process of writing a matrix A as the product of an orthogonal matrix Q and an upper triangular matrix R.
- The QR decomposition can be done by applying successive Householder transformations to the columns of A, such that each column is made orthogonal to the previous ones.
- The QR decomposition is useful for solving linear systems, finding eigenvalues and eigenvectors, and performing least squares regression.
- The Householder transformation is generally more accurate and stable than the Gram-Schmidt process, which is another method for performing orthogonalization using projection  .
- However, the Householder transformation requires more computation and storage, and it does not produce the orthogonal vectors directly, but in a factored form .