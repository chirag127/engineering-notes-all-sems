### Linear Dependence and Independence of Vectors

- A vector is an object that has both magnitude and direction, and can be represented by a directed line segment.
- A linear combination of vectors is an expression of the form `a1v1 + a2v2 + ... + anvn`, where `a1, a2, ..., an` are scalars and `v1, v2, ..., vn` are vectors.
- A set of vectors is said to be linearly dependent if there exists a nontrivial linear combination of them that equals the zero vector, i.e., `a1v1 + a2v2 + ... + anvn = 0`, where not all `a1, a2, ..., an` are zero.
- A set of vectors is said to be linearly independent if the only linear combination of them that equals the zero vector is the trivial one, i.e., `a1v1 + a2v2 + ... + anvn = 0`, where all `a1, a2, ..., an` are zero.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors.
- A set of vectors that contains the zero vector is always linearly dependent, since the zero vector can be written as a linear combination of any other vector with a nonzero coefficient.
- A set of vectors that contains only one nonzero vector is always linearly independent, since the only way to write the nonzero vector as a linear combination of itself is with a coefficient of one.
- A set of two or more vectors is linearly dependent if and only if one of the vectors can be written as a linear combination of the others.
- A set of two or more vectors is linearly independent if and only if none of the vectors can be written as a linear combination of the others.
- To check if a set of vectors is linearly dependent or independent, one can use the following methods:
  - Write the vectors as columns of a matrix and perform row operations to reduce the matrix to row echelon form. If the matrix has a row of zeros, then the vectors are linearly dependent. If the matrix has no row of zeros, then the vectors are linearly independent.
  - Write the vectors as rows of a matrix and find the determinant of the matrix. If the determinant is zero, then the vectors are linearly dependent. If the determinant is nonzero, then the vectors are linearly independent.
  - Write the linear combination of the vectors equal to the zero vector and solve the system of equations for the coefficients. If the system has a nontrivial solution, then the vectors are linearly dependent. If the system has only the trivial solution, then the vectors are linearly independent.