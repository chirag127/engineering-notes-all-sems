### Elementary transformations for the notes of the Unit 1 - Matrices in the subject of ENGINEERING MATHEMATICS-I

- Elementary transformations are operations done on the rows and columns of matrices to change their shape so that the computations become easier  .
- Elementary transformations are also used to discover the inverse of a matrix, the determinants of a matrix, and to solve a system of linear equations.
- There are three types of elementary transformations for matrices :
  - Row transformations: These are operations performed on the rows of a matrix, such as swapping two rows, multiplying a row by a nonzero scalar, or adding a multiple of one row to another row.
  - Column transformations: These are operations performed on the columns of a matrix, such as swapping two columns, multiplying a column by a nonzero scalar, or adding a multiple of one column to another column.
  - Row-column transformations: These are operations performed on both the rows and columns of a matrix, such as transposing the matrix, or multiplying the matrix by a diagonal matrix on the left or right.
- Elementary matrices are square matrices that can be obtained by applying one elementary transformation to the identity matrix .
- Elementary matrices have the following properties :
  - They are invertible, and their inverse is also an elementary matrix of the same type.
  - They generate the general linear group of all invertible matrices of a given size.
  - They can be used to perform elementary transformations on any matrix by multiplying them on the left or right. For example, if E is an elementary matrix and A is any matrix, then EA is the result of applying the same row transformation that E does to the identity matrix to A, and AE is the result of applying the same column transformation that E does to the identity matrix to A.
- Here are some examples of elementary matrices and their corresponding elementary transformations :
  - The matrix E = [[0, 1], [1, 0]] is obtained by swapping the first and second rows of the identity matrix I = [[1, 0], [0, 1]]. Therefore, E is an elementary matrix of row transformation type, and its inverse is E^-1 = E. Multiplying E on the left or right of any matrix A will swap the first and second rows or columns of A, respectively.
  - The matrix E = [[2, 0], [0, 1]] is obtained by multiplying the first row of the identity matrix I by 2. Therefore, E is an elementary matrix of row transformation type, and its inverse is E^-1 = [[1/2, 0], [0, 1]]. Multiplying E on the left or right of any matrix A will multiply the first row or column of A by 2, respectively.
  - The matrix E = [[1, 0], [3, 1]] is obtained by adding 3 times the first row of the identity matrix I to the second row. Therefore, E is an elementary matrix of row transformation type, and its inverse is E^-1 = [[1, 0], [-3, 1]]. Multiplying E on the left or right of any matrix A will add 3 times the first row or column of A to the second row or column of A, respectively.
  - The matrix E = [[1, 0], [0, 0]] is obtained by multiplying the second row of the identity matrix I by 0. Therefore, E is not an elementary matrix, because it is not invertible. Multiplying E on the left or right of any matrix A will make the second row or column of A zero, respectively.