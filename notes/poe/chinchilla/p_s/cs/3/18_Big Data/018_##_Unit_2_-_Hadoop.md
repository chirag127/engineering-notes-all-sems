## Unit 2 - Hadoop

Hadoop is an open-source framework for distributed storage and processing of big data. This unit covers the following topics:

### Hadoop Distributed File System (HDFS)

- HDFS is the distributed file system used by Hadoop.
- It is designed to handle large files and is fault-tolerant.
- HDFS stores files in blocks, which are replicated across multiple nodes in the cluster.
- HDFS has a Namenode and multiple Datanodes. The Namenode is responsible for managing the file system namespace and the Datanodes store the actual data.
- HDFS supports file streaming, which allows data to be written to and read from a file concurrently.

### MapReduce

- MapReduce is a programming model used for processing large data sets in a distributed environment.
- It consists of two phases: map and reduce.
- In the map phase, data is processed in parallel across multiple nodes in the cluster.
- In the reduce phase, the results from the map phase are combined to produce the final output.
- MapReduce is fault-tolerant, as it automatically handles node failures and reschedules tasks on other nodes.
- Hadoop provides a MapReduce framework for implementing MapReduce programs.

### YARN

- YARN (Yet Another Resource Negotiator) is the resource management framework introduced in Hadoop 2.
- YARN separates the resource management and job scheduling functions of Hadoop.
- YARN allows for multiple processing engines to run on the same Hadoop cluster, including MapReduce and Apache Spark.
- YARN provides a flexible and scalable platform for running distributed applications.

### Running MRv1 in YARN

- MRv1 (MapReduce version 1) is the original MapReduce implementation used in Hadoop.
- MRv1 can be run in YARN using the MapReduce Application Master.
- Running MRv1 in YARN provides better resource utilization and scalability than running it in standalone mode.
- However, MRv1 in YARN has certain limitations, such as not being able to run multiple jobs simultaneously.
- Organizations that have already invested in MRv1 can continue to use it in YARN, while also taking advantage of the benefits of YARN.

Overall, Hadoop is a powerful framework for processing large data sets in a distributed environment. By understanding the components of Hadoop, such as HDFS, MapReduce, and YARN, and how they work together, you can build scalable and fault-tolerant big data applications.