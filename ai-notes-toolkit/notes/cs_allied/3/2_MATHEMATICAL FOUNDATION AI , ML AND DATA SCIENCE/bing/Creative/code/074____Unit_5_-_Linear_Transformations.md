## Unit 5 - Linear Transformations

- A linear transformation (or a linear map) is a function `T: R^n -> R^m` that satisfies the following properties  :
  - `T(x + y) = T(x) + T(y)` for any vectors `x, y ∈ R^n`
  - `T(a x) = a T(x)` for any vector `x ∈ R^n` and any scalar `a ∈ R`
- A linear transformation can be represented by a matrix `A` such that `T(x) = A x` for any vector `x ∈ R^n` .
- Some examples of linear transformations are :
  - The zero transformation `T(x) = 0` for all `x`
  - The identity transformation `T(x) = x` for all `x`
  - The scaling transformation `T(x) = k x` for some scalar `k`
  - The rotation transformation `T(x) = R x` for some rotation matrix `R`
  - The projection transformation `T(x) = P x` for some projection matrix `P`
- Some properties of linear transformations are :
  - `T(0) = 0` for the zero vector `0`
  - `T(-x) = -T(x)` for any vector `x`
  - `T(x - y) = T(x) - T(y)` for any vectors `x, y`
  - `T(a x + b y) = a T(x) + b T(y)` for any vectors `x, y` and any scalars `a, b`
  - `T` is one-to-one if and only if `T(x) = 0` implies `x = 0`
  - `T` is onto if and only if for every vector `y ∈ R^m`, there exists a vector `x ∈ R^n` such that `T(x) = y`
  - `T` is invertible if and only if `T` is one-to-one and onto, and there exists a linear transformation `S: R^m -> R^n` such that `S(T(x)) = x` and `T(S(y)) = y` for all `x ∈ R^n` and `y ∈ R^m`