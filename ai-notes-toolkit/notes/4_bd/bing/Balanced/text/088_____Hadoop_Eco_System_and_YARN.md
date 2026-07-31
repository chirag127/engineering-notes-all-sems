### Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source software components and tools that work together to provide a distributed computing platform for big data processing and analysis.
- Some of the most well-known components of the Hadoop Eco System are HDFS, MapReduce, YARN, Hive, Pig, HBase, Spark, Oozie, Sqoop, Zookeeper, etc.
- YARN stands for Yet Another Resource Negotiator. It is a sub-project of Hadoop that provides a framework for resource management and job scheduling in a Hadoop cluster.
- YARN was introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0, such as scalability, efficiency, and flexibility.  
- YARN consists of two main components: a global ResourceManager (RM) that allocates resources across the cluster, and a per-application ApplicationMaster (AM) that coordinates the execution of tasks for each application.
- YARN supports multiple types of applications, not just MapReduce, and allows them to run concurrently on the same cluster.
- YARN also offers features such as security, high availability, fault tolerance, and dynamic resource allocation.