## Implement of Matrix Multiplication with Hadoop Map Reduce

- Matrix multiplication is a common operation in many applications that deal with large-scale data, such as machine learning, graph analysis, and linear algebra.
- Hadoop is a framework that allows for distributed processing of large data sets across clusters of computers using simple programming models.
- MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- Matrix multiplication with Hadoop MapReduce involves the following steps:
  - Define the input and output matrices, A and B, and their dimensions, m, n, and p.
  - Split the input matrices into blocks of rows and columns, and store them as key-value pairs in HDFS (Hadoop Distributed File System).
  - Write a mapper function that emits intermediate key-value pairs for each block of A and B, where the key is the index of the output matrix element, and the value is the block of A or B and its position.
  - Write a reducer function that receives all the intermediate values for a given output matrix element, and performs the dot product of the corresponding blocks of A and B, and emits the final key-value pair for the output matrix element.
  - Run the MapReduce job on the Hadoop cluster, and collect the output matrix from HDFS.

- An example of matrix multiplication with Hadoop MapReduce in Python is given below:

```python
# Matrix_Mapper.py
# This file contains the implementation of mapper.
# It maps keys according to the the matrix.
# For Example,
# A = |1 2|
#     |3 4|
# B = |5 6|
#     |7 8|
# C = A*B
# C = |19 22|
#     |43 50|
# The mapper will map the keys as follows
# A[0][0] -> C[0][0], C[0][1]
# A[0][1] -> C[0][0], C[0][1]
# A[1][0] -> C[1][0], C[1][1]
# A[1][1] -> C[1][0], C[1][1]
# B[0][0] -> C[0][0], C[1][0]
# B[0][1] -> C[0][1], C[1][1]
# B[1][0] -> C[0][0], C[1][0]
# B[1][1] -> C[0][1], C[1][1]

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # get the matrix name, row, column, and value
    matrix = words[0]
    row = int(words[1])
    col = int(words[2])
    val = int(words[3])
    # emit key-value pairs for each matrix element
    if matrix == "A":
        # for matrix A, the key is the row and column of the output matrix element
        # the value is the matrix name, the column of A, and the value of A
        for k in range(2):
            print '%d,%d\t%s,%d,%d' % (row, k, matrix, col, val)
    else:
        # for matrix B, the key is the row and column of the output matrix element
        # the value is the matrix name, the row of B, and the value of B
        for i in range(2):
            print '%d,%d\t%s,%d,%d' % (i, col, matrix, row, val)
```

```python
# Matrix_Reducer.py
# This file contains the implementation of reducer.
# It receives the intermediate values for a given output matrix element,
# and performs the dot product of the corresponding blocks of A and B,
# and emits the final key-value pair for the output matrix element.

import sys

# initialize the current key and the partial sum
current_key = None
current_sum = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    # convert value to