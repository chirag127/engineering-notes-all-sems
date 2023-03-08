 Here is the content in markdown format for the topic ### components of Hadoop for the notes of the Unit 2 - Hadoop in the subject of Big Data:

### Components of Hadoop

The Hadoop ecosystem consists of the following main components:

1. HDFS (Hadoop Distributed File System): HDFS is the primary storage system used by Hadoop. It is designed to store large data sets reliably, and to stream those data sets at high bandwidth to user applications. HDFS splits files into large blocks and distributes them across multiple nodes in a cluster.

2. MapReduce: MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. MapReduce consists of two main tasks - Map and Reduce. The Map task splits the input data into smaller chunks which are processed in parallel by the cluster nodes. The Reduce task aggregates the outputs of the Map tasks and produces the final output.

3. YARN (Yet Another Resource Negotiator): YARN is the resource management platform for Hadoop. It splits up the functionality of job scheduling and cluster resource management so that each can be handled by a separate, dedicated component. YARN consists of a central ResourceManager and per-node NodeManagers. The ResourceManager schedules applications and allocates resources, while the NodeManagers launch and monitor applications.

4. Hive: Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis. It converts queries written in a SQL-like declarative language called HiveQL into MapReduce jobs. Hive makes it easy for users with limited technical skills to interact with data stored in HDFS.

5. Pig: Pig is a high-level data-flow language and execution framework for parallel computation. It converts complex data processing into sequences of MapReduce programs. The language includes mechanisms for data grouping, filtering, joining, splitting, and iterations. Pig makes it possible to express complex data processing tasks in a simpler manner than writing low-level MapReduce programs in Java.

[Detailed diagrams, code examples, advantages, disadvantages, and applications can be added here for further understanding and reference.]