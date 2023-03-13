## Unit 2 - Hadoop and Map Reduce

Hadoop and Map Reduce are two components of the Hadoop ecosystem that enable parallel processing of large data sets in a distributed manner. Hadoop consists of a distributed file system called HDFS, which stores the data across multiple nodes, and a resource management layer called YARN, which allocates the resources for the applications. Map Reduce is a programming model that divides the data processing into two phases: map and reduce. The map phase applies a user-defined function to each input record and produces intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output.

The following diagram illustrates the basic architecture of a Hadoop and Map Reduce system using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Client      |     |    Client      |     |    Client      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Master      |     |    Master      |     |    Master      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Slave       |     |    Slave       |     |    Slave       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Slave       |     |    Slave       |     |    Slave       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The master nodes are responsible for coordinating the tasks and managing the metadata. The slave nodes are responsible for executing the tasks and storing the data. The client nodes are the ones that submit the applications and interact with the system. The master nodes include:

- NameNode: The master node of HDFS, which maintains the namespace and the block locations of the files.
- Secondary NameNode: A backup node of HDFS, which periodically merges the namespace image and the edit log of the NameNode.
- ResourceManager: The master node of YARN, which allocates the resources and schedules the applications across the cluster.
- JobTracker: The master node of Map Reduce, which assigns the map and reduce tasks to the slave nodes and monitors their progress.

The slave nodes include:

- DataNode: The slave node of HDFS, which stores the data blocks and communicates with the NameNode.
- NodeManager: The slave