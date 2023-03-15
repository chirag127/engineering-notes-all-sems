#### Map Reduce features

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- Map Reduce consists of two phases: map and reduce. The map phase applies a user-defined function to each input key-value pair and produces a set of intermediate key-value pairs. The reduce phase aggregates all the intermediate values associated with the same intermediate key and produces the final output.
- Map Reduce features include:
  - Scalability: Map Reduce can scale up to thousands of nodes and handle petabytes of data.
  - Fault-tolerance: Map Reduce can handle node failures and network partitions by re-executing the failed tasks on other nodes.
  - Simplicity: Map Reduce abstracts away the details of parallelization, distribution, load balancing, and fault recovery, and allows the programmer to focus on the logic of the application.
  - Flexibility: Map Reduce can process various types of data, such as structured, semi-structured, or unstructured, and support various types of operations, such as filtering, aggregation, join, or sorting.
  - Efficiency: Map Reduce can exploit the locality of data by moving the computation to the data, rather than the other way around, and minimize the data transfer over the network.
  - Compatibility: Map Reduce can work with various file systems, such as local file system, Hadoop Distributed File System (HDFS), or Amazon Simple Storage Service (S3), and various data formats, such as text, binary, or XML.
- A mnemonic to remember the Map Reduce features is: **SFSFEC** (Scalability, Fault-tolerance, Simplicity, Flexibility, Efficiency, Compatibility).