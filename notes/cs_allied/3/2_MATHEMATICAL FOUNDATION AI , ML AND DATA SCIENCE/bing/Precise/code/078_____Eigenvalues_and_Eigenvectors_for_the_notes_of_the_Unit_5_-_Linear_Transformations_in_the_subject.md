### Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are important concepts in the study of linear transformations in the subject of Mathematical Foundation for AI, ML, and Data Science. Here are some key points to remember:

1. An eigenvector of a square matrix A is a non-zero vector v such that Av = λv for some scalar λ. This scalar λ is called an eigenvalue of A.

2. The characteristic polynomial of a square matrix A is defined as det(A - λI), where I is the identity matrix of the same size as A. The eigenvalues of A are the roots of the characteristic polynomial.

3. The eigenspace of a matrix A corresponding to an eigenvalue λ is the set of all eigenvectors of A associated with λ, together with the zero vector.

4. The geometric multiplicity of an eigenvalue is the dimension of its eigenspace.

5. The algebraic multiplicity of an eigenvalue is its multiplicity as a root of the characteristic polynomial.

6. A matrix is diagonalizable if and only if the sum of the geometric multiplicities of its eigenvalues is equal to its size.

7. If a matrix is diagonalizable, then it can be written as A = PDP^-1, where D is a diagonal matrix containing the eigenvalues of A, and the columns of P are eigenvectors of A.

8. The eigendecomposition of a matrix is not unique. Different choices of eigenvectors can lead to different diagonalizations.

9. The power of a diagonalizable matrix can be easily computed using its eigendecomposition. If A = PDP^-1, then A^n = PD^nP^-1.

10. The determinant and trace of a matrix are equal to the product and sum of its eigenvalues, respectively.
