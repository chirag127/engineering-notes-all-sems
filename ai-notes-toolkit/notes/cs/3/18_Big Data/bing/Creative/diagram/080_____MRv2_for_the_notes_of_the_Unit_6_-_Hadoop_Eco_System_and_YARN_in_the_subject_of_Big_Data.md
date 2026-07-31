### MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- MRv2 stands for MapReduce version 2, which is a new architecture for processing large-scale data sets in parallel using Hadoop framework  .
- MRv2 uses YARN, which stands for Yet Another Resource Negotiator, which is a resource management layer that allocates compute resources to different applications running on Hadoop cluster   .
- The main components of MRv2 are:
  - ResourceManager: a global daemon that manages the cluster resources and assigns them to different applications  .
  - NodeManager: a per-node daemon that monitors the resource usage and health of the node, and communicates with the ResourceManager  .
  - ApplicationMaster: a per-application daemon that negotiates resources with the ResourceManager and coordinates the execution of the application tasks on the NodeManagers  .
  - Container: a unit of resource allocation that consists of a certain amount of memory, CPU, disk, and network bandwidth   .
- The advantages of MRv2 over MRv1 are:
  - It increases the scalability of the cluster by decoupling the resource management and job scheduling/monitoring functions  .
  - It improves the cluster utilization by allowing multiple types of applications to run on the same cluster, such as Spark, Hive, Pig, etc   .
  - It supports dynamic resource allocation and fine-grained resource control for different applications and tasks   .
  - It enables high availability and fault tolerance by using ZooKeeper to elect a leader ResourceManager and by allowing ApplicationMasters to restart failed tasks  .