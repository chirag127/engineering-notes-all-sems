### Finding a Basis of a Vector Space

- A basis of a vector space is a set of linearly independent vectors that span the whole space.
- A basis is not unique, but any two bases of the same vector space have the same number of elements, called the dimension of the space.
- To find a basis of a vector space, one can use the following methods:
  - If the vector space is given as the span of a set of vectors, then one can apply the Gaussian elimination algorithm to the matrix formed by the vectors as columns, and select the pivot columns as a basis.
  - If the vector space is given as the null space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and write the general solution of the homogeneous system as a linear combination of free variables, and select the coefficients of the free variables as a basis.
  - If the vector space is given as the column space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and select the pivot columns of the original matrix as a basis.
  - If the vector space is given as the row space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and select the non-zero rows of the reduced matrix as a basis.