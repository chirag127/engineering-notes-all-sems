# Unit 6 - Hadoop Eco System and YARN

## Hadoop Eco System

- The Hadoop Eco System is a collection of open source projects and tools that work together to provide various functionalities for big data processing and analysis.
- Some of the most well-known tools of the Hadoop Eco System are:
  - HDFS: The distributed file system that stores data across multiple nodes in a cluster.
  - MapReduce: The programming model that enables parallel processing of large-scale data using key-value pairs.
  - YARN: The resource management framework that allocates and schedules resources for applications running on Hadoop.
  - Hive: The data warehouse system that provides SQL-like query language for data analysis and manipulation.
  - Pig: The scripting language that allows users to write complex data transformations using a high-level syntax.
  - Spark: The fast and general-purpose engine for large-scale data processing, supporting batch, streaming, SQL, ML and graph analytics.
  - HBase: The distributed and scalable database that provides random access and consistent updates for structured and semi-structured data.
  - Oozie: The workflow scheduler that manages and coordinates the execution of jobs and tasks on Hadoop.
  - Sqoop: The tool that transfers data between Hadoop and relational databases.
  - Zookeeper: The service that provides coordination, configuration and synchronization for distributed systems.

## YARN

- YARN stands for Yet Another Resource Negotiator. It is the resource management framework that was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0's MapReduce.
- YARN splits the functionalities of resource management and job scheduling/monitoring into separate daemons: the ResourceManager (RM) and the ApplicationMaster (AM).
- The ResourceManager is the global authority that manages the resources and the cluster. It consists of two components: the Scheduler and the ApplicationsManager.
  - The Scheduler is responsible for allocating resources to applications based on various criteria such as capacity, fairness, priority, etc.
  - The ApplicationsManager is responsible for accepting and rejecting application submissions, and tracking the status and progress of applications.
- The ApplicationMaster is the per-application entity that negotiates resources from the ResourceManager and works with the NodeManagers to execute and monitor the tasks.
- The NodeManager is the per-node agent that monitors the resource usage and health of the node, and communicates with the ResourceManager and the ApplicationMaster.
- YARN enables the Hadoop Eco System to support a variety of applications and frameworks, such as MapReduce, Spark, Hive, Pig, etc. It also provides performance enhancements, scalability, flexibility and fault tolerance for the Hadoop cluster.