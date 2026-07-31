### Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- Orthogonal vectors are those that are perpendicular to each other, i.e. their dot product is zero.
- Orthogonal vectors have the property that they are linearly independent and form a basis for the subspace they span.
- Orthogonalization is useful for many applications, such as solving linear systems, finding least squares solutions, computing eigenvalues and eigenvectors, etc.
- One method for performing orthogonalization is the Householder transformation, which uses reflection across a hyperplane to zero out some components of a vector.
- A Householder transformation can be expressed as a matrix of the form H = I - 2vv^T, where v is a unit normal vector to the hyperplane of reflection, and I is the identity matrix.
- A Householder transformation is an orthogonal matrix, i.e. H^T = H^-1, and preserves the length of any vector, i.e. ||Hx|| = ||x|| for any x.
- A Householder transformation can be used to orthogonalize a set of vectors by applying it successively to each vector and subtracting its projection onto the previous orthogonal vectors.
- This process is equivalent to finding the QR decomposition of a matrix A, where A = QR, Q is an orthogonal matrix whose columns are the orthogonalized vectors, and R is an upper triangular matrix whose diagonal entries are the lengths of the orthogonalized vectors.
- The QR decomposition can be computed efficiently by using the Householder transformation to introduce zeros into the lower triangle of A, and storing the vectors v in the lower triangle of R.
- The QR decomposition can be used to solve linear systems, find least squares solutions, compute eigenvalues and eigenvectors, etc. by exploiting the properties of Q and R.