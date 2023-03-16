## Implement of Matrix Multiplication with Hadoop Map Reduce

Matrix multiplication can be performed using Hadoop MapReduce. This involves writing a program to multiply two matrices using the MapReduce framework. The program can be executed on a Hadoop cluster, such as the SDSC Comet Cluster, using an XSEDE login.

The implementation of matrix multiplication using Hadoop MapReduce can be written in various programming languages, including Python. The code for the matrix multiplication can be divided into two parts: the mapper and the reducer. The mapper takes the input matrices and generates key-value pairs, while the reducer takes the key-value pairs and performs the multiplication to generate the final result.

Before writing the code, the matrices must be prepared and put into the Hadoop Distributed File System (HDFS). Once the matrices are in HDFS, the MapReduce program can be run to perform the multiplication.

There are various resources available online, including code examples on GitHub  , that can provide guidance on how to implement matrix multiplication using Hadoop MapReduce. It is important to note that the implementation may not work properly if there are 0's in the input matrices.