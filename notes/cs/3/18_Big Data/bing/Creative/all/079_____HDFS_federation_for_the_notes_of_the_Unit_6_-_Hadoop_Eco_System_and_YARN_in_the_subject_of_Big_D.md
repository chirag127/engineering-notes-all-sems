# HDFS Federation

HDFS Federation is a feature of Hadoop 2.x that allows the HDFS architecture to scale horizontally by supporting multiple NameNodes/namespaces in a single cluster. Each NameNode manages a separate namespace volume, which consists of a metadata directory on the local file system, a block pool containing all the blocks for the files in the namespace, and a set of DataNodes that store the blocks. The DataNodes are shared among the NameNodes and can store blocks from multiple namespaces. The NameNodes do not communicate with each other and operate independently. The clients can access any namespace by specifying the NameNode address in the URI.

Some of the benefits of HDFS Federation are:

- It overcomes the limitations of a single NameNode, such as the memory requirement, the throughput, and the single point of failure.
- It isolates the namespaces from each other, which improves the availability and security of the cluster.
- It allows the namespaces to have different configurations and policies, such as replication factor, block size, and encryption.
- It enables the cluster to grow incrementally by adding more NameNodes and DataNodes as needed.

The architecture of HDFS Federation is shown in the following diagram:

![HDFS Federation Architecture](https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/HDFS-Federation-Architecture.png)

Some of the key components and concepts of HDFS Federation are:

- Namespace: A logical grouping of files and directories that are managed by a NameNode. A namespace has a unique identifier and a URI scheme. For example, hdfs://nn1/ and hdfs://nn2/ are two different namespaces.
- Block pool: A set of blocks that belong to a namespace. A block pool has a unique identifier and is stored in a subdirectory on the DataNodes. For example, BP-1234 and BP-5678 are two different block pools.
- Namespace volume: A self-contained unit of management that consists of a namespace and its corresponding block pool. A namespace volume is created by formatting a NameNode with a namespace ID and a block pool ID. A namespace volume can be upgraded, deleted, or added independently.
- Federation configuration: The configuration of the cluster that specifies the NameNodes, their namespaces, and their RPC addresses. The configuration is stored in a file called hdfs-site.xml on each node of the cluster. The configuration can be changed dynamically by using the hdfs dfsadmin command.