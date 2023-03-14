Hadoop Eco System Frameworks are a set of tools, libraries, and frameworks that help you build applications on top of Apache Hadoop. Hadoop provides massive parallelism with low latency and high throughput, which makes it well-suited for big data problems.

The core component of the Hadoop Eco System Frameworks is the Hadoop Distributed File System (HDFS), which is a distributed file system that provides high-throughput access to application data with no need for schemas to be defined up front. HDFS consists of two types of nodes: NameNode and DataNode. NameNode is the master node that stores the metadata of the files and directories, while DataNode is the worker node that stores the actual data blocks.

Another core component of the Hadoop Eco System Frameworks is the Yet Another Resource Negotiator (YARN), which is a resource-management platform responsible for managing compute resources in clusters and using them to schedule users’ applications. YARN consists of three components: ResourceManager, NodeManager, and ApplicationMaster. ResourceManager is the global scheduler that allocates resources to different applications, NodeManager is the agent that runs on each node and monitors the resource usage, and ApplicationMaster is the per-application framework that negotiates resources with the ResourceManager and coordinates the execution of tasks on the NodeManager.

A third core component of the Hadoop Eco System Frameworks is the MapReduce, which is a programming model for large-scale data processing. MapReduce consists of two phases: Map and Reduce. Map phase takes a set of input key-value pairs and transforms them into a set of intermediate key-value pairs, while Reduce phase takes the intermediate key-value pairs and aggregates them into a set of output key-value pairs. MapReduce can run on top of YARN or as a standalone service.

Hadoop Common is the fourth core component of the Hadoop Eco System Frameworks, which includes the libraries and utilities used and shared by other Hadoop modules. Hadoop Common provides the common functionalities such as configuration, logging, security, and serialization.

Besides the four core components, there are many other tools and applications that are part of the Hadoop Eco System Frameworks, such as Apache Pig, Apache Hive, Apache HBase, Apache Spark, Presto, and Apache Zeppelin. These tools provide various services such as query-based processing, in-memory processing, NoSQL database, machine learning, searching, indexing, and visualization of big data  .

The following diagram illustrates the basic architecture of the Hadoop Eco System Frameworks using ASCII art:

```
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|    Apache Pig     | |    Apache Hive    | |    Apache HBase   |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|    Apache Spark   | |      Presto       | |  Apache Zeppelin  |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|     MapReduce     | |       YARN        | |       HDFS        |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|   ApplicationMaster| |   ResourceManager | |     NameNode      |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|    NodeManager    | |    NodeManager    | |    DataNode       |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|    NodeManager    | |    NodeManager    | |    DataNode       |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
|                   | |                   | |                   |
|    NodeManager    | |    NodeManager    | |    DataNode       |
|                   | |                   | |                   |
+-------------------+ +-------------------+ +-------------------+
```