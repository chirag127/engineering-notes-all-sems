# Unit 6 - Hadoop Eco System and YARN

## Hadoop Eco System

- The Hadoop Eco System is a collection of open source projects and tools that work together to provide a scalable and reliable platform for big data processing and analysis.
- Some of the most well-known tools of the Hadoop Eco System include:
  - HDFS: A distributed file system that stores large volumes of data across multiple nodes in a cluster.
  - MapReduce: A programming model and framework for parallel processing of data using key-value pairs.
  - YARN: A resource management and scheduling system that enables multiple applications to run on the same cluster.
  - Hive: A data warehouse and query engine that provides SQL-like interface for data analysis.
  - Pig: A scripting language and platform for data transformation and manipulation.
  - Spark: A fast and general engine for large-scale data processing, supporting batch, streaming, SQL, ML and graph analytics.
  - HBase: A distributed and scalable NoSQL database that supports random read/write access to large tables.
  - Oozie: A workflow scheduler and coordinator that manages and executes Hadoop jobs.
  - Sqoop: A tool for transferring data between Hadoop and relational databases.
  - Zookeeper: A service for maintaining configuration information, naming, and synchronization for distributed systems.

## YARN

- YARN stands for Yet Another Resource Negotiator. It is a major component of Hadoop 2.0 that provides a more flexible and efficient way of managing and scheduling resources in a Hadoop cluster.
- YARN splits the functionalities of resource management and job scheduling/monitoring into separate daemons. The main components of YARN are:
  - ResourceManager (RM): A global service that allocates and manages resources across the cluster. It consists of two sub-components:
    - Scheduler: Responsible for assigning resources to applications based on various policies and constraints.
    - ApplicationsManager: Responsible for accepting and rejecting application submissions, and tracking the status and progress of applications.
  - NodeManager (NM): A per-node service that monitors and reports the resource utilization and health of the node. It also launches and manages containers that run the application tasks.
  - ApplicationMaster (AM): A per-application service that negotiates resources with the RM, and coordinates and monitors the execution of tasks in the containers. It also communicates with the client and provides feedback on the application status.
  - Container: A logical unit of resources (CPU, memory, disk, network) that is allocated by the RM and used by the AM to run the application tasks. A container can run any type of executable, such as a MapReduce task, a Spark task, or a custom application.