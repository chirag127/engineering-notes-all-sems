
### File Sizes in HDFS

* HDFS stands for Hadoop Distributed File System and is a distributed file system designed for storing very large files with streaming data access.
* HDFS divides large files into blocks and stores them across multiple nodes in a cluster. The default block size is 128 MB, but it can be configured to be larger or smaller.
* HDFS stores each block as an independent file on a local file system. Each block is replicated to other nodes in the cluster for fault tolerance.
* The maximum size of a single HDFS file is limited to the amount of storage available in the cluster. The maximum number of files in a directory is limited to the number of blocks in the cluster.
* HDFS is designed for large files and streaming reads. It is not suitable for small files or random reads.
* HDFS is optimized for large files and streaming reads. It is not suitable for small files or random reads.
* HDFS is designed to be highly fault tolerant. It replicates blocks across multiple nodes and can tolerate the failure of a node without losing data.
* HDFS is optimized for streaming reads. It is not optimized for random reads.
* HDFS is designed to be highly scalable. It can scale to hundreds of nodes in a cluster and store petabytes of data.
* HDFS is designed to be highly secure. It provides authentication, authorization, and encryption of data at rest.
* HDFS is designed to be highly efficient. It provides data locality and data replication to reduce network traffic.
* HDFS is designed to be highly available. It can detect and recover from node failures without losing data.