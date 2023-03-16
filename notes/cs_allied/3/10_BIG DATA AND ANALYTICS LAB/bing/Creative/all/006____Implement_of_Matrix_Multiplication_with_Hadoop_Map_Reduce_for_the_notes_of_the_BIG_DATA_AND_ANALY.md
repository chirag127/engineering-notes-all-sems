# Implement of Matrix Multiplication with Hadoop Map Reduce

- Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra.
- Hadoop Map Reduce is a framework for distributed parallel processing of large-scale data sets using a simple programming model based on key-value pairs.
- To implement matrix multiplication with Hadoop Map Reduce, we need to design a mapper function and a reducer function that can perform the computation in a distributed and scalable way.
- The mapper function takes an input key-value pair, where the key is the name of the matrix (A or B) and the value is a row or a column of the matrix, and emits intermediate key-value pairs, where the key is a pair of indices (i, k) and the value is a pair of matrix name and element value (A, a_ij) or (B, b_jk).
- The intermediate key-value pairs are grouped by the same key (i, k) and sent to the reducer function, which performs the dot product of the corresponding rows and columns of the matrices A and B, and emits the final key-value pair, where the key is the pair of indices (i, k) and the value is the product c_ik.
- The pseudocode for the mapper function and the reducer function are given below:

```
Mapper function:
  Input: key = matrix name, value = row or column of the matrix
  Output: intermediate key-value pairs
  For each element in the value:
    If the matrix name is A:
      Emit (i, k), (A, a_ij) for all k
    If the matrix name is B:
      Emit (i, k), (B, b_jk) for all i
```

```
Reducer function:
  Input: key = pair of indices (i, k), value = list of pairs of matrix name and element value
  Output: final key-value pair
  Initialize sum to 0
  For each pair in the value:
    If the matrix name is A:
      Store a_ij in a variable
    If the matrix name is B:
      Store b_jk in a variable
    Multiply a_ij and b_jk and add to sum
  Emit (i, k), sum
```

- The following diagram illustrates the matrix multiplication with Hadoop Map Reduce for two 2x2 matrices A and B:

![Matrix multiplication with Hadoop Map Reduce](https://miro.medium.com/max/1400/1*Q1y9tQsQ4Z4fQ2Q0w4w4jw.png)

- The mapper function emits four intermediate key-value pairs for each row or column of the matrices A and B, and the reducer function computes the dot product for each pair of indices (i, k) and emits the final key-value pair for the product matrix C.