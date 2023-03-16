# Singular Value Decomposition (SVD)

- Singular value decomposition (SVD) is a factorization of a real or complex matrix into three matrices .
- It generalizes the eigendecomposition of a square normal matrix with an orthonormal eigenbasis to any matrix.
- It is related to the polar decomposition.
- It has some interesting algebraic properties and conveys important geometrical and theoretical insights about linear transformations.
- It also has some important applications in data science.

## SVD Factorization

- Given a matrix A of size m x n, the SVD factorization is A = UDV^T, where   :
  - U is an m x m orthogonal matrix, whose columns are called left singular vectors of A.
  - D is an m x n diagonal matrix, whose diagonal elements are called singular values of A. The singular values are non-negative and arranged in descending order.
  - V is an n x n orthogonal matrix, whose columns are called right singular vectors of A.
  - V^T is the transpose of V.
- The SVD factorization can be computed using various numerical algorithms, such as the power method, the QR algorithm, or the Jacobi method .

## SVD Properties

- The SVD factorization reveals the rank, nullity, and range of a matrix A .
  - The rank of A is equal to the number of non-zero singular values in D.
  - The nullity of A is equal to the number of zero singular values in D.
  - The range of A is spanned by the left singular vectors corresponding to the non-zero singular values in U.
  - The null space of A is spanned by the right singular vectors corresponding to the zero singular values in V.
- The SVD factorization also reveals the best low-rank approximation of a matrix A .
  - If A is approximated by a matrix A_k of rank k, where k < min(m, n), then the optimal choice of A_k is given by U_k D_k V_k^T, where U_k, D_k, and V_k are obtained by keeping only the first k columns of U, D, and V, respectively.
  - The approximation error is minimized by the Frobenius norm or the 2-norm, and is equal to the sum of the squared singular values or the largest singular value that are discarded, respectively.
- The SVD factorization also reveals the least squares solution of an overdetermined or underdetermined system of linear equations .
  - If A is an m x n matrix with m > n and b is an m x 1 vector, then the system Ax = b may have no exact solution, but the least squares solution x_hat that minimizes the 2-norm of the residual r = b - Ax is given by x_hat = V D^-1 U^T b, where D^-1 is obtained by taking the reciprocal of the non-zero singular values in D and setting the rest to zero.
  - If A is an m x n matrix with m < n and b is an m x 1 vector, then the system Ax = b may have infinitely many solutions, but the least squares solution x_hat that minimizes the 2-norm of x is given by x_hat = V D^-1 U^T b, where D^-1 is obtained by taking the reciprocal of the non-zero singular values in D and setting the rest to zero.

## SVD Applications

- The SVD factorization has many applications in data science, such as :
  - Dimensionality reduction: By using the low-rank approximation of a matrix, one can reduce the number of features or observations in a data set, while preserving the most important information.
  - Data compression: By using the low-rank approximation of a matrix, one can reduce the storage space or transmission bandwidth required for a data set, while maintaining a reasonable quality.
  - Image processing: By using the low-rank approximation of a matrix, one can perform various tasks on images, such as denoising, smoothing, edge detection, or face recognition.
  - Recommender systems: By using the low-rank approximation of a matrix, one can model the preferences of users and items, and