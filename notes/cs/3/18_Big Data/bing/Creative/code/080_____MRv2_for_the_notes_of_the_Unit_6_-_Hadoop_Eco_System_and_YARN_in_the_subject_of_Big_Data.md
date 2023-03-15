# MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture of MapReduce introduced in Hadoop 0.23  .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, which is a framework for resource management and scheduling in Hadoop clusters  .
- The main idea of MRv2 is to separate the two major functions of the JobTracker in MRv1, which are resource management and job scheduling/monitoring, into separate daemons .
- The new components of MRv2 are:
  - ResourceManager: a global daemon that manages the allocation of resources (such as memory and CPU) to applications across the cluster  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager and coordinates the execution of tasks across the cluster  .
  - NodeManager: a per-node daemon that monitors the resource usage of containers and reports to the ResourceManager  .
  - Container: a unit of resource allocation that can run a task or an ApplicationMaster  .
- The advantages of MRv2 over MRv1 are:
  - Increased scalability: the ResourceManager can handle more nodes and applications than the JobTracker .
  - Improved cluster utilization: the ResourceManager can dynamically allocate resources to applications based on their needs and priorities .
  - Support for non-MR jobs: the ApplicationMaster can run any type of task, not only MapReduce, such as Spark, Tez, or Storm  .
  - Backward compatibility: the MRv2 can run MRv1 applications without any changes.