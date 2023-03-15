# Unit 6 - Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source projects and tools that work together to provide a distributed computing platform for big data processing and analysis.
- Some of the most well-known components of the Hadoop Eco System are HDFS, MapReduce, YARN, Hive, Pig, HBase, Spark, Oozie, Sqoop, Zookeeper, etc.
- YARN stands for Yet Another Resource Negotiator. It is a sub-project of Hadoop that provides a framework for resource management and job scheduling in a Hadoop cluster.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0, such as scalability, efficiency, and flexibility. 
- YARN consists of two main components: a global ResourceManager (RM) and per-application ApplicationMaster (AM).
- The ResourceManager is responsible for allocating and managing the resources (such as CPU, memory, disk, network) across the cluster nodes.
- The ApplicationMaster is responsible for coordinating and monitoring the execution of the application tasks on the allocated resources.
- YARN supports multiple types of applications, not just MapReduce, such as Spark, Hive, Pig, etc. by providing a common interface for resource negotiation and task execution.
- YARN also offers features such as security, high availability, fault tolerance, and dynamic resource allocation.