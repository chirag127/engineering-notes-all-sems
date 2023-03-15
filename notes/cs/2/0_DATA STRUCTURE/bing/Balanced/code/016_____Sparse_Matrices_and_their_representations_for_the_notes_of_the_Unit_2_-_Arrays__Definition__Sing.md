### Sparse Matrices and their representations

- A sparse matrix is a matrix in which most of the elements are zero.
- A sparse matrix can be represented in different ways to save space and time, such as:
  - Array representation: A two-dimensional array of size M x 3, where M is the number of non-zero elements in the matrix, and each row contains the row index, column index and value of a non-zero element.
  - Linked list representation: A linked list of nodes, where each node contains the row index, column index, value and pointer to the next node of a non-zero element.
  - Other representations, such as compressed sparse row (CSR), compressed sparse column (CSC), coordinate list (COO), etc.
- Operations on sparse matrices, such as addition, multiplication and transpose, can be performed on their representations without converting them to dense matrices.
- Sparse matrices are useful for applications that involve large matrices with few non-zero elements, such as graph theory, linear algebra, numerical analysis, etc.