#### Data replication in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that stores large-scale data across multiple nodes in a cluster.
- Data replication is a technique that creates multiple copies of the same data block and stores them on different nodes in the cluster, to ensure high availability and fault tolerance.
- Data replication in HDFS is controlled by two parameters: replication factor and block size.
- Replication factor is the number of copies of each data block that are stored in the cluster. The default value is 3, which means that each data block has three replicas on three different nodes.
- Block size is the size of each data block that is stored in the cluster. The default value is 128 MB, which means that each file is split into 128 MB chunks and stored as data blocks.
- Data replication in HDFS follows these steps:
  - When a client writes a file to HDFS, the client contacts the NameNode, which is the master node that maintains the metadata of the file system.
  - The NameNode allocates a unique block ID for each data block and returns a list of DataNodes, which are the worker nodes that store the data blocks, to the client.
  - The client contacts the first DataNode in the list and sends the data block to it. The first DataNode is called the pipeline leader.
  - The pipeline leader stores the data block locally and forwards it to the second DataNode in the list. The second DataNode stores the data block locally and forwards it to the third DataNode in the list. The third DataNode stores the data block locally and does not forward it further. This process is called the replication pipeline.
  - The DataNodes send acknowledgments to the client and the NameNode after storing the data blocks. The client waits for the acknowledgments from all the DataNodes before sending the next data block. The NameNode updates the metadata of the file system after receiving the acknowledgments from the DataNodes.
  - The client repeats the above steps until all the data blocks of the file are written to HDFS. The client closes the file after writing the last data block.
- Data replication in HDFS ensures that the data is available even if some nodes fail or become inaccessible. HDFS also performs periodic block scans and checksum validations to detect and repair corrupted data blocks. HDFS also balances the load of the cluster by moving data blocks from over-utilized nodes to under-utilized nodes.