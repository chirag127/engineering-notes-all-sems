 Here is the formal content written in Markdown format without any emojis or external links under the header ## Unit 2 - Hadoop:

## Unit 2 - Hadoop

1. Hadoop is an open-source software framework for distributed storage and processing of very large data sets on computer clusters built from commodity hardware.

2. The core of Apache Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part which is a MapReduce programming model.

3. HDFS:

- HDFS stores large files across multiple machines.
- It splits files into large blocks (typically 128 MB) and stores them on multiple DataNodes.
- It is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- It provides high throughput access to application data and is suitable for applications that have large data sets.

4. MapReduce:

- It is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.
- It consists of two major tasks - Map and Reduce.
- The Map task partitions the input data into chunks which are processed in parallel by the Map tasks.
- The Reduce task aggregates the outputs of the Map tasks and produces the final output.
- MapReduce is scalable and fault-tolerant and hides the complexities of parallelization and fault-tolerance from the application developer.

5. Hadoop ecosystem:

- Hadoop ecosystem consists of several other components apart from HDFS and MapReduce like Hive, Pig, HBase, ZooKeeper, Oozie, Sqoop, Flume, etc. which provide capabilities for performing different types of tasks.
- These different components of the Hadoop ecosystem help to solve different problems and use cases.