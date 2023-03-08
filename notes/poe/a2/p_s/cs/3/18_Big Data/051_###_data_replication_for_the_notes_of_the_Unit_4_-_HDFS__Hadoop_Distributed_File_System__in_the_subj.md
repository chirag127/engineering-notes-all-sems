 Here is the content in markdown format for the topic ### Data Replication for the notes of Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

Data Replication in HDFS:

- HDFS replicates data for fault tolerance. The replication factor (number of copies of a block) is configurable and typically 3 is used.
- The copies of a block are placed on different racks and nodes for high availability in case of hardware failures or network issues.
- The master node (NameNode) tracks the location of block replicas and their health. It re-replicates or de-replicates data based on the cluster conditions to ensure sufficient number of healthy replicas of data.
- Advantages: Fault tolerance, high availability, scalability (data closer to nodes needing it), reliability.
- Disadvantages: Higher storage space required, more network bandwidth used for replication leading to slightly lower performance.
- Use cases: When high availability and fault tolerance crucial like in enterprise systems. Replication provides data redundancy and availability even with hardware failures or network issues.

Here is an ASCII diagram showing replication of a block (data unit in HDFS) across a cluster with racks and nodes:

    Rack 1     Rack 2
    /  \       /  \
   /    \     /    \
  Node 1 Node 2 Node 3 Node 4

Block A (primary copy) -> Node 1
Block A (replica 1) -> Node 2
Block A (replica 2) -> Node 3

Applications can specify replication factor and HDFS ensures required replicas are maintained. Replication provides reliability, availability and scalability key for big data systems.