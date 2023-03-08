 Here is the content in Markdown format:

### Cluster Specification

- A Hadoop cluster consists of multiple servers that work together.
- The main types of servers in a Hadoop cluster are:
 - Master node: Name node, Secondary name node, Job tracker node.
 - Slave/Worker node: Data node, Task tracker node.
- The servers can be commodity hardware and the key is in the ability to scale out as more data and compute power is required.
- The distributed and scalable architecture of Hadoop enables it to handle big data problems by distributing the data and processing across multiple nodes.
- The Hadoop ecosystem uses the master-slave architecture with the master node coordinating the slave nodes.

#### Installing Hive

- Hive can be installed in three modes:
 - Local mode: Hive is installed on a local system and uses the local filesystem.
 - Pseudo-distributed mode: Hive is installed on a single node of a cluster and uses the HDFS.
 - Fully-distributed mode: Hive is installed on multiple nodes of a cluster and uses the HDFS.
- The main steps to install Hive are:
 - Install Java (if not already installed)
 - Download Hive
 - Unpack the Hive archive
 - Configure Hive
 - Add Hive binaries to the PATH
 - Start the MetaStore service
 - Initialize the Hive schema
- Once installed, Hive can be started using the `hive` command on the command line. The Hive CLI allows running queries, scripts etc. on the data in HDFS.
- The key advantages of Hive are:
 - It provides a SQL-like interface to query and manage large datasets residing in Hadoop/HDFS.
 - It enables easy data summarization, ad-hoc queries and the creation of multi-step workflows/pipelines.
- The main limitations of Hive are:
 - It may not be suitable for low-latency queries.
 - The SQL-like language (HiveQL) may not be suitable for complex queries.
 - The additional layer of abstraction provided by Hive can lead to performance overhead.