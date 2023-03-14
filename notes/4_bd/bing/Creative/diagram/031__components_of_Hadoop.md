Hadoop is a framework that uses distributed storage and parallel processing to store and manage big data. It consists of three core components: HDFS, MapReduce, and YARN. HDFS is the storage unit that distributes data across multiple nodes in a cluster. MapReduce is the processing unit that applies a map function and a reduce function to the data in parallel. YARN is the resource management unit that allocates and schedules resources for different applications running on the cluster.

The following diagram illustrates the basic architecture of a Hadoop cluster using ASCII art:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Master      |    |    Master      |    |    Master      |
|    Node        |    |    Node        |    |    Node        |
|                |    |                |    |                |
|  NameNode      |    |  ResourceManager|    |  JobHistory    |
|                |    |                |    |  Server        |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
       |                     |                      |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Slave       |    |    Slave       |    |    Slave       |
|    Node        |    |    Node        |    |    Node        |
|                |    |                |    |                |
|  DataNode      |    |  DataNode      |    |  DataNode      |
|                |    |                |    |                |
|  NodeManager   |    |  NodeManager   |    |  NodeManager   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The diagram shows that there are three types of master nodes: NameNode, ResourceManager, and JobHistory Server. The NameNode manages the metadata of the files stored in HDFS and coordinates the data access among the slave nodes. The ResourceManager manages the resources available in the cluster and assigns tasks to the slave nodes. The JobHistory Server records the history of the jobs submitted to the cluster and provides a web interface for monitoring and debugging.

The diagram also shows that there are three types of slave nodes: DataNode, NodeManager, and ApplicationMaster. The DataNode stores the actual data blocks in HDFS and communicates with the NameNode. The NodeManager reports the status of the resources and tasks to the ResourceManager and executes the tasks assigned by the ResourceManager. The ApplicationMaster is a process that runs on a slave node and negotiates resources with the ResourceManager and coordinates the execution of the tasks for a specific application. Each application has its own ApplicationMaster.