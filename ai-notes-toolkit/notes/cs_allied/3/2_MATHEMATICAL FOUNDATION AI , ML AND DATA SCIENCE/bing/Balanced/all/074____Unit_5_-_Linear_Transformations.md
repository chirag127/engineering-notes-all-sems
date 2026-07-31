## Unit 5 - Linear Transformations

- A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication.
- A linear transformation can be represented by a matrix, which encodes the effect of the transformation on the standard basis vectors of the domain and the range.
- The standard matrix of a linear transformation T is denoted by [T] and is defined by [T] = [[T(e1)] [T(e2)] ... [T(en)]], where e1, e2, ..., en are the standard basis vectors of the domain.
- The image of a vector x under a linear transformation T is given by T(x) = [T]x, where [T] is the standard matrix of T and x is a column vector.
- The kernel (or null space) of a linear transformation T is the set of all vectors x in the domain such that T(x) = 0. The kernel is a subspace of the domain.
- The range (or image) of a linear transformation T is the set of all vectors y in the codomain such that y = T(x) for some x in the domain. The range is a subspace of the codomain.
- The rank of a linear transformation T is the dimension of the range of T. The rank is equal to the number of linearly independent columns of [T].
- The nullity of a linear transformation T is the dimension of the kernel of T. The nullity is equal to the number of free variables in the reduced row echelon form of [T].
- The rank-nullity theorem states that for any linear transformation T from R^n to R^m, rank(T) + nullity(T) = n.
- A linear transformation T is one-to-one (or injective) if T(x) = T(y) implies x = y for any x and y in the domain. Equivalently, T is one-to-one if the kernel of T is {0}.
- A linear transformation T is onto (or surjective) if for every y in the codomain, there exists x in the domain such that T(x) = y. Equivalently, T is onto if the range of T is equal to the codomain.
- A linear transformation T is invertible if it is both one-to-one and onto. In this case, there exists a unique linear transformation S such that S(T(x)) = x and T(S(y)) = y for any x in the domain and y in the codomain. S is called the inverse of T and is denoted by T^-1.
- The inverse of a linear transformation T, if it exists, can be found by solving the matrix equation [T][S] = I, where I is the identity matrix. The inverse matrix [S] is then the standard matrix of T^-1.
- A composition of two linear transformations T and S is a linear transformation that maps x to T(S(x)). The composition is denoted by T o S and is read as "T composed with S".
- The standard matrix of a composition of two linear transformations T and S is given by [T o S] = [T][S], where [T] and [S] are the standard matrices of T and S, respectively.
- A linear transformation T is an isometry if it preserves the length and angle of vectors. Equivalently, T is an isometry if T(x) dot T(y) = x dot y for any x and y in the domain, where dot denotes the dot product.
- An isometry T is also called an orthogonal transformation. The standard matrix of an orthogonal transformation [T] satisfies [T]^T[T] = I, where [T]^T is the transpose of [T]. Equivalently, the columns of [T] are orthonormal vectors.