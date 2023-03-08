 Here is the content written in markdown format on the topic ## Unit 6 - Hadoop Eco System and YARN:

## Unit 6 - Hadoop Eco System and YARN

- Hadoop Eco System refers to the collection of various components and frameworks that are part of or work with Hadoop to solve big data problems. The core Hadoop components are Hadoop Common, Hadoop Distributed File System (HDFS) and Hadoop YARN.
- YARN (Yet Another Resource Negotiator) is the cluster resource management framework of Hadoop. It splits up the functionality of job scheduling and cluster resource management into separate daemons.
- The key components of YARN are:
 - ResourceManager (RM): Responsible for allocating resources to applications and scheduling applications. It has two main components: Scheduler and Applications Manager.
 - NodeManager (NM): Runs on each node in the cluster and is responsible for executing and monitoring tasks on that node. It periodically sends heartbeat messages to the RM.
 - ApplicationMaster (AM): Responsible for negotiating resources from RM and working with NM(s) to execute tasks.
- The key benefits of YARN over the traditional Hadoop MapReduce framework are:
 - Scalability: It can handle very large clusters with thousands of nodes efficiently.
 - Compatibility: It is compatible with the Hadoop ecosystem and can support more than just MapReduce applications like Spark, Hive, etc.
 - Multi-tenancy: It allows multiple applications to share cluster resources simultaneously.
 - Utilization: It improves resource utilization and performance through effective resource scheduling and isolation between applications.

[Further details, diagrams, examples, codes, advantages, disadvantages and applications can be added.]