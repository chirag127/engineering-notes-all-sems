# Sparse Matrices and their representations

- A sparse matrix is a matrix in which most of the elements are zero.
- A sparse matrix can be represented in different ways to save space and time, such as:
  - Triplet representation : A two-dimensional array with three rows, where each column stores the row index, column index and value of a non-zero element.
  - Linked representation: A linked list of nodes, where each node stores the row index, column index, value and pointer to the next node of a non-zero element.
  - Compressed sparse row (CSR) representation: Three one-dimensional arrays, where one array stores the non-zero values, one array stores the column indices of the non-zero values, and one array stores the cumulative number of non-zero values in each row.
  - Compressed sparse column (CSC) representation: Similar to CSR, but with column indices and values interchanged.
- Operations on sparse matrices, such as addition, multiplication and transpose, can be performed using the sparse representations, with different algorithms and complexities.