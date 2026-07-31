## Unit 4 - Vector Spaces

A vector space is a set of objects called vectors, which can be added together and multiplied by scalars, satisfying certain axioms.

Some examples of vector spaces are:

- The set of all n-tuples of real numbers, denoted by R^n, where addition and scalar multiplication are defined component-wise.
- The set of all polynomials of degree less than or equal to n, denoted by P_n, where addition and scalar multiplication are defined as usual.
- The set of all functions from a set X to a field F, denoted by F^X, where addition and scalar multiplication are defined point-wise.

Some properties of vector spaces are:

- A vector space has a zero vector, denoted by 0, such that for any vector v, v + 0 = 0 + v = v.
- A vector space has additive inverses, such that for any vector v, there exists a vector -v, such that v + (-v) = (-v) + v = 0.
- A vector space is closed under addition and scalar multiplication, meaning that if u and v are vectors and c is a scalar, then u + v and c * v are also vectors.
- A vector space satisfies the commutative and associative laws for addition, and the distributive laws for scalar multiplication, meaning that for any vectors u, v, and w, and scalars c and d, we have:

  - u + v = v + u
  - (u + v) + w = u + (v + w)
  - c * (u + v) = c * u + c * v
  - (c + d) * v = c * v + d * v
  - c * (d * v) = (c * d) * v

Some concepts related to vector spaces are:

- A subspace of a vector space V is a subset of V that is also a vector space under the same operations. A subspace must contain the zero vector, and be closed under addition and scalar multiplication.
- A linear combination of vectors v_1, v_2, ..., v_n is an expression of the form c_1 * v_1 + c_2 * v_2 + ... + c_n * v_n, where c_1, c_2, ..., c_n are scalars. The set of all linear combinations of v_1, v_2, ..., v_n is called the span of v_1, v_2, ..., v_n, and is denoted by span(v_1, v_2, ..., v_n).
- A set of vectors v_1, v_2, ..., v_n is linearly independent if the only linear combination of them that equals the zero vector is the trivial one, where all the scalars are zero. A set of vectors is linearly dependent if it is not linearly independent, meaning that there exists a non-trivial linear combination of them that equals the zero vector.
- A basis of a vector space V is a linearly independent set of vectors that spans V. A basis is not unique, but any two bases of the same vector space have the same number of vectors, called the dimension of V, and denoted by dim(V).
- A coordinate system of a vector space V is a way of assigning a unique n-tuple of scalars, called coordinates, to each vector in V, where n is the dimension of V. A coordinate system is determined by choosing a basis of V, and then expressing each vector as a linear combination of the basis vectors. The coordinates of a vector are the scalars in the linear combination. Different bases may lead to different coordinate systems, but the coordinates of a vector are invariant under a change of basis, meaning that they do not depend on the choice of basis.
- A linear transformation from a vector space V to a vector space W is a function T: V -> W that preserves the vector space operations, meaning that for any vectors u and v in V, and any scalar c, we have:

  - T(u + v) = T(u) + T(v)
  - T(c * v) = c * T(v)

Some properties of linear transformations are:

- A linear transformation T: V -> W is injective (one-to-one) if for any vectors u and v in V, T(u) = T(v) implies u = v. A linear transformation is surjective (onto) if for any vector w in W, there exists a vector v in V such that T(v) = w. A linear transformation is bijective (invertible) if it is both injective and surjective, meaning that it has a unique