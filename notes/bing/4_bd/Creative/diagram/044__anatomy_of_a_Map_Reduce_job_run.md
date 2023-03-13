A MapReduce job run consists of the following steps:

1. The client submits the job to the JobTracker, which is the master node that coordinates the execution of the job.
2. The JobTracker splits the input data into fixed-size chunks called input splits, and assigns a map task to each split. The input splits are stored in the Hadoop Distributed File System (HDFS), which is a distributed file system that replicates the data across multiple nodes for fault tolerance and high availability.
3. The map tasks read the input splits and apply a user-defined map function to each record. The map function transforms the input records into intermediate key-value pairs, which are written to a local disk on the same node where the map task is running.
4. The map tasks periodically report their progress and status to the JobTracker, which monitors the health and availability of the map tasks. If a map task fails or times out, the JobTracker can reassign the task to another node.
5. The JobTracker also partitions the intermediate key-value pairs into a fixed number of reduce tasks, based on a user-defined partitioning function. The partitioning function determines which reduce task is responsible for processing a given key.
6. The reduce tasks fetch the intermediate key-value pairs from the local disks of the map tasks, using a process called shuffle. The shuffle involves transferring data over the network, sorting and merging the data by key, and storing the data in the memory or disk of the reduce task node.
7. The reduce tasks apply a user-defined reduce function to each group of values that share the same key. The reduce function aggregates, filters, or transforms the values into a final output, which is written to the HDFS.
8. The JobTracker notifies the client when the job is completed, and the client can retrieve the output from the HDFS.

#### Anatomy of a MapReduce job run

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Client     |      |   JobTracker   |      |   TaskTracker  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |      +----------------+
       |                      |                      |      |                |
       |                      |                      |      |     HDFS      |
       |                      |                      |      |                |
       |                      |                      |      +----------------+
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |      +----------------+
       |                      |                      |             |      |                |
       |                      |                      |             |      |     Output     |
       |                      |                      |             |      |                |
       |                      |                      |             |      +----------------+
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |
       |                      |                      |             |      +----------------+
       |                      |                      |             |      |                |
       |                      |                      |             |      |   Reduce Task  |
       |                      |                      |             |      |                |
       |                      |                      |             |      +----------------+
       |                      |                      |             |             ^
       |                      |                      |             |             |
       |                      |                      |             |             |
       |                      |                      |             |             |
       |                      |                      |