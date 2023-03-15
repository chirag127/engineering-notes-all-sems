#### How does HDFS store

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets across multiple machines. It is designed to be fault-tolerant and scalable.

1. HDFS stores data in blocks, with a default block size of 128 MB. Each block is replicated across multiple DataNodes for fault tolerance.
2. When a file is uploaded to HDFS, it is split into blocks and distributed across the DataNodes in the cluster.
3. The NameNode is responsible for managing the file system namespace and coordinating access to the data. It maintains the metadata for the files and directories in the file system, including the mapping of blocks to DataNodes.
4. When a client wants to read a file, it contacts the NameNode to determine the location of the blocks that make up the file. The client then reads the data directly from the DataNodes.
5. When a client wants to write a file, it contacts the NameNode to determine the location of the DataNodes where the blocks should be written. The client then writes the data directly to the DataNodes.
6. Data is written to the DataNodes in a pipeline, with the first DataNode in the pipeline writing the data to its local storage and forwarding it to the next DataNode in the pipeline.
7. The replication factor, which determines the number of replicas of each block, is configurable. The default replication factor is 3, meaning that each block is stored on 3 DataNodes.
8. HDFS uses a rack-aware replica placement policy to improve data reliability and network bandwidth utilization. This policy ensures that replicas of a block are stored on different racks, so that a single rack failure does not result in data loss.
9. HDFS also supports erasure coding, which can provide the same level of data durability as replication with less storage overhead.

A mnemonic to remember the key components of HDFS is **"Hadoop's DataNodes Form Storage"**. This can help you remember that HDFS stores data in blocks across multiple DataNodes, with the NameNode managing the file system namespace and coordinating access to the data.