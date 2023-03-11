### Design of HDFS

HDFS (Hadoop Distributed File System) is the primary storage system used by Hadoop. It is designed to store large files and data sets, and it is fault-tolerant and scalable. Here are some key design features of HDFS:

1. **Master-Slave Architecture:** HDFS follows a master-slave architecture in which a single NameNode acts as the master and multiple DataNodes act as slaves. The NameNode is responsible for managing the file system namespace, while the DataNodes are responsible for storing the actual data.

2. **Data Replication:** HDFS stores data by dividing it into blocks and replicating each block across multiple DataNodes. By default, each block is replicated three times, although this can be configured. Data replication ensures that if a DataNode fails, the data can still be accessed from other DataNodes.

3. **Data locality:** HDFS is designed to store and process data in a distributed manner. When a job is submitted to Hadoop, the job tracker will try to schedule tasks on the nodes that have a copy of the required data. This reduces network traffic and improves the performance of the job.

4. **Checksums:** To ensure data integrity, HDFS uses checksums to verify that the data stored on the DataNodes is the same as the data that was originally written. If a checksum mismatch is detected, HDFS will automatically request that the corrupt block be replicated from another DataNode.

5. **Block Size:** HDFS stores data in fixed-size blocks, typically 128MB or 256MB. This allows for efficient data storage and processing, as well as better data locality.

6. **Fault Tolerance:** HDFS is designed to be fault-tolerant. If a DataNode fails, the NameNode will detect the failure and replicate the data on other DataNodes. If the NameNode fails, a standby NameNode can take over.

7. **Scalability:** HDFS is designed to be highly scalable. It can handle petabytes of data and can easily add new DataNodes to the cluster to increase storage capacity.

Overall, the design of HDFS is focused on scalability, fault-tolerance, and data locality. These features make it an ideal storage system for big data applications.