#### How does HDFS store?

HDFS (Hadoop Distributed File System) is a distributed file system designed to store large files and datasets across multiple machines. Here are the key points on how HDFS stores data:

1. **Data is split into blocks:** HDFS splits files into fixed-size blocks, typically 128 MB or 256 MB. Each block is stored as a separate file on the local file system of a data node.

2. **Blocks are replicated:** To ensure data availability and fault tolerance, each block is replicated across multiple data nodes in the cluster. The default replication factor is three, meaning that each block is stored on three different data nodes.

3. **Block placement is strategic:** HDFS uses a strategic block placement policy to ensure that replicas of a block are stored on different racks and data nodes to minimize the risk of data loss.

4. **Metadata is stored separately:** HDFS stores file system metadata, such as file names, permissions, and directory structures, in a separate namespace. This metadata is managed by a dedicated NameNode, which maintains the metadata information in memory and on disk.

5. **Data is accessed via a client-server architecture:** Clients access data in HDFS through a client-server architecture. The HDFS client sends requests to the NameNode for metadata information and block locations, and then retrieves the data from the appropriate data nodes.

6. **Data is streamed:** HDFS is optimized for streaming large datasets rather than random access of small files. HDFS is most efficient when reading or writing large files in sequential or batch mode.

In summary, HDFS stores data by splitting it into fixed-size blocks, replicating the blocks across multiple data nodes, and strategically placing the replicas on different racks and nodes. The metadata is stored separately and managed by a dedicated NameNode, while data is accessed through a client-server architecture optimized for streaming large datasets.