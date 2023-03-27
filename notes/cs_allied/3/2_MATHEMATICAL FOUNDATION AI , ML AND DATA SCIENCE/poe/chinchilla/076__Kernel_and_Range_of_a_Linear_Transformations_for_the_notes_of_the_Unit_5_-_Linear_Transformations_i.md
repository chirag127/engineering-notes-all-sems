### Kernel and Range of a Linear Transformation

In linear algebra, a linear transformation is a function that maps one vector space into another vector space, preserving the linear structure of the space. The kernel and range of a linear transformation are fundamental concepts that help us understand the behavior of linear transformations.

#### Kernel

The kernel of a linear transformation T, denoted by ker(T), is the set of all vectors in the domain of T that are mapped to the zero vector in the range of T. In other words, the kernel of T is the set of all solutions to the equation T(x) = 0.

Properties of kernels:
- The kernel of a linear transformation is always a subspace of the domain vector space.
- The kernel of an injective (one-to-one) linear transformation is the zero vector space.
- The kernel of a surjective (onto) linear transformation may contain more than just the zero vector.

#### Range

The range of a linear transformation T, denoted by range(T), is the set of all vectors in the range of T that are the image of some vector in the domain of T. In other words, the range of T is the set of all vectors T(x) for some x in the domain of T.

Properties of ranges:
- The range of a linear transformation is always a subspace of the range vector space.
- The range of an injective (one-to-one) linear transformation is the entire range vector space.
- The range of a surjective (onto) linear transformation may not span the entire range vector space.

#### Relationship between Kernel and Range

The kernel and range of a linear transformation are related by the rank-nullity theorem, which states that the dimension of the kernel plus the dimension of the range equals the dimension of the domain vector space.

Properties of the relationship:
- If the dimension of the kernel is zero, then the linear transformation is injective (one-to-one).
- If the dimension of the range is equal to the dimension of the range vector space, then the linear transformation is surjective (onto).
- If the dimension of the kernel is greater than zero and the dimension of the range is less than the dimension of the range vector space, then the linear transformation is neither injective nor surjective.

In summary, the kernel and range of a linear transformation are important concepts in linear algebra that help us understand the behavior of linear transformations. The properties of kernels and ranges are useful for determining the injectivity and surjectivity of linear transformations, and the relationship between kernel and range is governed by the rank-nullity theorem.