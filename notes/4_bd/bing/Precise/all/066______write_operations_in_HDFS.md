#### Write operations in HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets reliably and to stream those data sets at high bandwidth to user applications.

1. **Write Process**: When a client wants to write a file to HDFS, it first contacts the NameNode. The NameNode responds with the identities of the DataNodes that will store replicas of the first block of the file. The client then writes the data to the first DataNode, which in turn forwards the data to the next DataNode in the pipeline. Once all replicas of the first block are written, the client requests new DataNodes to write the next block of the file, and the process repeats until the file is written completely.

2. **Data Replication**: HDFS replicates each block of data to multiple DataNodes to ensure data reliability and availability. The default replication factor is 3, meaning that each block is stored on 3 different DataNodes. The replication factor can be configured per file or per directory.

3. **Data Integrity**: HDFS uses checksums to ensure the integrity of data stored on DataNodes. When a client writes data to HDFS, it computes a checksum for each block of data and sends the checksum to the DataNode along with the data. The DataNode stores the checksum with the data and verifies the checksum when it reads the data.

4. **Data Durability**: HDFS ensures data durability by writing data to multiple DataNodes and by storing the metadata on the NameNode. In case of a DataNode failure, the NameNode can reconstruct the lost data from the other replicas. In case of a NameNode failure, a secondary NameNode can take over the role of the primary NameNode.

5. **Write Performance**: HDFS is optimized for write-once-read-many workloads. It provides high write throughput by writing data to multiple DataNodes in parallel. However, the write performance may be limited by the network bandwidth and the disk I/O speed of the DataNodes.

6. **Atomicity**: HDFS provides atomicity for write operations by using a write-ahead log on the NameNode. When a client writes data to HDFS, the NameNode first logs the write operation to its edit log. Once the edit log is flushed to disk, the NameNode acknowledges the write operation to the client. In case of a NameNode failure, the edit log can be used to recover the file system metadata.

7. **Consistency**: HDFS provides strong consistency for write operations. Once a write operation is acknowledged by the NameNode, the data is guaranteed to be visible to all readers. However, HDFS does not provide immediate consistency for read operations. It may take some time for the data to be propagated to all replicas, and a reader may see stale data during this time.

In summary, HDFS provides reliable, scalable, and high-performance storage for large data sets. It ensures data integrity, durability, and availability through data replication, checksums, and write-ahead logging. It provides strong consistency for write operations and eventual consistency for read operations. Its write performance is optimized for write-once-read-many workloads.