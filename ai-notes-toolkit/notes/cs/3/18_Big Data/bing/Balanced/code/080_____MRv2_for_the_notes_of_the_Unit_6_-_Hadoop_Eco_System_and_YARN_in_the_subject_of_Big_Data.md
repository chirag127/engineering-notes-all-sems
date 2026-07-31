### MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture of MapReduce introduced in Hadoop 0.23  .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, which is a framework for managing and scheduling resources in a Hadoop cluster .
- MRv2 splits the two major functions of the JobTracker in MRv1, which are resource management and job scheduling/monitoring, into separate components  .
- The new components in MRv2 are:
  - ResourceManager: a global daemon that manages the allocation of resources (such as memory and CPU) to applications in the cluster  .
  - NodeManager: a per-node daemon that monitors the resource usage and health of the node, and communicates with the ResourceManager  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager, and coordinates the execution of tasks on the NodeManagers  .
- The benefits of MRv2 over MRv1 are:
  - Increased scalability: the ResourceManager can handle more nodes and applications than the JobTracker .
  - Improved utilization: the NodeManagers can run any type of tasks, not just MapReduce, and can dynamically adjust the resource allocation based on the demand .
  - Support for non-MR jobs: the ApplicationMasters can implement different frameworks and paradigms, such as Spark, Tez, and Storm, on top of YARN .
  - Enhanced fault tolerance: the ApplicationMasters can recover from failures and restart tasks without affecting the ResourceManager .