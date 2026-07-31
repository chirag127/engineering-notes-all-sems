 Here is the content in markdown format without any emojis or external links:

### Cluster Specification

1. Nodes: Master node and Slave/Worker nodes.
- Master node: Name node, Secondary name node, Job tracker.
- Slave/Worker nodes: Data nodes and Task trackers.

2. Name node: Maintains the file system namespace and regulates access to files by clients. It controls the file system metadata.

3. Data nodes: Stores the blocks for the files in HDFS. It's a slave node and there can be multiple data nodes in a cluster.

4. Job tracker: Schedules jobs and tracks resource utilization and progress. It allocates tasks to task trackers. Only one job tracker runs in a cluster.

5. Task trackers: Executes tasks assigned by the job tracker. It runs on the worker/slave nodes and there can be many task trackers per cluster.

6. HDFS: It is the primary storage system used by Hadoop. It stores data on the slave nodes as chunks/blocks. It provides scalability, fault tolerance and high throughput access to application data.

7. MapReduce: It is a programming model for processing/analysing large data sets. It consists of two major tasks - Map and Reduce which run on the worker nodes. MapReduce handles parallel processing of data on the cluster and fault tolerance.

The above points cover the key specifications regarding the Hadoop cluster nodes and core components. The master and slave nodes work together to handle the storage and processing of big data.