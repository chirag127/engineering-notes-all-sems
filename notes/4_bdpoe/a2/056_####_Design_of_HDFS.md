 Here is the content in markdown format for the topic #### Design of HDFS:

#### Design of HDFS

HDFS has a master-slave architecture. The main components are:

- NameNode: The master node that manages the file system namespace and regulates access to files by clients. It maintains the filesystem tree and the metadata for all the files and directory.
- DataNodes: Slave nodes that store the blocks and serve read/write requests from the clients.

The key design points of HDFS are:

- HDFS splits files into large blocks (typically 128MB) and stores multiple replicas of them (default 3) across different DataNodes. This leads to streaming access of data and high throughput data read/write.
- The NameNode is a single point of failure. It maintains the file system namespace and manages the DataNodes. If it fails, the file system goes offline.
- DataNodes store the data blocks. If a DataNode fails, the blocks it holds become unavailable. The NameNode will notice the failure and mark the blocks as corrupt. New replicas will be created on other DataNodes.
- HDFS is highly fault-tolerant. It uses replication to tolerate faults. The large block size makes recovery fast as the system only needs to replicate a few large blocks to recover instead of thousands of small blocks.
- The Master (NameNode) and Slave (DataNodes) architecture supports horizontal scalability. More DataNodes can be added to increase storage capacity and more NameNodes can be added for load balancing and high availability.

Some mnemonics and learning tricks for HDFS design:

- Namenode = Master, Datanodes = Slaves
- Files split into large blocks (128MB) for streaming access
- Replication (3x) provides fault-tolerance
- Fault-tolerance via replication of blocks
- Scales horizontally by adding more Datanodes

The strengths of HDFS design are high throughput, streaming access, fault-tolerance, and horizontal scalability. The limitations are the single point of failure in the NameNode and less suitable for small file storage and frequent read/write of files.