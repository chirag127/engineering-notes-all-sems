```markdown
## Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

### Arrays
- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- An array can be of one dimension (1-D), two dimensions (2-D), three dimensions (3-D) or more (n-D).
- The size of an array is fixed and must be declared before using it.
- The elements of an array are numbered from 0 to n-1, where n is the number of elements in the array.
- To access an element of an array, we use the array name followed by the index of the element in square brackets. For example, A[3] refers to the fourth element of the array A.

### Representation of Arrays
- There are two ways to represent an array in memory: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. The elements of each row are stored in consecutive memory locations. For example, a 2-D array A[3][4] is stored as follows in row major order:

| A[0][0] | A[0][1] | A[0][2] | A[0][3] |
| A[1][0] | A[1][1] | A[1][2] | A[1][3] |
| A[2][0] | A[2][1] | A[2][2] | A[2][3] |

- In column major order, the elements of an array are stored column by column, starting from the first column. The elements of each column are stored in consecutive memory locations. For example, a 2-D array A[3][4] is stored as follows in column major order:

| A[0][0] | A[1][0] | A[2][0] |
| A[0][1] | A[1][1] | A[2][1] |
| A[0][2] | A[1][2] | A[2][2] |
| A[0][3] | A[1][3] | A[2][3] |

### Derivation of Index Formulae
- To calculate the address of an element of an array, we need to know the base address of the array, the size of each element, and the index of the element.
- The base address of an array is the address of the first element of the array. For example, if A[0][0] is stored at location 1000, then the base address of A is 1000.
- The size of each element of an array depends on the data type of the array. For example, if the array is of type int, then each element occupies 4 bytes of memory.
- The index of an element of an array is the position of the element in the array, starting from 0. For example, A[2][3] has the index (2,3) in a 2-D array.
- The formula to calculate the address of an element of a 1-D array A[i] in row major order is:

  - Address of A[i] = Base address of A + (i * size of each element)

- The formula to calculate the address of an element of a 2-D array A[i][j] in row major order is:

  - Address of A[i][j] = Base address of A + ((i * number of columns) + j) * size of each element

- The formula to calculate the address of an element of a 3-D array A[i][j][k] in row major order is:

  - Address of A[i][j][k] = Base address of A + (((i * number of rows) + j) * number of columns + k) * size of each element

- The formula to calculate the address of an element of an n-D array A[i1][i2]...[in] in row major order is:

  - Address of A[i1][i2]...[in]