### Anatomy of a Map Reduce job run

A Map Reduce job is a unit of work that consists of a map phase and a reduce phase, which operate on a distributed file system (DFS) such as Hadoop Distributed File System (HDFS). The map phase transforms the input data into intermediate key-value pairs, and the reduce phase aggregates the intermediate values for each key and produces the final output. A Map Reduce job run involves the following steps:

1. The client submits the job to the JobTracker, which is a daemon process that runs on the master node of the cluster. The JobTracker is responsible for scheduling and coordinating the execution of the job across the cluster. The client specifies the input and output locations, the mapper and reducer classes, the number of map and reduce tasks, and other configuration parameters.
2. The JobTracker splits the input data into fixed-size chunks called input splits, each of which is assigned to a map task. The number of map tasks is usually equal to the number of input splits, but it can be adjusted by the client. The input splits are stored in HDFS and can be accessed by any node in the cluster.
3. The JobTracker assigns the map tasks to the TaskTrackers, which are daemon processes that run on the worker nodes of the cluster. The TaskTrackers are responsible for running the map and reduce tasks and reporting their progress and status to the JobTracker. The JobTracker tries to assign the map tasks to the nodes that are closest to the data, to minimize the network traffic and improve the performance.
4. The TaskTracker launches a separate JVM process for each map task and runs the mapper class on the input split. The mapper reads the input data and applies a user-defined function to generate the intermediate key-value pairs. The mapper can also perform filtering, sorting, and aggregation operations on the data. The intermediate key-value pairs are buffered in memory and periodically spilled to the local disk, partitioned by a hash function based on the key.
5. The TaskTracker notifies the JobTracker about the completion of the map task and the location of the intermediate data on the local disk. The JobTracker keeps track of the map output locations for each reduce task.
6. The JobTracker assigns the reduce tasks to the TaskTrackers, based on the availability of resources and the load balancing. The number of reduce tasks is determined by the client and can be changed by the setNumReduceTasks() method. The reduce tasks are independent of the map tasks and can start before all the map tasks are finished.
7. The TaskTracker launches a separate JVM process for each reduce task and runs the reducer class. The reducer fetches the intermediate data from the local disks of the nodes where the map tasks ran, using HTTP requests. The reducer merges and sorts the intermediate data by the key and applies a user-defined function to aggregate the values for each key. The reducer can also perform filtering, sorting, and aggregation operations on the data. The reducer writes the final output to the output location in HDFS.
8. The TaskTracker notifies the JobTracker about the completion of the reduce task and the location of the output data in HDFS. The JobTracker keeps track of the output locations for each job.
9. The JobTracker marks the job as successful when all the map and reduce tasks are finished and the output data is written to HDFS. The JobTracker also cleans up the intermediate data from the local disks of the nodes. The client can access the output data from HDFS or copy it to a local file system.

The following diagram illustrates the anatomy of a Map Reduce job run:

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
       |                      |                      |      +----------------+
       |                      |                      |      |                |
       |                      |