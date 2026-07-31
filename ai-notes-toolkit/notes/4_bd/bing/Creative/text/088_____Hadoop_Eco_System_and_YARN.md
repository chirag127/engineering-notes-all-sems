### Hadoop Eco System and YARN

- Hadoop is an open source framework that allows distributed processing of large-scale data using clusters of commodity hardware.
- Hadoop ecosystem refers to the various components and tools that work together to support Hadoop functionality, such as data ingestion, storage, processing, analysis, and visualization.
- YARN (Yet Another Resource Negotiator) is one of the core components of Hadoop ecosystem, introduced in Hadoop 2.0 to overcome the limitations of Hadoop 1.0 MapReduce.
- YARN is responsible for managing and allocating resources across the cluster, as well as scheduling and monitoring the execution of applications.
- YARN architecture consists of two main components: ResourceManager (RM) and ApplicationMaster (AM).
  - ResourceManager is the global authority that arbitrates resources among all the applications in the system. It has two sub-components: Scheduler and ApplicationsManager.
  - ApplicationMaster is the per-application framework that negotiates resources from the ResourceManager and works with the NodeManagers to execute and monitor the tasks.
- YARN enables the Hadoop ecosystem to support a variety of applications and frameworks, such as MapReduce, Spark, Hive, Pig, HBase, etc., by providing a common platform for resource management and isolation.
- YARN also improves the performance, scalability, and flexibility of the Hadoop ecosystem, by allowing multiple applications to run concurrently on the same cluster, and by supporting dynamic resource allocation and containerization.