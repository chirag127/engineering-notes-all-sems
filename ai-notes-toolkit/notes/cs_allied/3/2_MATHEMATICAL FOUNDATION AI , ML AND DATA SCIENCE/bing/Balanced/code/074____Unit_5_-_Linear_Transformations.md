## Unit 5 - Linear Transformations

A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication. In other words, a linear transformation is a function `T: V -> W` such that for any vectors `u` and `v` in `V` and any scalar `c`, we have:

- `T(u + v) = T(u) + T(v)`
- `T(cu) = cT(u)`

Some examples of linear transformations are:

- Scaling: multiplying each coordinate of a vector by a constant factor.
- Rotation: rotating a vector by a fixed angle around the origin.
- Projection: projecting a vector onto a subspace.
- Reflection: reflecting a vector across a line or a plane.

Some properties of linear transformations are:

- The zero vector is always mapped to the zero vector: `T(0) = 0`.
- The identity transformation maps every vector to itself: `T(v) = v` for all `v`.
- The composition of two linear transformations is also a linear transformation: `T(S(v)) = (T o S)(v)` for all `v`.
- The inverse of a linear transformation, if it exists, is also a linear transformation: `T(T^(-1)(v)) = T^(-1)(T(v)) = v` for all `v`.

To represent a linear transformation, we can use a matrix. A matrix is a rectangular array of numbers arranged in rows and columns. Each entry of a matrix is called an element. A matrix can be denoted by its size, such as `m x n`, where `m` is the number of rows and `n` is the number of columns, or by its elements, such as `[a_ij]`, where `a_ij` is the element in the `i`-th row and `j`-th column.

A matrix can act on a vector by multiplying them, which is equivalent to applying a linear transformation. The matrix-vector multiplication is defined as follows: if `A` is an `m x n` matrix and `x` is an `n x 1` vector, then the product `Ax` is an `m x 1` vector whose `i`-th element is the dot product of the `i`-th row of `A` and `x`:

`Ax = [a_11 a_12 ... a_1n] [x_1] = [a_11 x_1 + a_12 x_2 + ... + a_1n x_n]`
     `[a_21 a_22 ... a_2n] [x_2]   [a_21 x_1 + a_22 x_2 + ... + a_2n x_n]`
     `[...  ...  ... ... ] [... ]   [...  ...  ... ... ]`
     `[a_m1 a_m2 ... a_mn] [x_n]   [a_m1 x_1 + a_m2 x_2 + ... + a_mn x_n]`

The matrix-vector multiplication is also linear, meaning that for any matrices `A` and `B` and any vectors `u`, `v` and `w`, and any scalar `c`, we have:

- `A(u + v) = Au + Av`
- `A(cu) = cAu`
- `(A + B)u = Au + Bu`
- `A(Bu) = (AB)u`

The matrix that represents a linear transformation `T: V -> W` depends on the choice of bases for `V` and `W`. A basis for a vector space is a set of linearly independent vectors that span the space. A vector can be written as a linear combination of the basis vectors, and the coefficients of the linear combination are called the coordinates of the vector with respect to the basis. The coordinates of a vector form a vector themselves, called the coordinate vector.

If `B = {v_1, v_2, ..., v_n}` is a basis for `V` and `C = {w_1, w_2, ..., w_m}` is a basis for `W`, then the matrix that represents `T` with respect to `B` and `C` is denoted by `[T]_B^C` and has the following form:

`[T]_B^C = [T(v_1)]_C [T(v_2)]_C ... [T(v_n)]_C`
          `| ...   |   | ...   |     | ...   |`
          `| ...   |   |