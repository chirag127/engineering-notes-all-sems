### Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are important concepts in the study of linear transformations in the subject of Mathematical Foundation for AI, ML and Data Science. Here are some key points to remember:

1. An eigenvector of a square matrix A is a non-zero vector v such that Av = λv for some scalar λ. This scalar λ is called an eigenvalue of A.
2. The characteristic polynomial of a square matrix A is defined as det(A - λI), where I is the identity matrix of the same size as A.
3. The eigenvalues of a matrix A are the roots of its characteristic polynomial.
4. The eigenvectors of a matrix A corresponding to an eigenvalue λ are the non-zero solutions of the equation (A - λI)v = 0.
5. The geometric multiplicity of an eigenvalue is the dimension of the eigenspace corresponding to that eigenvalue. The algebraic multiplicity of an eigenvalue is its multiplicity as a root of the characteristic polynomial.
6. A matrix is diagonalizable if and only if the sum of the geometric multiplicities of its eigenvalues is equal to its size.
7. If a matrix is diagonalizable, it can be written as A = PDP^-1, where D is a diagonal matrix containing the eigenvalues of A on its diagonal, and the columns of P are the eigenvectors of A.
8. The eigendecomposition of a matrix can be used to compute its powers, its determinant, and its inverse (if it exists).

These are some of the key points to remember when studying eigenvalues and eigenvectors in the context of linear transformations. It is important to understand these concepts and their properties in order to apply them effectively in the field of AI, ML and Data Science.