# Kernel and Range of a Linear Transformation

In the study of linear transformations, two important concepts are the kernel and the range of a transformation. These concepts are used to understand the behavior of a linear transformation and its properties.

## Kernel of a Linear Transformation

The kernel of a linear transformation is the set of all vectors in the domain of the transformation that are mapped to the zero vector in the codomain. In other words, the kernel is the set of all vectors `v` such that `T(v) = 0`, where `T` is the linear transformation.

The kernel of a linear transformation is a subspace of the domain. This means that it is closed under addition and scalar multiplication. If `v` and `w` are in the kernel of `T`, then `T(v + w) = T(v) + T(w) = 0 + 0 = 0`, so `v + w` is also in the kernel. Similarly, if `v` is in the kernel and `c` is a scalar, then `T(cv) = cT(v) = c0 = 0`, so `cv` is also in the kernel.

## Range of a Linear Transformation

The range of a linear transformation is the set of all vectors in the codomain that are the image of at least one vector in the domain. In other words, the range is the set of all vectors `w` such that there exists a vector `v` in the domain with `T(v) = w`.

The range of a linear transformation is also a subspace of the codomain. This means that it is closed under addition and scalar multiplication. If `w` and `z` are in the range of `T`, then there exist vectors `v` and `u` in the domain such that `T(v) = w` and `T(u) = z`. Then, `T(v + u) = T(v) + T(u) = w + z`, so `w + z` is also in the range. Similarly, if `w` is in the range and `c` is a scalar, then there exists a vector `v` in the domain such that `T(v) = w`. Then, `T(cv) = cT(v) = cw`, so `cw` is also in the range.

These concepts are important in the study of linear transformations and can provide insight into the behavior and properties of a transformation. They are often used in the analysis of systems of linear equations and in the study of vector spaces and their subspaces.