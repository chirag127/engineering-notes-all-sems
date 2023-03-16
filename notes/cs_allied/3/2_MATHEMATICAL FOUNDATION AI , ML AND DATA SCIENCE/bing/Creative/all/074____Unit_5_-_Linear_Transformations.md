## Unit 5 - Linear Transformations

- A linear transformation (or a linear map) is a function T: R n → R m that satisfies the following properties  :
  - T (x + y) = T (x) + T (y) for any vectors x, y ∈ R n
  - T (a x) = a T (x) for any vector x ∈ R n and any scalar a ∈ R
- These properties imply that T preserves the zero vector, the negative of a vector, and linear combinations of vectors .
- A linear transformation can be represented by a matrix, which encodes the effect of T on a standard basis of R n .
- The matrix representation of a linear transformation depends on the choice of basis, and different bases may lead to different matrices for the same transformation .
- The rank of a linear transformation is the dimension of its image (or range), and the nullity of a linear transformation is the dimension of its kernel (or null space) .
- The rank-nullity theorem states that for any linear transformation T: R n → R m, rank(T) + nullity(T) = n .
- A linear transformation is one-to-one (or injective) if and only if its kernel is trivial (i.e., contains only the zero vector) .
- A linear transformation is onto (or surjective) if and only if its image is equal to its codomain .
- A linear transformation is bijective (or invertible) if and only if it is both one-to-one and onto .
- If a linear transformation is invertible, then its inverse is also a linear transformation, and the matrix representation of the inverse is the inverse of the matrix representation of the original transformation .
- A linear transformation is called an isomorphism if it is invertible and preserves the vector space structure of its domain and codomain .
- Two vector spaces are called isomorphic if there exists an isomorphism between them .
- A linear transformation is called an endomorphism if its domain and codomain are the same vector space .
- A linear transformation is called an automorphism if it is an endomorphism and an isomorphism .
- Examples of linear transformations include the zero transformation, the identity transformation, scaling, rotation, reflection, projection, and shear  .