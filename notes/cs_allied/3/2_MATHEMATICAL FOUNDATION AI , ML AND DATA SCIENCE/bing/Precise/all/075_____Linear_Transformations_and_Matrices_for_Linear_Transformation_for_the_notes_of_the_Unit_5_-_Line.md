# Unit 5 - Linear Transformations

### Linear Transformations

A linear transformation is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication. In other words, if `T` is a linear transformation, then for any vectors `u` and `v`, and any scalar `c`, the following properties hold:

1. `T(u + v) = T(u) + T(v)`
2. `T(cu) = cT(u)`

Linear transformations can be represented by matrices. If `T` is a linear transformation from an `n`-dimensional vector space to an `m`-dimensional vector space, then there exists an `m x n` matrix `A` such that `T(u) = Au` for all vectors `u` in the domain of `T`.

### Matrices for Linear Transformation

A matrix can be used to represent a linear transformation. Given a linear transformation `T` from an `n`-dimensional vector space to an `m`-dimensional vector space, we can find a matrix `A` such that `T(u) = Au` for all vectors `u` in the domain of `T`.

To find the matrix `A`, we can use the standard basis vectors of the domain. Let `e1, e2, ..., en` be the standard basis vectors of the `n`-dimensional vector space. Then, the columns of the matrix `A` are given by `T(e1), T(e2), ..., T(en)`.

In other words, the `i`-th column of the matrix `A` is the image of the `i`-th standard basis vector under the linear transformation `T`.

Once we have found the matrix `A`, we can use it to find the image of any vector `u` under the linear transformation `T` by computing the matrix-vector product `Au`. This allows us to represent the linear transformation `T` using a matrix, and to compute the image of any vector under `T` using matrix multiplication.