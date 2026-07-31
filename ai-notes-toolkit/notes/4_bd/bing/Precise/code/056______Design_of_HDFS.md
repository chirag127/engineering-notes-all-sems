#### Design of HDFS

HDFS is designed to store very large data sets reliably and to stream those data sets at high bandwidth to user applications. It is built to run on commodity hardware and is highly fault-tolerant. The architecture of HDFS is based on a master/slave model, where the master is the NameNode and the slaves are the DataNodes.

The NameNode manages the file system namespace and regulates access to files by clients. It also executes file system operations such as renaming, closing, and opening files and directories. The DataNodes are responsible for serving read and write requests from the file system's clients, and they also perform block creation, deletion, and replication upon instruction from the NameNode.

HDFS stores files as blocks, and the block size is configurable. Each block is stored on multiple DataNodes, and the number of replicas is also configurable. The NameNode determines the mapping of blocks to DataNodes, and it periodically receives a report from each DataNode about the blocks it is storing.

HDFS is designed to be accessed by a small number of very large files, rather than a large number of small files. It is optimized for streaming data access, and it is not suitable for low-latency data access. HDFS also provides interfaces for applications to move themselves closer to where the data is located, to reduce the amount of data that must be transferred over the network.