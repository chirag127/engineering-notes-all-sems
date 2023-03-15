# Data Replication in HDFS

- Data replication is the process of storing multiple copies of data across different nodes in a distributed system.
- In HDFS, data is automatically replicated to ensure high availability and fault tolerance.
- The default replication factor in HDFS is 3, meaning that each block of data is stored on 3 different nodes.
- The replication factor can be configured by the user to meet the specific needs of their data and use case.
- When a block of data is written to HDFS, the first copy is stored on the local node, and the other copies are stored on other nodes in the same rack or a different rack.
- The NameNode is responsible for managing the replication of data blocks and ensuring that the desired replication factor is maintained.
- If a node fails or a block becomes unavailable, the NameNode will initiate the replication of the missing block to another node to restore the desired replication factor.
- Data replication in HDFS helps to ensure data durability and availability, even in the face of hardware failures or network outages.