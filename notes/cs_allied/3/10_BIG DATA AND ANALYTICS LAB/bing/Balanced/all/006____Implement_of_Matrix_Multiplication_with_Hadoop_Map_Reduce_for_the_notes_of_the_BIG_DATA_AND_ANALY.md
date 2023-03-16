## Implement of Matrix Multiplication with Hadoop Map Reduce

- Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra.
- Hadoop is a framework that allows for distributed processing of large data sets across clusters of computers using simple programming models.
- MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- Matrix multiplication with Hadoop MapReduce involves the following steps:

  - Input: Two matrices A and B of size m x n and n x p respectively, where m, n, and p are positive integers.
  - Output: A matrix C of size m x p, where C[i][j] is the dot product of the i-th row of A and the j-th column of B.
  - Map: The map function takes a pair of matrices A and B as input and emits key-value pairs of the form ((i, j), (M, k, v)), where i and j are the row and column indices of the output matrix C, M is the matrix identifier (A or B), k is the common dimension index, and v is the matrix element value. For example, if A[2][3] = 4 and B[3][5] = 7, the map function will emit ((2, 5), (A, 3, 4)) and ((2, 5), (B, 3, 7)).
  - Reduce: The reduce function takes a key (i, j) and a list of values (M, k, v) as input and computes the dot product of the corresponding row of A and column of B. For each key, the reduce function groups the values by the matrix identifier M and sorts them by the common dimension index k. Then, it multiplies the corresponding values of A and B and sums them up to get the output element C[i][j]. For example, if the reduce function receives ((2, 5), [(A, 1, 2), (A, 2, 3), (A, 3, 4), (B, 1, 5), (B, 2, 6), (B, 3, 7)]), it will compute C[2][5] = (2 * 5) + (3 * 6) + (4 * 7) = 70.
  - Output: The output of the reduce function is a key-value pair of the form ((i, j), C[i][j]), where i and j are the row and column indices of the output matrix C and C[i][j] is the computed element value. The output pairs are written to a file or a database.

- The following pseudocode illustrates the map and reduce functions for matrix multiplication with Hadoop MapReduce:

```
map(key, value):
  // key: dummy value
  // value: a pair of matrices A and B
  A = value[0]
  B = value[1]
  for i = 1 to A.numRows:
    for j = 1 to B.numCols:
      for k = 1 to A.numCols:
        emit((i, j), (A, k, A[i][k]))
        emit((i, j), (B, k, B[k][j]))

reduce(key, values):
  // key: a pair of indices (i, j)
  // values: a list of pairs (M, k, v)
  A_list = []
  B_list = []
  for each (M, k, v) in values:
    if M == A:
      A_list.append((k, v))
    else:
      B_list.append((k, v))
  A_list.sort(by k)
  B_list.sort(by k)
  result = 0
  for i = 1 to A_list.length:
    result = result + (A_list[i][1] * B_list[i][1])
  emit(key, result)
```