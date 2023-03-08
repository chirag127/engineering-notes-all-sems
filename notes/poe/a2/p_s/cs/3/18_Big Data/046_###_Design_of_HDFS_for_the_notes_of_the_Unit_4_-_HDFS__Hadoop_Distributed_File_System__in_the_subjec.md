 Here is the content in markdown format for the topic ### Design of HDFS for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

### Design of HDFS

- HDFS has a master-slave architecture. The HDFS cluster consists of a single NameNode, and multiple DataNodes.
- The NameNode is the master server that manages the file system namespace and regulates access to files by clients.
- The DataNodes are the slave nodes that store the blocks and serve read/write requests from the clients.
- The files in HDFS are broken down into block-sized chunks, typically 64MB or 128MB. The blocks of a file are replicated for fault tolerance. The replication factor can be 3 or more.
- The NameNode maintains the file system namespace and the locations of the blocks. It keeps the mapping of files to blocks. When the client wants to read a file, the NameNode provides the location of the blocks and the client contacts the DataNodes directly to read the blocks.
- The DataNodes send periodic reports to the NameNode with the list of blocks on them. The NameNode uses these reports to keep its metadata up-to-date. The NameNode is a single point of failure for HDFS. So it is important to configure a secondary NameNode that can take over in case the primary NameNode fails.
- HDFS provides streaming access to large files. It is designed more for large files that are sequentially accessed rather than random access. The emphasis is on high throughput of data rather than low latency of data access. Hence, HDFS is more suitable for batch-processing workloads rather than real-time queries.
- Advantages: Fault tolerance, Scalability, Economical, Suitable for large datasets
- Disadvantages: Not suitable for low latency data access, Does not support random writes, Not suitable for a large number of small files

[Include diagrams/codes/tables/examples/applications as relevant and helpful]