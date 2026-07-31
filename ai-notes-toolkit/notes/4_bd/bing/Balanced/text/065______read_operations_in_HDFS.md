#### Read operations in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store the actual data blocks of the files.
- To read a file from HDFS, a client application first contacts the NameNode and obtains the list of DataNodes that store the replicas of the blocks of the file.
- The client then contacts one of the DataNodes directly and requests the transfer of the desired block. The DataNode sends the block to the client as a stream of bytes over a TCP connection.
- The client can read the block from the stream and verify its checksum. If the checksum does not match, the client can request the same block from another DataNode that has a replica of that block.
- The client repeats this process until it has read all the blocks of the file. The client can also read the blocks in parallel from multiple DataNodes to improve the read performance.
- HDFS supports both sequential and random access to files. Sequential access is more efficient as it can take advantage of the locality of the blocks. Random access requires the client to seek to the desired position in the file, which may involve contacting the NameNode multiple times to locate the blocks.