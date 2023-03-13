### Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source projects and tools that work together to provide a distributed computing platform for big data processing and analysis.
- Hadoop Eco System consists of four core components: Hadoop Distributed File System (HDFS), MapReduce, YARN and Hadoop Common.
- HDFS is a distributed file system that stores large volumes of data across multiple nodes in a cluster.
- MapReduce is a programming model and framework for parallel processing of data using key-value pairs.
- YARN is a resource management and scheduling layer that allocates and manages resources for applications running on Hadoop clusters.
- Hadoop Common is a set of libraries and utilities that support the other components of Hadoop Eco System.
- Some of the most well-known tools of the Hadoop Eco System include Hive, Pig, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.
- Hive is a data warehouse system that provides a SQL-like interface for querying and analyzing data stored in HDFS.
- Pig is a scripting language and platform for data transformation and analysis using MapReduce.
- Spark is a fast and general engine for large-scale data processing that supports batch, streaming, SQL, machine learning and graph processing.
- HBase is a distributed and scalable NoSQL database that provides random access and strong consistency for structured and semi-structured data.
- Oozie is a workflow scheduler and coordinator that manages and executes Hadoop jobs.
- Sqoop is a tool for transferring data between HDFS and relational databases.
- Zookeeper is a service for maintaining configuration information, naming, synchronization and group services for distributed applications.

- YARN stands for Yet Another Resource Negotiator and it is the second generation of Hadoop resource management system.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0 MapReduce, such as scalability, resource utilization, flexibility and compatibility.
- YARN splits the functionalities of resource management and job scheduling/monitoring into separate daemons: ResourceManager (RM) and ApplicationMaster (AM).
- ResourceManager is a global daemon that runs on a master node and is responsible for managing the cluster resources and allocating them to different applications.
- ApplicationMaster is a per-application daemon that runs on a worker node and is responsible for negotiating resources with the ResourceManager and coordinating the execution of tasks on the allocated containers.
- A container is a unit of resource allocation that consists of a certain amount of memory, CPU, disk and network bandwidth.
- An application is either a single job or a DAG (directed acyclic graph) of jobs that run on the YARN framework.
- YARN supports multiple types of applications, such as MapReduce, Spark, Hive, Pig, etc., by providing a generic ApplicationMaster interface that can be implemented by different frameworks.
- YARN also supports dynamic resource allocation, node labels, security, high availability, fault tolerance and federation features.

- A possible mnemonic to remember the four core components of Hadoop Eco System is: **H**ave **M**any **Y**ummy **H**amburgers (HDFS, MapReduce, YARN, Hadoop Common).
- A possible mnemonic to remember the main functions of ResourceManager and ApplicationMaster is: **R**esource **M**anager **A**llocates **R**esources, **A**pplication **M**aster **A**dministers **A**pplications (RM AR, AM AA).