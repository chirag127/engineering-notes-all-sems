# MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture of MapReduce introduced in Hadoop 0.23 .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, as the resource management layer for Hadoop .
- YARN splits the two major functions of the JobTracker in MRv1, which are resource management and job scheduling/monitoring, into separate daemons  .
- The main components of YARN are:
  - ResourceManager: a global daemon that manages the allocation of resources (such as memory and CPU) to applications across the cluster  .
  - NodeManager: a per-node daemon that monitors the resource usage of containers and reports to the ResourceManager  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager and coordinates the execution of tasks across the NodeManagers  .
  - Container: a unit of resource allocation that can run a task or an ApplicationMaster  .
- The advantages of MRv2 over MRv1 are:
  - Increased scalability of the cluster, as the ResourceManager can handle more nodes and applications than the JobTracker .
  - Improved cluster utilization, as the resources can be dynamically allocated to different applications based on their needs and priorities .
  - Support for non-MapReduce jobs, such as Spark, Tez, and Storm, that can run on YARN and leverage its resource management capabilities .
  - Enhanced job scheduling and monitoring, as the ApplicationMaster can implement custom logic and policies for its tasks  .