### Linear Dependence and Independence of Vectors

- A vector is a quantity that has both magnitude and direction. Examples of vectors are displacement, velocity, force, etc.
- A vector can be represented by an arrow whose length is proportional to its magnitude and whose direction is the same as its direction.
- A vector can also be represented by a list of numbers called components, which indicate how much the vector moves along each coordinate axis. For example, the vector (3, 4) moves 3 units along the x-axis and 4 units along the y-axis.
- A vector space is a set of vectors that can be added and multiplied by scalars (numbers) according to certain rules. For example, the set of all vectors in the plane is a vector space, denoted by R^2.
- A linear combination of vectors is a sum of scalar multiples of vectors. For example, 2(3, 4) + (-1)(1, 2) = (5, 6) is a linear combination of the vectors (3, 4) and (1, 2).
- A set of vectors is linearly dependent if there is a nontrivial linear combination of them that equals the zero vector. For example, the set {(1, 2), (2, 4)} is linearly dependent because 2(1, 2) + (-1)(2, 4) = (0, 0).
- A set of vectors is linearly independent if the only linear combination of them that equals the zero vector is the trivial one, where all the scalars are zero. For example, the set {(1, 0), (0, 1)} is linearly independent because the only way to get (0, 0) from them is by multiplying both by zero.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors. It does not make sense to say that a vector is linearly dependent or independent by itself.
- To check if a set of vectors is linearly dependent or independent, one can use the following methods:
  - Write the vectors as the columns of a matrix and perform row operations to reduce the matrix to row echelon form. If the matrix has a row of zeros, then the vectors are linearly dependent. If the matrix has no row of zeros, then the vectors are linearly independent.
  - Write the vectors as the rows of a matrix and find the determinant of the matrix. If the determinant is zero, then the vectors are linearly dependent. If the determinant is nonzero, then the vectors are linearly independent.
  - Write the linear combination of the vectors that equals the zero vector and solve for the scalars. If there is a nontrivial solution, then the vectors are linearly dependent. If the only solution is the trivial one, then the vectors are linearly independent.