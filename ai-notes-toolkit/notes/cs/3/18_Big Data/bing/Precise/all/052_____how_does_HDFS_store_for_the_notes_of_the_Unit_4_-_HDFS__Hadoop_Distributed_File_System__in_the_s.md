### HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to store large data sets across multiple machines. Here are some key points on how HDFS stores data:

1. HDFS divides files into blocks and stores each block on a DataNode .
2. Multiple DataNodes are linked to the master node in the cluster, the NameNode .
3. The master node distributes replicas of these data blocks across the cluster .
4. The NameNode also instructs the user where to locate wanted information .
5. HDFS stores data in a distributed manner, dividing the data into small pieces and storing it on different DataNodes in the cluster .
6. HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes .
7. HDFS stores data across commodity hardware, providing economical storage for big data .
8. HDFS follows the Write-Once-Read-Many-Times pattern for efficient data processing .
