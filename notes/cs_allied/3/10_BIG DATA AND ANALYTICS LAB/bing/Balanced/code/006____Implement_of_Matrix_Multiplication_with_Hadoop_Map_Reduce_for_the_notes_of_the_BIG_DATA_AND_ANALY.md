## Implement of Matrix Multiplication with Hadoop Map Reduce

- Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra.
- Hadoop Map Reduce is a framework for distributed parallel processing of large-scale data sets using a master-slave architecture.
- The basic idea of matrix multiplication with Hadoop Map Reduce is to divide the input matrices into smaller sub-matrices, and assign each sub-matrix to a mapper or a reducer task.
- The mapper task reads the sub-matrix from the input file, and emits key-value pairs of the form `(i, k, A[i][j])` for matrix A, and `(j, k, B[j][k])` for matrix B, where `i`, `j`, and `k` are the row, column, and intermediate indices, respectively.
- The reducer task receives the key-value pairs from the mapper tasks, and groups them by the key `(i, k)`. For each key, the reducer task performs the dot product of the corresponding sub-matrices, and emits the result as `(i, k, C[i][k])`, where `C[i][k]` is the element of the output matrix C at row `i` and column `k`.
- The output file contains the key-value pairs of the form `(i, k, C[i][k])`, which can be converted to the matrix format by sorting them by the key `(i, k)`.
- The following pseudocode illustrates the mapper and reducer functions for matrix multiplication with Hadoop Map Reduce:

```
Mapper function:
  Input: a sub-matrix of A or B
  Output: key-value pairs of the form (i, k, A[i][j]) or (j, k, B[j][k])
  For each element in the sub-matrix:
    If the sub-matrix belongs to A:
      Emit (i, k, A[i][j]) for all k from 1 to n
    Else if the sub-matrix belongs to B:
      Emit (j, k, B[j][k]) for all k from 1 to n

Reducer function:
  Input: key-value pairs of the form (i, k, A[i][j]) or (j, k, B[j][k])
  Output: key-value pairs of the form (i, k, C[i][k])
  For each key (i, k):
    Initialize C[i][k] to 0
    For each value v in the list of values for the key (i, k):
      If v belongs to A:
        Store v as A[i][j]
      Else if v belongs to B:
        Store v as B[j][k]
    Compute C[i][k] as the dot product of A[i] and B[k]
    Emit (i, k, C[i][k])
```