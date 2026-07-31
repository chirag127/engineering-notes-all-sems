## Unit 2 - Hadoop and Map Reduce

- **Hadoop** is an open-source software framework for storing and processing large datasets using distributed computing.
- It is designed to scale up from a single server to thousands of machines, each offering local computation and storage.
- Hadoop consists of two main components: the **Hadoop Distributed File System (HDFS)** and the **MapReduce** programming model.
- HDFS is a distributed file system that provides high-throughput access to application data. It is designed to be fault-tolerant and to run on commodity hardware.
- **MapReduce** is a programming model for processing large datasets in parallel across a cluster of machines.
- In the MapReduce model, the data is divided into chunks and processed by the **map** function, which produces a set of intermediate key-value pairs.
- These intermediate key-value pairs are then shuffled and sorted by the framework and fed into the **reduce** function, which produces the final output.
- Hadoop and MapReduce are widely used in big data processing, including data mining, machine learning, and data analysis.