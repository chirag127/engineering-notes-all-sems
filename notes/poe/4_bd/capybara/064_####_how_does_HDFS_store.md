#### How Does HDFS Store

HDFS (Hadoop Distributed File System) is a distributed file system designed to store large datasets across multiple commodity servers. It is an essential part of the Hadoop ecosystem, which is widely used for big data processing and storage.

Here are some important points to understand how HDFS stores data:

1. File Splitting: HDFS stores large files as blocks, which are typically 128 MB or 256 MB in size. When a file is uploaded to HDFS, it is automatically split into multiple blocks, and each block is stored on a different data node in the cluster. This allows HDFS to store large files efficiently and in a fault-tolerant manner.

2. Replication: HDFS replicates each block multiple times to ensure data reliability and availability. By default, each block is replicated three times, which means there are three copies of each block stored on different data nodes. This replication factor can be configured to suit different storage and reliability requirements.

3. NameNode and DataNodes: HDFS consists of two types of nodes: NameNode and DataNodes. The NameNode is responsible for managing the file system namespace, maintaining the metadata about the files and directories, and coordinating the access to the data. The DataNodes, on the other hand, are responsible for storing and serving the actual data blocks.

4. Rack Awareness: HDFS is designed to be rack-aware, which means it tries to store replicas of each block across different racks in the data center. This helps to avoid the risk of losing all replicas of a block in case of a rack failure. By default, HDFS stores one replica of each block on a different rack, and the remaining replicas on different nodes within the same rack.

5. Balancing: HDFS automatically balances the storage and the replication of data blocks across the data nodes in the cluster. This means that if a node becomes too full, HDFS will move some of the blocks to other nodes to maintain a balanced distribution of data.

6. Checksums: HDFS uses checksums to ensure data integrity. Each block is assigned a checksum when it is stored, and this checksum is verified every time the block is read. If the checksum does not match, HDFS automatically requests another replica of the block from a different data node.

7. Erasure Coding: HDFS also supports erasure coding, which is an alternative to replication for data reliability. Erasure coding uses mathematical algorithms to split each block into smaller fragments and generate additional fragments that can be used to reconstruct the original data in case of data loss. Erasure coding can reduce the storage overhead of replication while maintaining the same level of data reliability.

Overall, HDFS is a robust and scalable file system that can store and manage large datasets in a distributed and fault-tolerant manner. Understanding how HDFS stores data is essential for anyone working with big data processing and storage.