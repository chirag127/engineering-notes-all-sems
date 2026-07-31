### Kernel and Range of a Linear Transformation

- A linear transformation is a function T: V -> W that preserves the operations of vector addition and scalar multiplication, i.e., T(u + v) = T(u) + T(v) and T(cu) = cT(u) for any vectors u, v in V and any scalar c.
- The kernel (or null space) of a linear transformation T: V -> W is the set of all vectors u in V such that T(u) = 0 (the zero vector in W). It is denoted by ker(T) or N(T).
- The range (or image) of a linear transformation T: V -> W is the set of all vectors w in W that can be obtained by applying T to some vector in V. It is denoted by ran(T) or Im(T).
- The kernel and the range of a linear transformation are both subspaces, i.e., they are closed under vector addition and scalar multiplication.
- The kernel and the range of a linear transformation are related to the dimension of the domain and the codomain by the rank-nullity theorem, which states that dim(V) = dim(ker(T)) + dim(ran(T)) for any linear transformation T: V -> W, where dim(V) and dim(W) are the dimensions of V and W, respectively.
- The rank of a linear transformation T: V -> W is the dimension of its range, i.e., rank(T) = dim(ran(T)).
- The nullity of a linear transformation T: V -> W is the dimension of its kernel, i.e., null(T) = dim(ker(T)).
- A linear transformation T: V -> W is one-to-one (or injective) if T(u) = T(v) implies that u = v for any vectors u, v in V. Equivalently, T is one-to-one if ker(T) = {0}, i.e., the kernel contains only the zero vector.
- A linear transformation T: V -> W is onto (or surjective) if ran(T) = W, i.e., every vector in W is in the range of T. Equivalently, T is onto if rank(T) = dim(W).
- A linear transformation T: V -> W is bijective if it is both one-to-one and onto. In this case, T has an inverse function T^-1: W -> V that satisfies T^-1(T(u)) = u for any u in V and T(T^-1(w)) = w for any w in W.
- A matrix transformation is a special type of linear transformation that maps a vector x in R^n to a vector Ax in R^m, where A is an m x n matrix. The kernel and the range of a matrix transformation are the same as the null space and the column space of the matrix A, respectively. The rank and the nullity of a matrix transformation are the same as the rank and the nullity of the matrix A, respectively.