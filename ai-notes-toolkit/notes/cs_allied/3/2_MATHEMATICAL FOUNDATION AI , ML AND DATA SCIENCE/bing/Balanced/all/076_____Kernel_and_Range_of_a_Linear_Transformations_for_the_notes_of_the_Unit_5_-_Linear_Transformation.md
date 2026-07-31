# Kernel and Range of a Linear Transformation

- A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication.
- The kernel (or null space) of a linear transformation T: V -> W is the set of all vectors u in V such that T(u) = 0 (the zero vector in W).
- The range (or image) of a linear transformation T: V -> W is the set of all vectors w in W that can be written as T(v) for some v in V.
- The kernel and the range of a linear transformation are important because they reveal information about the structure and properties of the transformation, such as whether it is one-to-one, onto, invertible, etc.
- The kernel and the range of a linear transformation are also subspaces of their respective vector spaces, which means they satisfy the following properties:
  - They contain the zero vector.
  - They are closed under vector addition and scalar multiplication.
  - They have a basis and a dimension.
- The dimension of the kernel of a linear transformation is called the nullity, and the dimension of the range is called the rank. There is a formula that relates the nullity, the rank, and the dimension of the domain of a linear transformation, called the rank-nullity theorem:
  - If T: V -> W is a linear transformation, and V is a finite-dimensional vector space, then nullity(T) + rank(T) = dim(V).
- To find the kernel and the range of a linear transformation, one can use the following steps:
  - For the kernel, find the set of all vectors v in V such that T(v) = 0, by solving a system of linear equations or using matrix methods. Then, find a basis and the dimension of this set, which will be the kernel and the nullity of T, respectively.
  - For the range, find the set of all vectors w in W that can be written as T(v) for some v in V, by expressing w as a linear combination of the images of a basis of V under T. Then, find a basis and the dimension of this set, which will be the range and the rank of T, respectively.