# Sparse Matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements.
- Sparse matrices arise in many applications, such as finite element methods, graph theory, network analysis, image processing, etc.
- Storing and manipulating sparse matrices efficiently is important for saving space and time.
- There are different ways of representing sparse matrices, depending on the structure and sparsity pattern of the matrix.
- Some common representations are:

  - **Triplet representation**: This is the simplest way of storing a sparse matrix. It consists of three arrays: one for the row indices, one for the column indices, and one for the non-zero values. The length of each array is equal to the number of non-zero elements in the matrix. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    row = [1, 1, 2, 3]
    col = [0, 1, 2, 1]
    val = [5, 8, 3, 6]
    ```

    The advantage of this representation is that it is easy to construct and manipulate. The disadvantage is that it does not preserve the order or structure of the matrix, and it may have duplicate entries for the same element.

  - **Compressed sparse row (CSR) representation**: This is a more compact way of storing a sparse matrix. It consists of three arrays: one for the non-zero values, one for the column indices, and one for the row pointers. The length of the first two arrays is equal to the number of non-zero elements in the matrix. The length of the third array is equal to the number of rows plus one. The row pointers array stores the index of the first non-zero element in each row, and the last element is the total number of non-zero elements. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    val = [5, 8, 3, 6]
    col = [0, 1, 2, 1]
    row_ptr = [0, 0, 2, 3, 4]
    ```

    The advantage of this representation is that it preserves the row order and structure of the matrix, and it allows for efficient row-wise operations and matrix-vector multiplication. The disadvantage is that it is not easy to insert or delete elements, and it does not support column-wise operations.

  - **Compressed sparse column (CSC) representation**: This is a similar way of storing a sparse matrix as CSR, but with the roles of rows and columns reversed. It consists of three arrays: one for the non-zero values, one for the row indices, and one for the column pointers. The length of the first two arrays is equal to the number of non-zero elements in the matrix. The length of the third array is equal to the number of columns plus one. The column pointers array stores the index of the first non-zero element in each column, and the last element is the total number of non-zero elements. For example, the matrix

    ```
    | 0 0 0 0 |
    | 5 8 0 0 |
    | 0 0 3 0 |
    | 0 6 0 0 |
    ```

    can be stored as:

    ```
    val = [5, 6, 8, 3]
    row = [1, 3, 1, 2]
    col_ptr = [0, 2, 4, 5, 5]
    ```

    The advantage of this representation is that it preserves the column order and structure of the matrix, and it allows for efficient column-wise operations and matrix-vector multiplication. The disadvantage is that it is not easy to insert or delete elements, and it does not support row-wise operations.

  - **Coordinate list (COO) representation**: This is a variation of the triplet representation, where the three arrays are sorted by row and column indices. This makes it easier to convert to CSR or CSC formats, and to perform matrix operations such as addition, subtraction, and multiplication. For example, the matrix

    ```
    | 0 0 0 0

```
