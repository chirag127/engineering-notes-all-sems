# Hadoop Eco System and YARN

- Hadoop is an open source framework that allows distributed processing of large-scale data using clusters of commodity hardware.
- Hadoop consists of four main modules: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce, and Hadoop YARN.
- Hadoop Common provides the common utilities and libraries that are used by other Hadoop modules.
- HDFS is a distributed file system that stores data across multiple nodes in a cluster, providing high availability, fault tolerance, and scalability.
- MapReduce is a programming model that enables parallel processing of large data sets using key-value pairs.
- YARN is a resource management layer that allocates and manages the resources and schedules the jobs in a Hadoop cluster.
- YARN stands for Yet Another Resource Negotiator. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as low resource utilization, fixed data flow, and lack of support for non-MapReduce applications.
- YARN consists of two main components: a global ResourceManager (RM) and per-application ApplicationMaster (AM).
- The RM is responsible for managing the cluster resources, such as memory, CPU, disk, and network bandwidth. It also arbitrates the resource requests from different applications and assigns them to the available nodes.
- The AM is responsible for coordinating the execution of a specific application, such as a MapReduce job or a Spark application. It negotiates the resources with the RM, monitors the progress of the tasks, and handles the failures and retries.
- Each node in a YARN cluster has a NodeManager (NM) that communicates with the RM and the AMs. The NM reports the resource availability and usage of the node, and launches and kills the containers that run the tasks.
- A container is a unit of resource allocation in YARN. It specifies the amount of memory, CPU, disk, and network bandwidth that a task needs to run. A container can run any type of application, such as MapReduce, Spark, Hive, Pig, etc.
- YARN enables the Hadoop ecosystem to be more flexible, efficient, and scalable. It allows multiple applications to run on the same cluster, sharing the resources and data. It also supports dynamic data flow, interactive processing, and real-time analytics.