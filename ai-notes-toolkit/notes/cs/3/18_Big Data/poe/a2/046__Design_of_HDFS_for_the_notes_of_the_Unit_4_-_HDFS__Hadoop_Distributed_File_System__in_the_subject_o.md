 Here is the content in Markdown format with formal tone and without emojis or external links:

### Design of HDFS for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

1. HDFS is designed for storing very large files with streaming access patterns, running on clusters of commodity hardware.

2. HDFS provides high throughput access to application data and is suitable for applications that have large data sets.

3. HDFS is designed to be fault-tolerant, designed with hardware failures in mind by replicating data across multiple machines.

4. The HDFS architecture consists of a NameNode (master server) and DataNodes (slave servers). The NameNode manages the file system namespace and regulates access to files by clients.

5. DataNodes store data in files as blocks within the cluster and they serve read/write requests from clients.

6. Data is stored in files, and files are split into one or more blocks. Blocks are large by default (128MB) for efficiency.

7. The replicas of a block are stored on different DataNodes for fault tolerance. The default replication value is 3, providing strong data reliability.

8. HDFS follows the Master/Slave architecture. The NameNode is the master server that manages the file system namespace and regulates access to files by clients.

The content summarizes some of the key design points of HDFS like fault tolerance, master-slave architecture, usage of commodity hardware, streaming access of large files, etc. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.