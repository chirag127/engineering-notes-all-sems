### Linear Dependence and Independence of Vectors

- A vector is an object that has both magnitude and direction, and can be represented by an arrow or a column of numbers.
- A linear combination of vectors is an expression of the form `a1v1 + a2v2 + ... + anvn`, where `a1, a2, ..., an` are scalars (numbers) and `v1, v2, ..., vn` are vectors.
- A set of vectors is linearly dependent if there is a nontrivial linear combination of them that equals the zero vector, i.e., there exist scalars `a1, a2, ..., an`, not all zero, such that `a1v1 + a2v2 + ... + anvn = 0`.
- A set of vectors is linearly independent if the only linear combination of them that equals the zero vector is the trivial one, i.e., the scalars `a1, a2, ..., an` are all zero.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors.
- Linear dependence and independence can be checked by writing the vectors as columns of a matrix and performing row operations to reduce the matrix to echelon form. If the matrix has a row of zeros, then the vectors are linearly dependent. If the matrix has no row of zeros, then the vectors are linearly independent.
- Linear dependence and independence are important concepts in linear algebra, as they determine the existence and uniqueness of solutions to systems of linear equations, the span and dimension of vector spaces, and the basis and rank of matrices.