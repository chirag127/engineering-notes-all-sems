### Sparse Matrices and their representations

- A sparse matrix is a matrix in which most of the elements are zero. This is in contrast to a dense matrix, where most of the elements are non-zero.
- Sparse matrices arise in many applications, such as graph theory, network analysis, finite element methods, etc. where the data is sparse or has a lot of empty spaces.
- Storing and manipulating sparse matrices in their original form can be inefficient and wasteful of space and time. Therefore, various representations and operations have been developed to handle sparse matrices more efficiently.
- Sparse matrix representations store only the non-zero elements of the matrix, along with their row and column indices. This avoids the wastage of space in storing the zero elements, and also saves time in finding the non-zero elements in a large matrix.
- There are different ways of representing sparse matrices, such as:

  - **Triplet representation**: In this representation, a sparse matrix is stored as a list of triplets, where each triplet consists of the row index, column index, and value of a non-zero element. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    | row | col | val |
    | --- | --- | --- |
    | 0   | 2   | 3   |
    | 1   | 0   | 2   |
    | 3   | 1   | 4   |

    The advantage of this representation is that it is simple and easy to implement. The disadvantage is that it does not preserve the order of the elements, and it may contain duplicate entries for the same element.

  - **Linked list representation**: In this representation, a sparse matrix is stored as a linked list of nodes, where each node contains the row index, column index, value, and pointers to the next node in the same row and the same column. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    ![linked list representation](https://media.geeksforgeeks.org/wp-content/uploads/20190902115231/Sparse-Matrix-Linked-List-Representation.png)

    The advantage of this representation is that it preserves the order of the elements, and it allows easy traversal of the matrix by row or by column. The disadvantage is that it requires extra space for the pointers, and it is more complex to implement.

  - **Compressed sparse row (CSR) representation**: In this representation, a sparse matrix is stored as three arrays: one for the non-zero values, one for the column indices of the non-zero values, and one for the row pointers that indicate the start of each row in the value and column index arrays. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |
    | 2 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 |
    | 0 | 4 | 0 | 0 |

    can be represented as

    | val | 3 | 2 | 4 |
    | --- | - | - | - |
    | col | 2 | 0 | 1 |
    | row | 0 | 1 | 2 | 3 |

    The advantage of this representation is that it is compact and efficient for matrix-vector multiplication and other operations. The disadvantage is that it is not easy to insert or delete elements, and it does not allow random access to the elements.

  - **Compressed sparse column (CSC) representation**: In this representation, a sparse matrix is stored as three arrays: one for the non-zero values, one for the row indices of the non-zero values, and one for the column pointers that indicate the start of each column in the value and row index arrays. For example, the matrix

    | 0 | 0 | 3 | 0 |
    | - | - | - | - |