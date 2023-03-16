### Definition of Eigenvalue and Eigenvector

- An eigenvalue is a scalar value that satisfies the equation **Ax = λx**, where **A** is a square matrix, **x** is a nonzero vector, and **λ** is a scalar.
- An eigenvector is a nonzero vector that satisfies the equation **Ax = λx**, where **A** is a square matrix, **x** is a vector, and **λ** is a scalar.
- The scalar **λ** is called an eigenvalue of **A**, and the vector **x** is called an eigenvector of **A** corresponding to **λ**.
- An eigenvalue and its corresponding eigenvector are also called an eigenpair of **A**.
- The set of all eigenvalues of **A** is called the spectrum of **A**.
- The set of all eigenvectors of **A** corresponding to a given eigenvalue **λ** is called the eigenspace of **A** associated with **λ**.
- The dimension of the eigenspace of **A** associated with **λ** is called the geometric multiplicity of **λ**.
- The number of times **λ** appears as a root of the characteristic polynomial of **A** is called the algebraic multiplicity of **λ**.
- The algebraic multiplicity of an eigenvalue is always greater than or equal to its geometric multiplicity.
- An eigenvalue is called simple if its algebraic multiplicity is one, and repeated if its algebraic multiplicity is greater than one.
- A square matrix **A** is called diagonalizable if it has a basis of eigenvectors, that is, if there exists a matrix **P** such that **P**<sup>-1</sup>**AP** is a diagonal matrix.
- A square matrix **A** is diagonalizable if and only if the sum of the geometric multiplicities of its eigenvalues is equal to its size, that is, if and only if for every eigenvalue **λ** of **A**, the geometric multiplicity of **λ** is equal to the algebraic multiplicity of **λ**.
- A square matrix **A** is called invertible if there exists a matrix **B** such that **AB** = **BA** = **I**, where **I** is the identity matrix. An invertible matrix is also called nonsingular, and a non-invertible matrix is called singular.
- A square matrix **A** is invertible if and only if zero is not an eigenvalue of **A**.