# Orthogonal Vectors

- Orthogonal vectors are vectors that are perpendicular to each other, i.e., they form a right angle.
- In Euclidean space, two vectors are orthogonal if and only if their dot product is zero, i.e., they make an angle of 90° (π/2 radians), or one of the vectors is zero.
- A set of vectors is mutually orthogonal if every pair of vectors in the set is orthogonal.
- Orthogonal vectors have some important properties, such as:
  - The length of the projection of a vector onto an orthogonal vector is zero.
  - The Pythagorean theorem holds for orthogonal vectors, i.e., the square of the length of the sum of two orthogonal vectors is equal to the sum of the squares of their lengths.
  - Orthogonal vectors are linearly independent, i.e., they cannot be expressed as linear combinations of each other.
  - A basis of a vector space is called an orthogonal basis if it consists of orthogonal vectors.
  - An orthogonal basis can be normalized to obtain an orthonormal basis, i.e., a basis of unit vectors that are orthogonal to each other.
- To find an orthogonal vector to a given vector, one can use the following methods:
  - In two dimensions, a vector (x, y) is orthogonal to a vector (-y, x) or (y, -x).
  - In three dimensions, a vector (x, y, z) is orthogonal to a vector (y, -x, 0) or (-y, x, 0) or any vector of the form (a, b, -ax-by) where a and b are arbitrary constants.
  - In general, a vector is orthogonal to any vector that is in the null space of its transpose matrix, i.e., the set of solutions to the equation Ax = 0, where A is the matrix obtained by writing the vector as a row.