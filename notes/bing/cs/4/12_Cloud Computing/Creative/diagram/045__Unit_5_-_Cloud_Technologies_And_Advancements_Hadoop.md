## Unit 5 - Cloud Technologies And Advancements Hadoop

Hadoop is a big data solution that provides a distributed computing framework for processing and analyzing large datasets using commodity hardware. Hadoop follows a master-slave architecture, where the master node coordinates the tasks and the slave nodes execute them. Hadoop consists of four main components: HDFS, MapReduce, YARN, and ZooKeeper.

HDFS is the Hadoop Distributed File System, which stores the data across multiple nodes in a cluster. HDFS splits the data into blocks and replicates them for fault tolerance. HDFS has two types of nodes: NameNode and DataNode. NameNode is the master node that manages the metadata of the files and blocks, such as their location, size, permissions, etc. DataNode is the slave node that stores the actual data blocks and communicates with the NameNode.

MapReduce is the programming model that allows parallel processing of data using two types of functions: map and reduce. Map function takes a set of key-value pairs as input and transforms them into another set of key-value pairs. Reduce function takes the output of the map function and aggregates them based on the key. MapReduce has two types of nodes: JobTracker and TaskTracker. JobTracker is the master node that assigns and monitors the map and reduce tasks. TaskTracker is the slave node that executes the tasks and reports to the JobTracker.

YARN is the Yet Another Resource Negotiator, which is responsible for resource management and scheduling in the Hadoop cluster. YARN has two types of nodes: ResourceManager and NodeManager. ResourceManager is the master node that allocates and manages the resources across the cluster. NodeManager is the slave node that reports the resource usage and availability to the ResourceManager and launches the containers for the tasks.

ZooKeeper is the service that ensures synchronization and coordination among the nodes in the Hadoop cluster. ZooKeeper maintains a hierarchical namespace of configuration data and provides atomic operations to update and access them. ZooKeeper has two types of nodes: Leader and Follower. Leader is the node that handles the client requests and coordinates the updates. Follower is the node that replicates the data from the leader and participates in the leader election.

The following diagram illustrates the basic architecture of Hadoop using ASCII characters:

```
+-----------------+  +-----------------+  +-----------------+
|    NameNode     |  |   JobTracker    |  |  ResourceManager |
+-----------------+  +-----------------+  +-----------------+
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
        |                    |                    |
+--------+--------+  +--------+--------+  +--------+--------+
| DataNode | TaskTracker | NodeManager |  | DataNode | TaskTracker | NodeManager |
+--------+--------+  +--------+--------+  +--------+--------+
| DataNode | TaskTracker | NodeManager |  | DataNode | TaskTracker | NodeManager |
+--------+--------+  +--------+--------+  +--------+--------+
| DataNode | TaskTracker | NodeManager |  | DataNode | TaskTracker | NodeManager |
+--------+--------+  +--------+--------+  +--------+--------+
| DataNode | TaskTracker | NodeManager |  | DataNode | TaskTracker | NodeManager |
+--------+--------+  +--------+--------+  +--------+--------+
```