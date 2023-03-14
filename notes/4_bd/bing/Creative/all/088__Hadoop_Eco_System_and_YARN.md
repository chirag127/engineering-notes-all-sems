### Hadoop Eco System and YARN

- Hadoop Eco System is a collection of various components and tools that work together to provide a scalable, reliable and efficient platform for big data processing and analysis.
- Some of the most well-known tools of the Hadoop Eco System are HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.
- HDFS is the distributed file system that stores large files across multiple nodes in a cluster. It has a master-slave architecture with a NameNode and DataNodes.
- Hive is a data warehousing tool that provides a SQL-like interface to query and analyze data stored in HDFS. It translates queries into MapReduce jobs and supports data summarization, partitioning and bucketing.
- Pig is a scripting language that allows users to write complex data transformations and analysis using a high-level syntax. It also translates scripts into MapReduce jobs and supports user-defined functions and operators.
- YARN is the resource management and job scheduling layer of Hadoop. It stands for Yet Another Resource Negotiator and it separates the processing layer from the resource management layer.
- YARN has two main components: Resource Manager and Node Manager. Resource Manager is the master daemon that allocates resources and assigns tasks to the nodes. Node Manager is the slave daemon that runs on each node and monitors the resource usage and task execution.
- YARN also supports Application Master, which is a per-application framework that negotiates resources with the Resource Manager and coordinates the execution of tasks across the nodes.
- YARN enables Hadoop to support different types of processing, such as batch, interactive, streaming and real-time. It also improves the scalability, efficiency and flexibility of the Hadoop cluster.
- MapReduce is the data processing layer of Hadoop that implements the map and reduce functions to process large datasets in parallel. It works with YARN to distribute and execute the tasks across the cluster.
- Spark is a fast and general-purpose data processing engine that can run on top of YARN. It supports in-memory computation, SQL, streaming, machine learning and graph processing. It also provides APIs in Java, Python, Scala and R.
- HBase is a distributed and column-oriented database that runs on top of HDFS. It provides low-latency and random access to large amounts of structured and semi-structured data. It also supports versioning, compression and replication.
- Oozie is a workflow scheduler that manages and coordinates the execution of Hadoop jobs. It supports both MapReduce and Spark jobs, as well as Pig and Hive scripts. It also supports dependency management, retry policies and notifications.
- Sqoop is a tool that transfers data between Hadoop and relational databases. It supports bulk import and export of data using JDBC connectors. It also supports incremental updates, compression and partitioning.
- Zookeeper is a distributed coordination service that provides reliable and consistent configuration, synchronization and naming for Hadoop components. It also supports leader election, group membership and distributed locking.

A possible mnemonic to remember the Hadoop Eco System components is:

**H**ave **H**igh **P**erformance **Y**ARN **M**anage **S**park **H**Base **O**ozie **S**qoop **Z**ookeeper

A possible ascii diagram to illustrate the YARN architecture is:

```
+-----------------+      +-----------------+
|                 |      |                 |
|   Resource      |      |   Node          |
|   Manager       |      |   Manager       |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|   Scheduler     |      |   Container     |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|   Application   |      |   Application   |
|   Manager       |      |   Master        |
|                 |      |                 |
+-----------------+      +-----------------+
         |                      |
         |                      |
         +----------------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |