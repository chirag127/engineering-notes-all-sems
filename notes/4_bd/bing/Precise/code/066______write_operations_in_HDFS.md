#### Write Operations in HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets reliably and to stream those data sets at high bandwidth to user applications. Here are some key points to remember about write operations in HDFS:

1. **Data Replication:** HDFS replicates data blocks for fault tolerance. The default replication factor is 3, meaning that HDFS stores three copies of each data block on different nodes.

2. **Data Pipelining:** When a client writes data to HDFS, the data is first written to the local disk of the client machine. Then, the data is sent to the first DataNode in the pipeline. The first DataNode stores the data and forwards it to the second DataNode in the pipeline, and so on.

3. **Data Integrity:** HDFS uses checksums to ensure data integrity. When a client writes data to HDFS, it computes a checksum for each data block and sends the checksum to the DataNode along with the data. The DataNode verifies the checksum before storing the data.

4. **Write-once-read-many:** HDFS follows the write-once-read-many model. Once a file is created, written, and closed, it cannot be modified. However, it can be read any number of times.

5. **Atomicity:** HDFS supports atomicity for write operations. This means that a write operation is either completed successfully or not at all. If a write operation fails, the file system state is unchanged.

6. **Data Locality:** HDFS tries to place data blocks on the same node or rack as the client writing the data. This improves data locality and reduces network traffic.

7. **Data Coherency:** HDFS provides data coherency by ensuring that once a write operation is completed and the file is closed, all subsequent reads will see the new data.
