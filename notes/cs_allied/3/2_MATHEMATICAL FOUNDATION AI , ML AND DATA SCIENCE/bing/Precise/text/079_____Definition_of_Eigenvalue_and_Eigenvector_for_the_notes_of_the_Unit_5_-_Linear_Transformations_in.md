### Definition of Eigenvalue and Eigenvector

- In linear algebra, an eigenvector or characteristic vector of a linear transformation is a nonzero vector that changes by a scalar factor when that linear transformation is applied to it.
- The corresponding scalar factor is called an eigenvalue or characteristic value associated with that eigenvector.
- More formally, let `T` be a linear transformation from a vector space `V` over a field `F` into itself and let `v` be a nonzero vector in `V`. Then `v` is an eigenvector of `T` if `T(v)` is a scalar multiple of `v`. This can be written as:

```
T(v) = λv
```

where `λ` is a scalar in the field `F`, known as the eigenvalue or characteristic value associated with the eigenvector `v`.

- If `v` is an eigenvector of the linear transformation `T`, then any nonzero scalar multiple of `v` is also an eigenvector of `T` associated with the same eigenvalue `λ`.
- The set of all eigenvectors of `T` associated with the same eigenvalue `λ`, together with the zero vector, is called the eigenspace of `T` associated with `λ`. The dimension of this eigenspace is called the geometric multiplicity of the eigenvalue `λ`.
- The eigenvalues and eigenvectors of a linear transformation have important geometric interpretations and are widely used in many areas of mathematics and science, including physics, engineering, and computer science.