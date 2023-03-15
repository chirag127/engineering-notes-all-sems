### Data Replication in HDFS (Hadoop Distributed File System)

- Data replication is the process of storing data in more than one location to improve data availability and reliability.
- In HDFS, data is automatically replicated across multiple DataNodes to ensure data durability and fault tolerance.
- The default replication factor in HDFS is 3, meaning that each block of data is stored on 3 different DataNodes.
- The replication factor can be configured by the user to meet the specific needs of their data and use case.
- When a DataNode fails, the NameNode automatically initiates the replication of the missing blocks to other DataNodes to maintain the desired replication factor.
- Data replication in HDFS also improves data locality, allowing for faster data access and processing by reducing the need for data transfer across the network.
- HDFS uses a rack-aware replica placement policy to ensure that replicas are placed on different racks to improve data availability in the event of a rack failure.
