Apache Hadoop is a software framework for storing and processing large datasets of varying sizes and formats across clusters of computers. It follows the master-slave architecture, where the master nodes assign tasks to the slave nodes and monitor their progress. Hadoop consists of two main components: HDFS and MapReduce.

HDFS stands for Hadoop Distributed File System, which is responsible for storing the data blocks across the cluster nodes. HDFS provides fault tolerance, high availability, scalability, and reliability. HDFS has two types of nodes: NameNode and DataNode. NameNode is the master node that manages the metadata of the file system, such as the location of the data blocks, the file permissions, the replication factor, etc. DataNode is the slave node that stores the actual data blocks and communicates with the NameNode.

MapReduce is the programming model for processing the data blocks in parallel. MapReduce has two types of nodes: JobTracker and TaskTracker. JobTracker is the master node that coordinates the execution of the MapReduce jobs, such as splitting the input data, assigning the map and reduce tasks, monitoring the task status, etc. TaskTracker is the slave node that runs the map and reduce tasks on the data blocks and reports to the JobTracker.

The following diagram illustrates the basic architecture of Apache Hadoop:

```
+-----------------+     +-----------------+     +-----------------+
|     Client      |     |     Client      |     |     Client      |
+-----------------+     +-----------------+     +-----------------+
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
          |                     |                     |
          +---------------------+---------------------+
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
+-----------------+     +-----------------+     +-----------------+
|    NameNode      |     |    JobTracker    |     |    Secondary    |
| (Master of HDFS) |     | (Master of MR)   |     |    NameNode     |
+-----------------+     +-----------------+     +-----------------+
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
          +---------------------+---------------------+
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
+-----------------+     +-----------------+     +-----------------+
|    DataNode      |     |    DataNode      |     |    DataNode     |
| (Slave of HDFS)  |     | (Slave of HDFS)  |     | (Slave of HDFS) |
+-----------------+     +-----------------+     +-----------------+
|    TaskTracker   |     |    TaskTracker   |     |    TaskTracker  |
| (Slave of MR)    |     | (Slave of MR)    |     | (Slave of MR)   |
+-----------------+     +-----------------+     +-----------------+
```