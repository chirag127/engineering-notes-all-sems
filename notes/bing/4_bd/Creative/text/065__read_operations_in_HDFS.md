#### Read operations in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store the actual data blocks of the files.
- To read a file from HDFS, a client application first contacts the NameNode and obtains the list of DataNodes that store the replicas of the blocks of the file.
- The client then contacts one of the DataNodes directly and requests the transfer of the desired block. The DataNode sends the block to the client as a stream of bytes over a TCP connection.
- The client reads the data from the stream and verifies the checksum of the block. If the checksum matches, the client is done with the block. If the checksum does not match, the client reports the error to the NameNode and tries to read the block from another DataNode that has a replica of the same block.
- The client repeats this process until it has read all the blocks of the file. The client can also read the file in parallel from multiple DataNodes to improve the read performance.