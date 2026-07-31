# Unit 6 - Hadoop Eco System and YARN

## Hadoop Eco System

- The Hadoop Eco System refers to the various components of the Apache Hadoop software library that provide different functionalities for big data processing.
- The Hadoop Eco System includes open source projects as well as a complete range of complementary tools that work with Hadoop.
- Some of the most well-known tools of the Hadoop Eco System are:
  - HDFS: The distributed file system that stores data across multiple nodes in a cluster.
  - MapReduce: The programming model that enables parallel processing of large-scale data using key-value pairs.
  - YARN: The resource management and job scheduling framework that coordinates the execution of applications on Hadoop.
  - Hive: The data warehouse system that provides SQL-like query language and schema-on-read for structured and semi-structured data.
  - Pig: The high-level scripting language that allows data analysis and transformation using a set of operators.
  - Spark: The fast and general-purpose engine for large-scale data processing that supports batch, streaming, SQL, machine learning and graph analytics.
  - HBase: The distributed and scalable NoSQL database that provides random access and strong consistency for structured and semi-structured data.
  - Oozie: The workflow scheduler that manages and executes Hadoop jobs in a predefined sequence or based on data availability.
  - Sqoop: The tool that transfers data between Hadoop and relational databases.
  - Zookeeper: The service that provides coordination, configuration and synchronization for distributed systems.

## YARN

- YARN stands for Yet Another Resource Negotiator. It is the resource management and job scheduling framework that was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0.
- YARN splits the functionalities of resource management and job scheduling/monitoring into separate daemons. The main components of YARN are:
  - ResourceManager (RM): The global daemon that manages the allocation and utilization of resources (such as memory and CPU) across the cluster. It has two sub-components:
    - Scheduler: The module that assigns resources to applications based on various policies and constraints.
    - ApplicationsManager: The module that accepts and rejects application submissions and tracks the status of running applications.
  - NodeManager (NM): The per-node daemon that monitors and reports the resource usage and health of each node to the ResourceManager. It also launches and manages the containers that run the application tasks.
  - ApplicationMaster (AM): The per-application daemon that negotiates resources with the ResourceManager and coordinates the execution of tasks across the NodeManagers. It also communicates with the client and handles the application-specific logic.
  - Container: The unit of resource allocation and execution in YARN. It is a collection of resources (such as memory and CPU) that is assigned to a node and used to run a task. A container can run multiple tasks of the same application, but not tasks of different applications.