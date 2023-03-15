# Hermitian Matrix

- A Hermitian matrix is a complex square matrix that is equal to its own conjugate transpose. That is, if A is a Hermitian matrix, then A = A^H, where A^H denotes the conjugate transpose of A.
- The conjugate transpose of a matrix is obtained by taking the transpose of the matrix and then replacing each element by its complex conjugate. For example, if A = [[1 + i, 2 - i], [3 + 2i, 4 - i]], then A^H = [[1 - i, 3 - 2i], [2 + i, 4 + i]].
- A Hermitian matrix has the following properties :
  - It has only real eigenvalues.
  - It has orthogonal eigenvectors, which can be chosen to form an orthonormal basis of the vector space.
  - It is diagonalizable by a unitary matrix, that is, A = UDU^H, where U is a unitary matrix and D is a diagonal matrix with the eigenvalues of A on the diagonal.
  - It is symmetric with respect to the real inner product, that is, <Ax, y> = <x, Ay> for any vectors x and y, where <.,.> denotes the real inner product.
- Some examples of Hermitian matrices are:
  - The identity matrix I, which is also a unitary matrix.
  - The Pauli matrices, which are used in quantum mechanics. They are given by:

  ```
  sigma_1 = [[0, 1], [1, 0]]
  sigma_2 = [[0, -i], [i, 0]]
  sigma_3 = [[1, 0], [0, -1]]
  ```

  - Any real symmetric matrix, which is also a Hermitian matrix. For example, A = [[2, 3], [3, 4]] is a real symmetric and Hermitian matrix.