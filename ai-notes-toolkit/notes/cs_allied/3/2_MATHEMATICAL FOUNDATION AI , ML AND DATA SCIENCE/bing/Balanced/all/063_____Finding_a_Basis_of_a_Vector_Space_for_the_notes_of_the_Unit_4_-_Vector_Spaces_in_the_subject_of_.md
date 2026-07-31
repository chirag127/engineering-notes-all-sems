# Finding a Basis of a Vector Space

- A basis of a vector space is a set of linearly independent vectors that span the whole space.
- A basis has two important properties:
  - Any vector in the space can be written as a unique linear combination of the basis vectors.
  - The number of basis vectors is equal to the dimension of the space, which is the minimum number of vectors needed to span the space.
- To find a basis of a vector space, we can use the following steps:
  - If the space is given by a set of vectors, we can check if they are linearly independent and span the space. If yes, then they form a basis. If not, we can use the row reduction method to eliminate the linearly dependent vectors and obtain a basis.
  - If the space is given by a set of equations, we can write them in matrix form and use the row reduction method to find the reduced row echelon form of the matrix. The pivot columns of the matrix correspond to the basis vectors of the space.
  - If the space is given by a subspace of another space, we can find a basis of the larger space and then check which basis vectors belong to the subspace. Alternatively, we can find a basis of the orthogonal complement of the subspace and then use the Gram-Schmidt process to obtain a basis of the subspace.