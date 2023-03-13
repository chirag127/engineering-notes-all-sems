Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of several components that work together to achieve this goal. The main components of Hadoop are:

- Hadoop Distributed File System (HDFS): This is the storage layer of Hadoop that stores data across multiple nodes in a cluster. It splits the data into blocks and replicates them for fault tolerance. It also provides a namespace and a file system interface for accessing the data. HDFS has two types of nodes: NameNode and DataNode. NameNode is the master node that manages the metadata and the namespace of the file system. DataNode is the worker node that stores and serves the data blocks.
- Hadoop MapReduce: This is the processing layer of Hadoop that implements a programming model for parallel processing of data. It consists of two phases: Map and Reduce. Map phase takes the input data and transforms it into key-value pairs. Reduce phase takes the output of the Map phase and aggregates it based on the keys. MapReduce has two types of nodes: JobTracker and TaskTracker. JobTracker is the master node that coordinates the execution of the MapReduce jobs. TaskTracker is the worker node that runs the map and reduce tasks assigned by the JobTracker.
- Hadoop YARN: This is the resource management layer of Hadoop that allocates and manages the resources (CPU, memory, disk, network) for the applications running on the cluster. It consists of two components: ResourceManager and NodeManager. ResourceManager is the master node that oversees the resource allocation and scheduling of the applications. NodeManager is the worker node that monitors and reports the resource usage and status of the node.

The following diagram illustrates the basic architecture of Hadoop using ASCII characters:

```
    +----------------+            +----------------+
    |                |            |                |
    |    Client      |            |    Client      |
    |                |            |                |
    +----------------+            +----------------+
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   |                        |   |
          |   +------------------------+   |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          |                              |
          +------------------------------+
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |