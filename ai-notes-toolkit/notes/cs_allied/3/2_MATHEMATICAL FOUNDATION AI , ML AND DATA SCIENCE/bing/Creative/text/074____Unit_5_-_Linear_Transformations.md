## Unit 5 - Linear Transformations

- A linear transformation (or a linear map) is a function T: R n → R m that satisfies the following properties  :
  - T (x + y) = T (x) + T (y) for any vectors x, y ∈ R n
  - T (a x) = a T (x) for any vector x ∈ R n and any scalar a ∈ R
- A linear transformation can be represented by a matrix A such that T (x) = A x for any vector x ∈ R n
- A linear transformation can be visualized as a mapping that preserves the properties of vector addition and scalar multiplication
- Some examples of linear transformations are:
  - The zero transformation defined by T (x) = 0 for all x ∈ R n
  - The identity transformation defined by T (x) = x for all x ∈ R n
  - The scaling transformation defined by T (x) = k x for some scalar k ∈ R and any vector x ∈ R n
  - The rotation transformation defined by T (x) = R x for some rotation matrix R and any vector x ∈ R n
- Some properties of linear transformations are  :
  - T preserves the zero vector: T (0) = 0
  - T preserves the negative of a vector: T (-x) = -T (x) for any vector x ∈ R n
  - T preserves linear combinations: T (a x + b y) = a T (x) + b T (y) for any vectors x, y ∈ R n and any scalars a, b ∈ R
  - T preserves the dimension of the domain and the range: dim (T (R n)) = dim (R m)
  - T preserves the rank and the nullity of a matrix: rank (T) = rank (A) and nullity (T) = nullity (A) where A is the matrix representation of T
  - T preserves the linear independence and the basis of a vector space: if {v 1, v 2, ..., v k} is a basis for R n, then {T (v 1), T (v 2), ..., T (v k)} is a basis for T (R n)