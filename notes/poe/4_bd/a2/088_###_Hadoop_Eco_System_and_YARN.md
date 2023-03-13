 Here is the content in markdown format for the topic ### Hadoop Eco System and YARN:

### Hadoop Eco System and YARN

The Hadoop Ecosystem refers to the collection of tools and technologies that are designed to work with the Hadoop Framework. The Hadoop Ecosystem includes components such as:

- HDFS - Hadoop Distributed File System - Used for storing large data on the cluster.
- MapReduce - A programming model for large scale data processing.
- YARN - Yet Another Resource Negotiator - A cluster resource management technology.
- Hive - A data warehouse infrastructure built on top of Hadoop for data summarization, query, and analysis.
- Pig - A high-level data-flow language and execution framework for parallel computation.
- HBase - A distributed, scalable, big data store.
- ZooKeeper - A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
- Oozie - A workflow scheduler system to manage Hadoop jobs.

YARN (Yet Another Resource Negotiator) is the cluster management technology in Hadoop 2. The key features of YARN are:

- Separates the resource management and job scheduling/monitoring functions.
- Supports multiple data processing frameworks, not just MapReduce.
- Improved utilization of cluster resources.
- Scalability and high availability.

The main components of YARN are:

- ResourceManager - Manages resources (memory, CPU, etc.) in the cluster.
- NodeManager - Manages resources on a single machine and executors tasks on that machine.
- ApplicationMaster - Negotiates resources from the ResourceManager and works with the NodeManager(s) to execute and monitor the tasks of an application.

Some key benefits of YARN are:

- Better utilization of cluster resources as multiple applications can run simultaneously.
- Fault tolerance through redundancy. If an ApplicationMaster or NodeManager fails, the system redirects work to other nodes.
- Scalability to handle very large clusters with thousands of nodes.

[Include detailed diagrams, examples, advantages, disadvantages, applications, etc. if required.]