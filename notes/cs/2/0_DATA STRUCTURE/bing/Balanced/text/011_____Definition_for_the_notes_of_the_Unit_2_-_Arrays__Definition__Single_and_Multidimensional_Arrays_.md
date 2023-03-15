### Definition for the notes of the Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial. in the subject of DATA STRUCTURE

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- A single-dimensional array is an array with one dimension, or one row of elements. For example, int A[10] is a single-dimensional array of 10 integers.
- A multidimensional array is an array with more than one dimension, or more than one row and column of elements. For example, int B[3][4] is a two-dimensional array of 3 rows and 4 columns of integers.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common orders: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of B[3][4] are stored as B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3].
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of B[3][4] are stored as B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3].
- The index formulae for an array are used to calculate the address of an element in memory, given its index and the base address of the array. The formulae depend on the order, the number of dimensions, and the size of each dimension of the array.
- For a single-dimensional array A[n] stored in row major order, the address of A[i] is given by:

  - Address of A[i] = Base address of A + i * size of each element

- For a two-dimensional array B[m][n] stored in row major order, the address of B[i][j] is given by:

  - Address of B[i][j] = Base address of B + (i * n + j) * size of each element

- For a three-dimensional array C[p][q][r] stored in row major order, the address of C[i][j][k] is given by:

  - Address of C[i][j][k] = Base address of C + (i * q * r + j * r + k) * size of each element

- For an n-dimensional array D[d1][d2]...[dn] stored in row major order, the address of D[i1][i2]...[in] is given by:

  - Address of D[i1][i2]...[in] = Base address of D + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of each element

- The index formulae for arrays stored in column major order can be derived by reversing the order of the indices and dimensions in the formulae for row major order.
- Arrays can be used to store and manipulate various types of data, such as matrices, vectors, strings, tables, etc.
- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements. Storing a sparse matrix as a regular array would waste a lot of memory space. Therefore, there are different ways of representing a sparse matrix, such as:

  - Triplet representation: A sparse matrix is stored as a list of triplets, where each triplet consists of the row index, the column index, and the value of a non-zero element. For example, the