### Unit 5 - Linear Transformations

#### Linear Transformations

A linear transformation is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication. In other words, if `T` is a linear transformation, then for any vectors `u` and `v`, and any scalar `c`, the following properties hold:

1. `T(u + v) = T(u) + T(v)`
2. `T(cu) = cT(u)`

#### Matrices for Linear Transformation

A matrix can represent a linear transformation. Given a linear transformation `T` from an `n`-dimensional vector space to an `m`-dimensional vector space, there exists an `m x n` matrix `A` such that for any vector `x` in the domain of `T`, `T(x) = Ax`. The columns of the matrix `A` are the images of the standard basis vectors under the transformation `T`.

In other words, if `e1, e2, ..., en` are the standard basis vectors for the domain of `T`, then the `i`-th column of `A` is `T(ei)`. The matrix `A` is called the matrix representation of the linear transformation `T`.