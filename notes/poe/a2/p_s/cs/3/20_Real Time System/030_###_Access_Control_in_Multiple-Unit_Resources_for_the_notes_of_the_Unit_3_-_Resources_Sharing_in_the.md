 Here is the content in markdown format:

## Hadoop Environment

1. Hadoop Distributed File System (HDFS) - HDFS is the primary storage system used by Hadoop applications. It splits files into large blocks and distributes them across nodes in a cluster. This allows for streaming access of large files at high throughput.

2. MapReduce - MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It consists of two major tasks - Map, which splits and processes the input, and Reduce, which aggregates the results. MapReduce implementations like Hadoop's MapReduce framework handle distributing tasks and managing resources.

3. YARN - YARN (Yet Another Resource Negotiator) is the resource management platform for Hadoop. It separates resource management and job scheduling/monitoring from the programming framework (like MapReduce). This design allows multiple frameworks, such as MapReduce, Spark, and Flink, to run on YARN and share a common pool of cluster resources.

4. Common - The Hadoop Common package contains libraries and utilities needed by other Hadoop modules. This includes configuration files, log4j for logging, and utilities for compression, data integrity, and serialization.

Advantages:

- Scalable and Fault Tolerant - Hadoop is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Fault tolerance is built in, so jobs are not affected by failures of individual machines.
- Cost Effective - Hadoop runs on commodity hardware and open source software, keeping costs low.
- Flexible - Hadoop's modular architecture allows swapping out and supplementing components as needed. Different processing frameworks can run on the environment.

Applications:

- Web indexing
- Genomics sequence analysis
- Log and server log analysis
- Image processing
- Social network analysis
- predictive modeling