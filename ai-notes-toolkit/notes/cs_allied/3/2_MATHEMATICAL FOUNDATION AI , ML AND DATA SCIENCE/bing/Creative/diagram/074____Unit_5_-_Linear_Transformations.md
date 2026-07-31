## Unit 5 - Linear Transformations

A linear transformation is a function that maps vectors from one vector space to another vector space, while preserving the operations of vector addition and scalar multiplication. In other words, a linear transformation is a function T: R^n -> R^m that satisfies the following properties :

- T(x + y) = T(x) + T(y) for any vectors x, y ∈ R^n
- T(a x) = a T(x) for any vector x ∈ R^n and any scalar a ∈ R

Some examples of linear transformations are:

- The zero transformation, which maps every vector to the zero vector: T(x) = 0 for all x
- The identity transformation, which maps every vector to itself: T(x) = x for all x
- The scaling transformation, which multiplies every vector by a constant: T(x) = k x for some k ∈ R
- The projection transformation, which maps every vector to its component along a given direction: T(x) = (x · u) u for some unit vector u
- The rotation transformation, which rotates every vector by a given angle: T(x) = R x for some rotation matrix R

Some properties of linear transformations are :

- T preserves the zero vector: T(0) = 0
- T preserves the negative of a vector: T(-x) = -T(x) for any x
- T preserves linear combinations: T(a x + b y) = a T(x) + b T(y) for any x, y and scalars a, b
- T is determined by its action on a basis: if B = {v_1, v_2, ..., v_n} is a basis for R^n, then T is uniquely defined by T(v_i) for i = 1, 2, ..., n
- T can be represented by a matrix: if A is an m x n matrix, then T(x) = A x is a linear transformation from R^n to R^m
- T has a kernel and a range: the kernel of T is the set of vectors that are mapped to zero by T, and the range of T is the set of vectors that are mapped to some vector by T
- T has a rank and a nullity: the rank of T is the dimension of the range of T, and the nullity of T is the dimension of the kernel of T
- T satisfies the rank-nullity theorem: the rank of T plus the nullity of T equals the dimension of the domain of T