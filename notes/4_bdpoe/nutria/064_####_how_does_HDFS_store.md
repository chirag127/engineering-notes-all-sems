
#### How does HDFS Store

HDFS (Hadoop Distributed File System) is a distributed file system that stores data across multiple nodes in a cluster. It is designed to facilitate rapid data processing and to handle large amounts of data. HDFS works by storing data in blocks, which are then distributed across the nodes in the cluster. Each node holds a copy of the data and is responsible for managing its own block.

The data is stored in a hierarchical structure, with directories and files. Each directory and file is assigned a unique identifier (UID) which is used to identify it. This UID is also used to track the data across the nodes in the cluster.

HDFS is designed to be fault tolerant, meaning that it can handle node failures without losing any data. This is achieved by replicating the data across multiple nodes. If one node fails, the data can still be accessed from the other nodes.

HDFS also allows for high availability, meaning that the data is always accessible. This is achieved by using a master-slave architecture, where the master node is responsible for managing the data and the slave nodes provide access to the data.

Mnemonics and learning tricks:

- Hadoop Distributed File System (HDFS): "HDFS - Handle Data Files Securely"
- UID: "Unique Identifier"
- Fault tolerance: "Fault Tolerance: Keeps Data Safe"
- High availability: "High Availability: Always Accessible"