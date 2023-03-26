 Here is the formal notes in Markdown format on the topic "Implement of Matrix Multiplication with Hadoop Map Reduce for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB":

## Implement of Matrix Multiplication with Hadoop Map Reduce

1. Introduction
- Matrix multiplication is an important operation in linear algebra with applications in various domains like machine learning, scientific computing, etc.
- In this experiment, we will implement matrix multiplication using Hadoop MapReduce.

2. Problem Statement
- Given two input matrices A and B of size NxN, calculate the product matrix C = A x B.

3. Algorithm
- The algorithm follows the standard matrix multiplication algorithm.
- In the Map phase, each mapper will multiply a block of A matrix with each block of B matrix and emit the partial results.
- In the Reduce phase, the partial results will be accumulated to get the final output.

4. Map Phase
- The input matrices A and B are split into multiple blocks.
- Each mapper gets one block of A and one block of B.
- The mapper multiplies the two blocks and emits the partial output.

5. Reduce Phase
- The partial results from the mappers are accumulated in the reducers to get the final output matrix C.
- The size of the reducers will be same as the size of the output matrix C.

6. Results
- The output matrix C is calculated which is the product of input matrices A and B.
- The time taken will increase linearly with the increase in the size of the input matrices.

7. Conclusion
- We implemented matrix multiplication using Hadoop MapReduce.
- The algorithm follows the standard matrix multiplication approach by splitting the input into blocks and multiplying and accumulating in MapReduce phases.