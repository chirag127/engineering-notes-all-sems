## Unit 6 - Hadoop Eco System and YARN

- Hadoop Eco System is a collection of open source projects and tools that work together to provide various functionalities for big data processing and analysis on top of the Hadoop distributed file system (HDFS).
- Some of the most well-known tools of the Hadoop Eco System include HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.
- YARN stands for Yet Another Resource Negotiator. It is a framework for resource management and job scheduling in Hadoop clusters. It was introduced in Hadoop 2.0 to overcome the limitations of MapReduce 1.0, such as scalability, resource utilization, and flexibility. 
- The main components of YARN are:
  - ResourceManager (RM): It is a global daemon that runs on the master node and is responsible for allocating and managing the resources across the cluster. It also performs job scheduling and load balancing.
  - NodeManager (NM): It is a local daemon that runs on each slave node and is responsible for monitoring and reporting the resource usage and health of the node to the RM. It also launches and manages the containers that run the application tasks.
  - ApplicationMaster (AM): It is a per-application daemon that runs on a container assigned by the RM and is responsible for negotiating and obtaining the resources from the RM, coordinating and monitoring the execution of the application tasks, and communicating with the NM.
  - Container: It is a logical unit of resources (such as memory, CPU, disk, network, etc.) that is allocated by the RM and used by the application tasks. A container can run one or more tasks of the same or different applications.
- The main advantages of YARN are:
  - It improves the scalability of the cluster by supporting up to 10,000 nodes and 1,00,000 tasks.
  - It improves the resource utilization of the cluster by dynamically allocating and releasing the resources based on the application needs and cluster availability.
  - It improves the flexibility of the cluster by supporting multiple programming models and frameworks other than MapReduce, such as Spark, Hive, Pig, etc.
  - It improves the reliability of the cluster by isolating the failures of the applications from the RM and the NM, and providing fault tolerance and recovery mechanisms for the applications.