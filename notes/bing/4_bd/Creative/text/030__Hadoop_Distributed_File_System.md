#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a file system that provides scalable, reliable, and fault-tolerant storage for large-scale data processing applications.
- HDFS is designed to run on clusters of commodity hardware, and can store petabytes of data across thousands of nodes.
- HDFS follows a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store the actual data blocks.
- HDFS supports a write-once-read-many model, where files are split into fixed-size blocks (typically 128 MB) and replicated across multiple DataNodes for fault tolerance and high availability.
- HDFS provides a Java-based API for clients to interact with the file system, as well as a web-based interface and a command-line interface.
- HDFS supports several features, such as:
  - Rack awareness: HDFS can optimize the placement of data blocks based on the network topology of the cluster, and can tolerate rack failures by maintaining multiple replicas across different racks.
  - Snapshots: HDFS can create point-in-time copies of directories or files, which can be used for backup, disaster recovery, or testing purposes.
  - Federation: HDFS can scale horizontally by allowing multiple NameNodes to operate independently, each managing a separate namespace and a subset of DataNodes.
  - High Availability: HDFS can eliminate the single point of failure of the NameNode by using a pair of NameNodes in an active-standby configuration, and using a shared storage or a quorum journal manager to synchronize their states.
  - Erasure coding: HDFS can reduce the storage overhead of replication by using erasure coding, which splits data blocks into smaller fragments and encodes them with parity information, such that the original data can be recovered from a subset of the fragments.
  - Encryption: HDFS can encrypt data at rest and in transit, using keys managed by a key management server, and using transparent encryption zones to specify which directories or files should be encrypted.