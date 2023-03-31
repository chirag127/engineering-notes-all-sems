
## Implement of Matrix Multiplication with Hadoop Map Reduce for the notes of the BIG DATA AND ANALYTICS LAB

1. Hadoop MapReduce is an open-source framework for distributed computing that can be used to process large amounts of data in a distributed manner.
2. It is designed to scale up from single servers to thousands of machines, each providing local computation and storage.
3. The MapReduce framework is designed to process large amounts of data in a distributed manner.
4. The MapReduce framework consists of two phases: Map and Reduce.
5. In the Map phase, each input file is read and split into multiple key-value pairs.
6. The Reducer phase aggregates the values associated with the same key.
7. Matrix multiplication is a fundamental operation in linear algebra.
8. The Hadoop MapReduce framework can be used to implement matrix multiplication in a distributed manner.
9. The input matrices are read from HDFS and the output is written to HDFS.
10. The Map phase reads the input matrices and emits key-value pairs for each element in the matrices.
11. The Reduce phase aggregates the values associated with the same key and performs the multiplication.
12. The result is written to HDFS as the output matrix.