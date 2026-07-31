## Implement of Matrix Multiplication with Hadoop Map Reduce

Matrix multiplication is a common operation in many data analysis tasks. Hadoop MapReduce can be used to implement matrix multiplication in a distributed and scalable manner. Here are the steps to implement matrix multiplication with Hadoop MapReduce:

1. Prepare the input matrices and store them in HDFS (Hadoop Distributed File System).
2. Write a MapReduce program to perform the matrix multiplication. The program can be written in languages such as Java or Python.
3. The Map function takes a row of the first matrix and a column of the second matrix as input and outputs the product of the corresponding elements as the intermediate key-value pairs.
4. The Reduce function takes the intermediate key-value pairs, groups them by key, and sums the values to produce the final result.
5. Run the MapReduce program on the Hadoop cluster to perform the matrix multiplication.

There are several examples of matrix multiplication implementations using Hadoop MapReduce available online, such as on GitHub  . It is important to note that the implementation may not work properly if there are 0's in the input matrices.