# Implement of Matrix Multiplication with Hadoop Map Reduce

Matrix multiplication is a common operation in many data analysis tasks. Hadoop MapReduce is a powerful tool for processing large datasets in a distributed environment. It is possible to implement matrix multiplication using Hadoop MapReduce.

MapReduce is a technique in which a huge program is subdivided into small tasks and run parallelly to make computation faster, save time, and mostly used in distributed systems. It has 2 important parts: 
1. Mapper: It takes raw data input and organizes it into key-value pairs.
2. Reducer: It takes the output from the mapper and combines the values with the same key to produce the final result.

There are several implementations of matrix multiplication using Hadoop MapReduce available online, including implementations in Python and Java. These implementations typically involve two steps: 
1. In the first step, the mapper reads the input matrices and generates key-value pairs where the key is the position of the element in the result matrix and the value is the product of the corresponding elements in the input matrices.
2. In the second step, the reducer sums the values with the same key to produce the final result.

It is important to note that the implementation of matrix multiplication using Hadoop MapReduce may not work properly when there are 0's in the input matrices. It is also important to carefully design the key-value pairs to ensure that the computation is distributed evenly across the cluster.