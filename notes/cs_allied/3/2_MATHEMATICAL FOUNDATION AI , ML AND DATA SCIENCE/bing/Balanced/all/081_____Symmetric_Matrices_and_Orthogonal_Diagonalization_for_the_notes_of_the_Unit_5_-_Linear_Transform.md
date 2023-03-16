# Symmetric Matrices and Orthogonal Diagonalization

- A matrix A is **symmetric** if A = A^T, where A^T is the transpose of A. This means that A is equal to its mirror image across the main diagonal. Symmetric matrices have some special properties that make them easier to work with than general matrices.
- A matrix A is **diagonalizable** if there exists an invertible matrix P such that P^-1AP is a diagonal matrix D. This means that A can be transformed into a simpler form by a change of basis. Diagonalizable matrices have some nice properties, such as having n linearly independent eigenvectors, where n is the size of the matrix.
- A matrix A is **orthogonally diagonalizable** if there exists an **orthogonal** matrix P such that P^-1AP is a diagonal matrix D. This means that A can be transformed into a simpler form by a change of basis that preserves lengths and angles. Orthogonal matrices have some nice properties, such as having P^-1 = P^T, and having orthonormal columns (i.e., columns that are unit vectors and perpendicular to each other).
- The main result about symmetric matrices and orthogonal diagonalization is the following:

**Theorem:** A matrix A is symmetric if and only if it is orthogonally diagonalizable.

- This theorem tells us that symmetric matrices have a very special structure: they can always be diagonalized by an orthogonal matrix, and conversely, any matrix that can be diagonalized by an orthogonal matrix must be symmetric. This has many applications in mathematics, physics, and engineering, such as finding the principal axes of inertia of a rigid body, or finding the best fit line or plane for a set of data points.
- To prove this theorem, we need to use some facts about eigenvalues and eigenvectors of symmetric matrices. Recall that an eigenvalue of a matrix A is a scalar λ such that there exists a nonzero vector x satisfying Ax = λx. Such a vector x is called an eigenvector of A corresponding to λ. The set of all eigenvectors of A corresponding to λ, together with the zero vector, is called the eigenspace of A for λ, and is denoted by E_λ.
- The following are some facts about eigenvalues and eigenvectors of symmetric matrices:

**Fact 1:** The eigenvalues of a symmetric matrix are real numbers.

**Fact 2:** The eigenspaces of a symmetric matrix are orthogonal to each other. That is, if λ and μ are distinct eigenvalues of a symmetric matrix A, and x is an eigenvector of A for λ, and y is an eigenvector of A for μ, then x and y are perpendicular to each other.

**Fact 3:** The eigenvectors of a symmetric matrix can be chosen to be orthonormal. That is, for each eigenvalue λ of a symmetric matrix A, we can find a basis for E_λ consisting of unit vectors that are perpendicular to each other. Moreover, we can do this for all eigenvalues simultaneously, so that we get a basis for the whole space consisting of orthonormal eigenvectors of A.

- Using these facts, we can prove the theorem as follows:

**Proof:**

(=>) Suppose A is symmetric. We want to show that A is orthogonally diagonalizable. By Fact 3, we can find a basis for the whole space consisting of orthonormal eigenvectors of A. Let P be the matrix whose columns are these eigenvectors. Then P is an orthogonal matrix, since its columns are orthonormal. Moreover, P^-1AP is a diagonal matrix, since each column of P is an eigenvector of A, and the diagonal entries are the corresponding eigenvalues. Therefore, A is orthogonally diagonalizable.

(<=) Suppose A is orthogonally diagonalizable. We want to show that A is symmetric. Let P be an orthogonal matrix such that P^-1AP is a diagonal matrix D. Then we have A = PDP^-1 = PDPT, since P^-1 = PT. Taking the transpose of both sides, we get A^T = (PDPT)^T = (PT)^T D^T P^T = PDPT = A, since D is diagonal and P is orthogonal. Therefore, A is symmetric.