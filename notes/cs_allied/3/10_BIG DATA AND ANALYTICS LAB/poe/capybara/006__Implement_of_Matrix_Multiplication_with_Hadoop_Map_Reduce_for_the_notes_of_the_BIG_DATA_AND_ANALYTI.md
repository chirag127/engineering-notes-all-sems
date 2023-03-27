## Implement of Matrix Multiplication with Hadoop Map Reduce

In the field of Big Data and Analytics, matrix multiplication is a fundamental operation that is used in various applications such as machine learning, data mining, and image processing. With the increase in the size of the matrices, the traditional methods of matrix multiplication become inefficient and take a lot of time. Therefore, it is essential to adopt a distributed computing approach to perform matrix multiplication on large-scale data.

Hadoop Map Reduce is a framework designed to process large datasets in parallel across a cluster of computers. It provides a distributed computing environment that can perform matrix multiplication using Map Reduce jobs. Here are the steps to implement matrix multiplication with Hadoop Map Reduce:

1. **Data Preparation:** The first step is to prepare the input data in the form of two matrices. Each matrix is divided into blocks of a specific size, and each block is assigned to a separate mapper. The data is then distributed across the cluster of computers.

2. **Mapper Function:** The mapper function takes two blocks of matrices as input and multiplies them to produce a partial result. The output of the mapper function is a key-value pair, where the key is the index of the resulting block, and the value is the partial result.

3. **Shuffle and Sort:** The shuffle and sort phase is responsible for grouping the intermediate results based on their keys. All the partial results with the same key are sent to the same reducer.

4. **Reducer Function:** The reducer function takes the partial results with the same key and combines them to produce the final result. The output of the reducer function is a key-value pair, where the key is the index of the final resulting block, and the value is the final result.

5. **Output Generation:** The final step is to generate the output in the form of two matrices. Each matrix is constructed by combining the resulting blocks.

In conclusion, Hadoop Map Reduce provides an efficient and scalable approach to perform matrix multiplication on large-scale data. By dividing the matrices into blocks and processing them in parallel, it reduces the computation time and improves the performance. It is essential to understand the steps involved in implementing matrix multiplication with Hadoop Map Reduce for the BIG DATA AND ANALYTICS LAB subject.