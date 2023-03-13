### Hadoop Eco System and YARN

- Hadoop is an open source framework that allows for distributed processing of large and complex data sets across clusters of computers.
- Hadoop consists of four main modules: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce and Hadoop YARN.
- Hadoop Common provides the common utilities and libraries that are used by other Hadoop modules.
- HDFS is a distributed file system that stores data across multiple nodes in a cluster, providing high availability, fault tolerance and scalability.
- MapReduce is a programming model and execution engine that enables parallel processing of data using key-value pairs.
- YARN is the resource management and job scheduling layer of Hadoop that allocates and manages the resources and keeps all things working as they should.
- YARN stands for Yet Another Resource Negotiator. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce in Hadoop 1.0, such as low resource utilization, lack of support for non-MapReduce applications and fixed job execution model.
- YARN splits up the functionalities of resource management and job scheduling/monitoring into separate daemons: a global ResourceManager (RM) and per-application ApplicationMaster (AM).
- The RM is responsible for managing the cluster resources, such as memory, CPU, disk and network bandwidth. It also arbitrates resource requests from competing applications.
- The AM is responsible for coordinating the execution of a specific application, such as a MapReduce job or a Spark application. It requests resources from the RM, communicates with the NodeManagers (NMs) that run the application tasks and monitors the progress and status of the application.
- The NM is a daemon that runs on each node in the cluster and manages the containers that run the application tasks. A container is a unit of resource allocation that consists of a certain amount of memory, CPU, disk and network bandwidth. The NM also monitors the health and performance of the node and reports to the RM.
- YARN enables the Hadoop ecosystem to be more flexible, efficient and scalable. It allows for multiple types of applications to run on the same cluster, such as MapReduce, Spark, Hive, Pig, HBase, etc. It also supports dynamic resource allocation, high availability, security and isolation.