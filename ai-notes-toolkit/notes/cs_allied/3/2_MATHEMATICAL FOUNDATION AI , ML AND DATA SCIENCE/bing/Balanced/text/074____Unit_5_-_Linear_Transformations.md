## Unit 5 - Linear Transformations

- A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication.
- A linear transformation can be represented by a matrix, which encodes the effect of the transformation on the standard basis vectors of the domain and the range.
- The standard matrix of a linear transformation T is denoted by [T] and is defined by [T] = [[T(e1)] [T(e2)] ... [T(en)]], where e1, e2, ..., en are the standard basis vectors of the domain.
- The matrix-vector product [T]x can be interpreted as applying the linear transformation T to the vector x, or as taking a linear combination of the columns of [T] with the coefficients from x.
- The domain of a linear transformation T is the set of all vectors that can be input to T, and the range of T is the set of all possible outputs of T.
- The kernel (or null space) of a linear transformation T is the set of all vectors x such that T(x) = 0, and the image (or column space) of T is the span of the columns of [T].
- A linear transformation T is one-to-one if T(x) = T(y) implies x = y, or equivalently, if the kernel of T contains only the zero vector.
- A linear transformation T is onto if every vector in the range of T is the image of some vector in the domain of T, or equivalently, if the image of T is equal to the range of T.
- A linear transformation T is invertible if there exists another linear transformation S such that T(S(x)) = x and S(T(x)) = x for all x, or equivalently, if T is both one-to-one and onto.
- The inverse of a linear transformation T, denoted by T^-1, is the unique linear transformation that satisfies T(T^-1(x)) = x and T^-1(T(x)) = x for all x.
- The inverse of a linear transformation T, if it exists, can be found by solving the matrix equation [T][S] = I, where I is the identity matrix and [S] is the standard matrix of T^-1.
- A linear transformation T preserves the properties of vectors, such as length, angle, and orthogonality, if and only if [T] is an orthogonal matrix, meaning that [T]^-1 = [T]^T, where [T]^T is the transpose of [T].
- Some examples of linear transformations are rotations, reflections, projections, scaling, and shearing.