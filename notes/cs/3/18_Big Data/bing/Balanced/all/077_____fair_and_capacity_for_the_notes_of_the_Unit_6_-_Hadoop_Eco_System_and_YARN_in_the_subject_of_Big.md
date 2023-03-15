# Unit 6 - Hadoop Eco System and YARN

## Hadoop Eco System

- The Hadoop Eco System refers to the various components of the Apache Hadoop software library that provide different functionalities for big data processing.
- The Hadoop Eco System includes open source projects as well as a complete range of complementary tools that can be integrated with Hadoop.
- Some of the most well-known tools of the Hadoop Eco System are:
  - HDFS: The Hadoop Distributed File System that stores large volumes of data across multiple nodes in a cluster.
  - MapReduce: The programming model that allows parallel processing of data using key-value pairs.
  - YARN: The resource management and job scheduling framework that enables multiple applications to run on Hadoop.
  - Hive: The data warehouse system that provides SQL-like query language for data analysis.
  - Pig: The scripting language that allows data transformation and manipulation using high-level operators.
  - Spark: The fast and general-purpose engine for large-scale data processing that supports batch, streaming, SQL, machine learning and graph analytics.
  - HBase: The distributed and scalable NoSQL database that provides random access and consistent updates for structured and semi-structured data.
  - Oozie: The workflow scheduler that orchestrates and coordinates the execution of Hadoop jobs.
  - Sqoop: The tool that transfers data between Hadoop and relational databases.
  - Zookeeper: The service that provides coordination, configuration and synchronization for distributed systems.

## YARN

- YARN stands for Yet Another Resource Negotiator. It is the resource management and job scheduling framework that enables multiple applications to run on Hadoop.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0, such as scalability, resource utilization, and application diversity.
- YARN splits up the functionalities of resource management and job scheduling/monitoring into separate daemons. The main components of YARN are:
  - ResourceManager (RM): The global daemon that manages the resources and allocates them to different applications based on their requirements and priorities.
  - ApplicationMaster (AM): The per-application daemon that negotiates resources with the RM, monitors the progress of the application, and handles failures and retries.
  - NodeManager (NM): The per-node daemon that monitors the resource usage and health of the node, and communicates with the RM and AM.
  - Container: The unit of resource allocation that consists of a fixed amount of memory, CPU, disk and network bandwidth. A container can run a single task or a process of an application.
- YARN provides the following advantages over Hadoop 1.0:
  - Scalability: YARN can support up to 10,000 nodes and 100,000 tasks in a cluster, compared to 4,000 nodes and 40,000 tasks in Hadoop 1.0.
  - Resource utilization: YARN can dynamically allocate resources to different applications based on their needs and availability, rather than pre-assigning fixed slots of map and reduce tasks.
  - Application diversity: YARN can support various types of applications besides MapReduce, such as Spark, Hive, Pig, HBase, etc. YARN also allows customizing the AM for different application logic and optimization.