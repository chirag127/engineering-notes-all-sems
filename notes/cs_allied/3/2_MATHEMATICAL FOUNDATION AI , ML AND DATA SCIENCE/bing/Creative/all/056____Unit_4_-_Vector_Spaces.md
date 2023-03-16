## Unit 4 - Vector Spaces

A vector space is a set of objects called vectors, which can be added together and multiplied by scalars, satisfying certain axioms. 

Some examples of vector spaces are:

- The set of all real numbers, denoted by R, is a vector space over itself, with addition and multiplication as the operations.
- The set of all n-tuples of real numbers, denoted by R^n, is a vector space over R, with component-wise addition and scalar multiplication as the operations.
- The set of all polynomials of degree at most n, denoted by P_n, is a vector space over R, with polynomial addition and scalar multiplication as the operations.
- The set of all functions from a set X to R, denoted by F(X), is a vector space over R, with point-wise addition and scalar multiplication as the operations.

The axioms that a vector space must satisfy are:

- Closure under addition: For any two vectors u and v in the vector space, u + v is also in the vector space.
- Commutativity of addition: For any two vectors u and v in the vector space, u + v = v + u.
- Associativity of addition: For any three vectors u, v and w in the vector space, (u + v) + w = u + (v + w).
- Existence of additive identity: There exists a vector 0 in the vector space, such that for any vector u in the vector space, u + 0 = u.
- Existence of additive inverse: For any vector u in the vector space, there exists a vector -u in the vector space, such that u + (-u) = 0.
- Closure under scalar multiplication: For any scalar c and any vector u in the vector space, c * u is also in the vector space.
- Distributivity of scalar multiplication over vector addition: For any scalar c and any two vectors u and v in the vector space, c * (u + v) = (c * u) + (c * v).
- Distributivity of scalar multiplication over scalar addition: For any two scalars c and d and any vector u in the vector space, (c + d) * u = (c * u) + (d * u).
- Associativity of scalar multiplication: For any two scalars c and d and any vector u in the vector space, (c * d) * u = c * (d * u).
- Existence of multiplicative identity: There exists a scalar 1, such that for any vector u in the vector space, 1 * u = u.

Some important concepts and results related to vector spaces are:

- A subspace of a vector space is a subset of the vector space that is also a vector space under the same operations. A subspace must contain the zero vector, be closed under addition and scalar multiplication, and inherit the axioms from the original vector space.
- A linear combination of a set of vectors is a sum of scalar multiples of those vectors. For example, 3 * u - 2 * v + 5 * w is a linear combination of the vectors u, v and w.
- A span of a set of vectors is the set of all linear combinations of those vectors. For example, the span of the vectors u and v is the set of all vectors of the form c * u + d * v, where c and d are scalars.
- A linearly dependent set of vectors is a set of vectors such that at least one of them can be written as a linear combination of the others. For example, the set {u, v, u + v} is linearly dependent, since u + v can be written as 1 * u + 1 * v.
- A linearly independent set of vectors is a set of vectors such that none of them can be written as a linear combination of the others. For example, the set {u, v, w} is linearly independent, if u, v and w are not coplanar.
- A basis of a vector space is a linearly independent set of vectors that spans the vector space. For example, the set {(1, 0, 0), (0, 1, 0), (0, 0, 1)} is a basis of R^3, since any vector in R^3 can be written as a unique linear combination of these three vectors.
- The dimension of a vector space is the number of vectors in a basis of the vector space. For example, the dimension of R^3 is 3, since any basis of R^3 must contain 3 vectors. The dimension of a vector space is