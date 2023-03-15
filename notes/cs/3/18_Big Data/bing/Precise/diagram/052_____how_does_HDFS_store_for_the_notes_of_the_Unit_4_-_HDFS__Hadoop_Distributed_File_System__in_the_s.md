### HDFS (Hadoop Distributed File System) - Unit 4: How does HDFS store data?

HDFS stores data in a distributed manner by dividing files into blocks and storing each block on a DataNode. Multiple DataNodes are linked to the master node in the cluster, the NameNode. The master node distributes replicas of these data blocks across the cluster and instructs the user where to locate wanted information .

- HDFS divides files into blocks and stores each block on a DataNode .
- Multiple DataNodes are linked to the master node in the cluster, the NameNode .
- The master node distributes replicas of these data blocks across the cluster .
- The master node also instructs the user where to locate wanted information .
- HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes .
- HDFS stores data across commodity hardware, providing economical storage for big data .
- HDFS follows the Write-Once-Read-Many-Times pattern for efficient data processing .