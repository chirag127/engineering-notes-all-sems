### Linear Dependence and Independence of Vectors

- A vector is a quantity that has both magnitude and direction. Examples of vectors are displacement, velocity, force, etc.
- A vector can be represented by an arrow whose length is proportional to its magnitude and whose direction is the same as its direction.
- A vector can also be represented by a list of numbers called coordinates or components, which specify the magnitude and direction of the vector in a given coordinate system.
- A vector space is a set of vectors that can be added and multiplied by scalars (numbers) according to certain rules. Examples of vector spaces are the set of all vectors in two-dimensional or three-dimensional space, the set of all polynomials of a given degree, the set of all matrices of a given size, etc.
- A linear combination of vectors is a sum of scalar multiples of the vectors. For example, if u, v, and w are vectors and a, b, and c are scalars, then au + bv + cw is a linear combination of u, v, and w.
- A set of vectors is linearly dependent if there is a nontrivial linear combination of the vectors that equals the zero vector. A nontrivial linear combination means that at least one of the scalars is not zero. For example, the set {u, v, w} is linearly dependent if there exist scalars a, b, and c, not all zero, such that au + bv + cw = 0.
- A set of vectors is linearly independent if the only linear combination of the vectors that equals the zero vector is the trivial one, where all the scalars are zero. For example, the set {u, v, w} is linearly independent if the only solution to the equation au + bv + cw = 0 is a = b = c = 0.
- Linear dependence and independence are properties of a set of vectors, not of individual vectors. It does not make sense to say that a vector is linearly dependent or independent by itself, or that a vector is linearly dependent or independent on another vector.
- The number of vectors in a set is not enough to determine whether the set is linearly dependent or independent. For example, a set of two vectors can be linearly dependent or independent, depending on the vectors. However, some general rules are:
  - A set of one nonzero vector is always linearly independent.
  - A set of two vectors is linearly dependent if and only if one of the vectors is a scalar multiple of the other.
  - A set of more than two vectors is linearly dependent if at least one of the vectors can be written as a linear combination of the others.
  - A set of vectors that contains the zero vector is always linearly dependent.
- To check whether a set of vectors is linearly dependent or independent, one can use the following methods:
  - Write the vectors as columns of a matrix and perform row operations to reduce the matrix to row echelon form. The set of vectors is linearly dependent if and only if there is a row of zeros in the reduced matrix.
  - Write the vectors as rows of a matrix and compute the determinant of the matrix. The set of vectors is linearly dependent if and only if the determinant is zero.
  - Write a linear combination of the vectors equal to the zero vector and solve for the scalars. The set of vectors is linearly dependent if and only if there is a nontrivial solution to the system of equations.
- Linear independence is an important concept in linear algebra because it allows us to determine whether a set of vectors forms a basis for a vector space. A basis is a set of linearly independent vectors that spans the vector space, meaning that every vector in the vector space can be written as a linear combination of the basis vectors. A basis is useful because it provides a coordinate system for the vector space, where each vector can be uniquely represented by its coordinates with respect to the basis.