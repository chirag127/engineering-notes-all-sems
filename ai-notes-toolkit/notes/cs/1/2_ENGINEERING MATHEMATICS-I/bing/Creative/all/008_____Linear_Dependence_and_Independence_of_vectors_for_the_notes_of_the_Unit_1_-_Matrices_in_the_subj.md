# Linear Dependence and Independence of Vectors

- A vector is a quantity that has both magnitude and direction. Examples of vectors are displacement, velocity, force, etc.
- A vector can be represented by an arrow or by a column matrix of its components.
- A linear combination of vectors is an expression of the form a1v1 + a2v2 + ... + anvn, where a1, a2, ..., an are scalars and v1, v2, ..., vn are vectors.
- A set of vectors is said to be linearly dependent if there exists a nontrivial linear combination of them that equals the zero vector. That is, if there exist scalars a1, a2, ..., an, not all zero, such that a1v1 + a2v2 + ... + anvn = 0.
- A set of vectors is said to be linearly independent if the only linear combination of them that equals the zero vector is the trivial one, where all the scalars are zero. That is, if a1v1 + a2v2 + ... + anvn = 0 implies that a1 = a2 = ... = an = 0.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors. A single vector is always linearly dependent on itself, but it is linearly independent from any other vector.
- A set of vectors that contains the zero vector is always linearly dependent, since any nonzero scalar times the zero vector gives the zero vector.
- To check if a set of vectors is linearly dependent or independent, one can use the following methods:
  - Write the vectors as column matrices and form a matrix by placing them side by side. Then perform row operations to reduce the matrix to its row echelon form. If the row echelon form has a row of zeros, then the set of vectors is linearly dependent. Otherwise, it is linearly independent.
  - Write the vectors as column matrices and form a matrix by placing them side by side. Then find the determinant of the matrix. If the determinant is zero, then the set of vectors is linearly dependent. Otherwise, it is linearly independent.
  - Write the linear combination a1v1 + a2v2 + ... + anvn = 0 as a system of linear equations in the scalars a1, a2, ..., an. Then solve the system using any method. If the system has a nontrivial solution, then the set of vectors is linearly dependent. Otherwise, it is linearly independent.
- Linear dependence and independence are important concepts in linear algebra, as they are related to the notions of span, basis, dimension, rank, nullity, etc.