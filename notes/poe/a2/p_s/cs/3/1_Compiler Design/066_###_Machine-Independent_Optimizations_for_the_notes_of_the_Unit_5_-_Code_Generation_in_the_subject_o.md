 Here is the content in Markdown format:

## Unit 2 - Hadoop and Map Reduce

1. **Hadoop**: Hadoop is an open-source software framework used for distributed storage and processing of big data sets using the MapReduce programming model. It is scalable, efficient, and fault-tolerant. The two major components of Hadoop are:
    - Hadoop Distributed File System (HDFS): Used for storing large data sets across multiple machines. It provides high throughput access to application data and is fault tolerant.
    - Hadoop MapReduce: A programming model for large scale data processing. It consists of two major tasks - Map and Reduce.

2. **MapReduce**: MapReduce is a distributed processing model for big data that consists of two major tasks:
    - **Map**: The master node takes the input and partitions it into multiple blocks and distributes them to mapper nodes. The mapper nodes process the blocks in parallel and emit intermediate key-value pairs.
    - **Reduce**: The intermediate key-value pairs are shuffled and sorted and sent to the reducer nodes. The reducer nodes aggregate the values for each key and output the final results.
    - Advantages: Scalable, Fault tolerant, Distributed processing.
    - Disadvantages: Not suitable for iterative algorithms or machine learning tasks.

3. **Word Count Example**: A classic example to understand MapReduce is to count the occurrences of each word in a file.
    - **Map**: Takes input as file and outputs (word, 1) for each word.
    - **Reduce**: Takes (word, list of 1s) and outputs (word, count) by summing up the 1s.

[Diagrams and examples can be added here to aid understanding]

MapReduce is a very powerful paradigm for processing huge amounts of data in a scalable and fault-tolerant manner. It forms the core of the Hadoop ecosystem and has a wide variety of applications in Big Data analytics.