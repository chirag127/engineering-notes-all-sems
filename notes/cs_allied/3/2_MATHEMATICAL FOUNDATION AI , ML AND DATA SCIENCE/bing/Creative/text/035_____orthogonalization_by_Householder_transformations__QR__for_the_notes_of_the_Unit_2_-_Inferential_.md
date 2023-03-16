### Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- QR decomposition is a method of orthogonalization that factorizes a matrix A into a product of an orthogonal matrix Q and an upper triangular matrix R, such that A = QR.
- Householder transformations are orthogonal transformations that correspond to reflection through a plane or a hyperplane.
- Householder transformations can be used to perform QR decomposition by reflecting the columns of A onto the coordinate axes, one by one, until R is obtained.
- The advantage of Householder transformations over other methods of orthogonalization, such as Gram-Schmidt, is that they are more stable and accurate in the presence of round-off errors.
- The algorithm for Householder QR decomposition is as follows:

  - For k = 1, ..., n, where n is the number of columns of A:
    - Let x be the k-th column of A below the diagonal, and let e be the unit vector in the direction of the k-th axis.
    - Compute the Householder vector v = sign(x_k) ||x|| e + x, where sign(x_k) is the sign of the first element of x, and ||x|| is the norm of x.
    - Normalize v by dividing it by its norm, v = v / ||v||.
    - Compute the Householder matrix H_k = I - 2 v v^T, where I is the identity matrix and v^T is the transpose of v.
    - Apply the Householder transformation to A by multiplying it on the left by H_k, A = H_k A.
    - The result is an upper triangular matrix R.
  - The orthogonal matrix Q can be obtained by multiplying the inverse of the Householder matrices, Q = H_1^(-1) H_2^(-1) ... H_n^(-1).
  - Alternatively, Q can be computed by applying the Householder transformations to the identity matrix, Q = H_n H_(n-1) ... H_1 I.