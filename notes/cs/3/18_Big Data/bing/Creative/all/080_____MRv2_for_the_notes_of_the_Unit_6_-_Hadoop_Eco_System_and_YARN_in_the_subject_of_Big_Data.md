# MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture of MapReduce introduced in Hadoop 0.23 .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, as the resource management layer for Hadoop .
- YARN splits the two major functions of the JobTracker in MRv1, which are resource management and job scheduling/monitoring, into separate daemons  .
- The main components of YARN are:
  - ResourceManager: a global daemon that manages the allocation of resources (such as memory and CPU) to applications across the cluster  .
  - NodeManager: a per-node daemon that monitors the resource usage and health of the node, and communicates with the ResourceManager  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager, and coordinates the execution of tasks on the NodeManagers  .
  - Container: a unit of resource allocation that encapsulates a set of resources (such as memory and CPU) and a set of tasks (such as map or reduce) to run on a NodeManager  .
- The benefits of MRv2 over MRv1 are:
  - Increased scalability of the cluster, as the ResourceManager can handle more nodes and applications than the JobTracker .
  - Improved cluster utilization, as the resources can be dynamically allocated and shared among different applications and frameworks .
  - Support for non-MapReduce jobs, such as Spark, Tez, and Storm, that can run on YARN as well .
  - Enhanced fault tolerance, as the ApplicationMaster can restart failed tasks and containers without affecting the ResourceManager .