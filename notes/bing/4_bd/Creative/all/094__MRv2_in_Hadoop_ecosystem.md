#### MRv2 in Hadoop ecosystem

- MRv2 stands for MapReduce version 2, which is an application framework that runs within YARN (Yet Another Resource Negotiator) in Hadoop 2.
- YARN is a resource management layer that separates the scheduling and resource allocation tasks from the data processing logic of MapReduce.
- MRv2 is backward compatible with the org.apache.hadoop.mapred APIs of Hadoop 1, which means that the compiled binaries of MapReduce applications can run on both Hadoop 1 and Hadoop 2 without any modification.
- MRv2 has several advantages over the original MapReduce framework, such as:
  - It allows multiple types of applications to run on Hadoop, not just MapReduce. For example, Spark, Storm, Tez, etc.
  - It improves the scalability and performance of MapReduce by using a more efficient scheduler and a distributed cache.
  - It supports high availability and security features such as Kerberos authentication and failover of ResourceManager and ApplicationMaster.
  - It enables finer-grained resource allocation and dynamic resource sharing among applications.
- MRv2 has a different architecture and components than the original MapReduce framework, such as:
  - ResourceManager: The central authority that manages the resources and applications in the cluster.
  - NodeManager: The agent that runs on each node and reports the resource usage and status to the ResourceManager.
  - ApplicationMaster: The process that coordinates the execution of a single application on the cluster. It requests resources from the ResourceManager and communicates with the NodeManagers to launch and monitor the containers.
  - Container: The unit of resource allocation and execution in YARN. It consists of a fixed amount of memory, CPU, disk, and network bandwidth. A container can run a MapReduce task or any other type of application logic.
  - Client: The process that submits the application to the ResourceManager and monitors its progress.

- A simple diagram of the MRv2 architecture is shown below:

```
+-----------------+             +-----------------+
|     Client      |             |   ResourceManager   |
+-----------------+             +-----------------+
        |                                |
        | submit application             |
        |------------------------------> |
        |                                |
        | application ID                 |
        |<------------------------------ |
        |                                |
        | monitor application            |
        |<-----------------------------> |
        |                                |
        |                                | allocate resources
        |                                |-------------------> +-----------------+
        |                                |                    |   NodeManager   |
        |                                |<-------------------+-----------------+
        |                                |                    | launch container
        |                                |                    |-----------------> +-----------------+
        |                                |                    |                  |   ApplicationMaster  |
        |                                |                    |                  +-----------------+
        |                                |                    |                  | request resources
        |                                |                    |                  |-----------------> | 
        |                                |                    |                  |<----------------- |
        |                                |                    |                  | launch containers
        |                                |                    |<---------------- |-----------------> |
        |                                |                    |                  | monitor containers
        |                                |                    |<---------------- |<----------------> |
        |                                |                    |                  | finish application
        |                                |                    |<---------------- |-----------------> |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
        |                                |                    |                  |                  |
+-----------------+             +-----------------+      +-----------------+      +-----------------+
```