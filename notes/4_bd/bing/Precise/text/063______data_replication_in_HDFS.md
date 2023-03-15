#### Data replication in HDFS

- HDFS stands for Hadoop Distributed File System.
- It is designed to store and manage large amounts of data across multiple machines.
- One of the key features of HDFS is data replication.
- Data replication refers to the process of storing multiple copies of the same data on different machines.
- This is done to ensure data availability and reliability.
- In HDFS, data is automatically replicated across multiple machines.
- The default replication factor is 3, meaning that 3 copies of the data are stored on different machines.
- The replication factor can be configured by the user.
- When a file is uploaded to HDFS, it is split into blocks and each block is replicated across multiple machines.
- If one machine fails, the data can still be accessed from the other machines.
- Data replication in HDFS helps to ensure that data is always available and can be accessed quickly, even in the event of a machine failure.