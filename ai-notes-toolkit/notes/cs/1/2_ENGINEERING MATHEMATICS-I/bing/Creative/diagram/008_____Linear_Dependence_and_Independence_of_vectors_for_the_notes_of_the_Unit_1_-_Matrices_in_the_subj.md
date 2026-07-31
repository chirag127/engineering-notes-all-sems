### Linear Dependence and Independence of Vectors

- A vector is a quantity that has both magnitude and direction. Examples of vectors are displacement, velocity, force, etc.
- A vector can be represented by a directed line segment with an arrow indicating the direction. The length of the line segment is proportional to the magnitude of the vector.
- A vector can also be represented by a column matrix with its components along the x, y, and z axes. For example, the vector v = (2, -3, 4) can be written as

v = 
| 2 |
| -3 |
| 4 |

- A linear combination of vectors is an expression of the form a1v1 + a2v2 + ... + anvn, where a1, a2, ..., an are scalars (constants) and v1, v2, ..., vn are vectors.
- A set of vectors {v1, v2, ..., vn} is said to be linearly dependent if there exist scalars a1, a2, ..., an, not all zero, such that a1v1 + a2v2 + ... + anvn = 0. This means that at least one of the vectors can be written as a linear combination of the others.
- A set of vectors {v1, v2, ..., vn} is said to be linearly independent if the only scalars a1, a2, ..., an that satisfy a1v1 + a2v2 + ... + anvn = 0 are a1 = a2 = ... = an = 0. This means that none of the vectors can be written as a linear combination of the others.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors. It does not make sense to say that a single vector is linearly dependent or independent.
- A set of vectors that contains the zero vector is always linearly dependent, since any nonzero scalar times the zero vector gives the zero vector.
- A set of vectors that contains only one nonzero vector is always linearly independent, since the only scalar that makes the linear combination zero is zero itself.
- A set of vectors that contains more vectors than the dimension of the vector space is always linearly dependent, since there are more unknowns than equations in the linear combination.
- A set of vectors that spans the vector space is linearly independent if and only if it is a basis for the vector space, i.e., it is the smallest set of vectors that can generate any vector in the space by linear combinations.
- To check if a set of vectors is linearly dependent or independent, one can use the following methods:
  - Write the vectors as column matrices and form a matrix with them. Then perform row operations to reduce the matrix to its row echelon form or reduced row echelon form. If the matrix has a row of zeros, then the vectors are linearly dependent. If the matrix has no row of zeros, then the vectors are linearly independent.
  - Write the vectors as column matrices and form a matrix with them. Then find the determinant of the matrix. If the determinant is zero, then the vectors are linearly dependent. If the determinant is nonzero, then the vectors are linearly independent. This method only works for square matrices, i.e., when the number of vectors is equal to the dimension of the vector space.
  - Write the linear combination a1v1 + a2v2 + ... + anvn = 0 as a system of linear equations in the scalars a1, a2, ..., an. Then solve the system using any method, such as substitution, elimination, or matrix methods. If the system has a nontrivial solution, i.e., a solution where not all scalars are zero, then the vectors are linearly dependent. If the system has only the trivial solution, i.e., a solution where all scalars are zero, then the vectors are linearly independent.