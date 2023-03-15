### MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture of MapReduce introduced in Hadoop 0.23  .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, which is a framework for managing and scheduling resources in a Hadoop cluster  .
- MRv2 splits the two major functions of the JobTracker in MRv1, which are resource management and job scheduling/monitoring, into separate components  .
- The new components in MRv2 are:
  - ResourceManager: a global daemon that manages the allocation of resources (such as memory and CPU) to applications in the cluster  .
  - NodeManager: a per-node daemon that monitors the resource usage and health of the node, and communicates with the ResourceManager  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager, and coordinates the execution of tasks on the NodeManagers  .
- The benefits of MRv2 over MRv1 are:
  - Increased scalability: the ResourceManager can handle more nodes and applications than the JobTracker  .
  - Improved cluster utilization: the resources can be dynamically allocated and shared among different applications, and can be used for any type of task, not just MapReduce  .
  - Support for non-MR jobs: the ApplicationMaster can run any kind of application, such as Spark, Tez, or Storm, on top of YARN  .