### HDFS (Hadoop Distributed File System) - Unit 4: How does HDFS store data?

- HDFS stores data in a distributed manner by dividing the data into small pieces and storing it on different DataNodes in the cluster.
- HDFS divides files into blocks and stores each block on a DataNode .
- Multiple DataNodes are linked to the master node in the cluster, the NameNode .
- The master node distributes replicas of these data blocks across the cluster.
- The master node also instructs the user where to locate wanted information.
- HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes.
- HDFS stores data across commodity hardware, providing economical storage for big data.
- HDFS follows the Write-Once-Read-Many-Times pattern for efficient data processing.
- The data for HDFS files will be stored in the directory specified in `dfs.datanode.data.dir`.