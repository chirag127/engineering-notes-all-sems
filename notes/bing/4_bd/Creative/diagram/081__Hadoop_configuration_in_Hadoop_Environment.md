#### Hadoop configuration in Hadoop Environment

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and Yet Another Resource Negotiator (YARN).

HDFS is a distributed file system that provides high-throughput access to data stored on the cluster nodes. HDFS splits the data into blocks and replicates them across multiple nodes for fault tolerance. HDFS also maintains the metadata of the files, such as the location of the blocks, the size of the files, and the permissions.

YARN is a resource management system that allocates resources (such as CPU and memory) to the applications running on the cluster. YARN also schedules the execution of the tasks and monitors their progress. YARN supports various types of applications, such as MapReduce, Spark, Hive, and Pig.

The following diagram illustrates the basic architecture of a Hadoop cluster:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NameNode     |    | SecondaryNameNode |  |    ResourceManager   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    DataNode     |    |    DataNode     |    |    DataNode     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    NodeManager  |    |    NodeManager  |    |    NodeManager  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The NameNode is the master node that manages the namespace and the metadata of the files stored on HDFS. It also coordinates the replication and the recovery of the blocks. The NameNode communicates with the DataNodes, which are the slave nodes that store the actual data blocks. The NameNode also communicates with the clients, which are the applications that read and write data to HDFS.

The SecondaryNameNode is a helper node that periodically merges the edits log and the fsimage file of the NameNode. It also acts as a backup for the NameNode in case of failure.

The ResourceManager is the master node that manages the resources and the applications running on the cluster. It consists of two main components: the Scheduler and the ApplicationsManager. The Scheduler allocates resources to the applications based on various criteria, such as capacity, fairness, and priority. The ApplicationsManager accepts the application submissions, negotiates the first container for the application, and monitors the application status.

The NodeManager is the slave node that monitors the resource usage and the health of the node. It also communicates with the ResourceManager and the ApplicationMaster. The ApplicationMaster is the process that runs on a container and coordinates the execution of the tasks for a specific application. It requests resources from the ResourceManager and launches containers on the NodeManager. It also reports the progress and the status of the application to the ResourceManager and the client.