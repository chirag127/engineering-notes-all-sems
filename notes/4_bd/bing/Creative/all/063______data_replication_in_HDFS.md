#### Data replication in HDFS

- Data replication is the process of copying data from one HDFS service to another, or to and from other storage systems such as Amazon S3 or Microsoft ADLS.
- Data replication is useful for fault tolerance, disaster recovery, backup, and data migration.
- HDFS stores each file as a sequence of blocks, which are replicated across different nodes in the cluster.
- The default replication factor is 3, which means each block is copied to 3 nodes. The replication factor can be configured per file or per directory.
- The NameNode is responsible for managing the replication of blocks. It keeps track of the location and health of each block and node.
- The NameNode also balances the load of the cluster by moving blocks from over-utilized nodes to under-utilized nodes.
- The replication process is as follows:
  - When a client writes a file to HDFS, it splits the file into blocks and sends them to the DataNodes.
  - The client also sends the block locations to the NameNode, which updates its metadata.
  - The NameNode assigns a replication pipeline for each block, which is a list of DataNodes that will store the replicas of the block.
  - The first DataNode in the pipeline receives the block from the client and writes it to its local disk.
  - The first DataNode then forwards the block to the second DataNode in the pipeline, which writes it to its local disk and forwards it to the third DataNode, and so on.
  - The last DataNode in the pipeline sends an acknowledgment to the previous DataNode, which sends an acknowledgment to the previous DataNode, and so on, until the first DataNode receives the final acknowledgment.
  - The first DataNode then sends a confirmation to the client, which sends a confirmation to the NameNode, which updates its metadata.
  - The replication process is repeated for each block of the file until the file is fully replicated.
- A simple mnemonic to remember the replication process is: **C**lient writes to **F**irst DataNode, which writes to **S**econd DataNode, which writes to **T**hird DataNode, and so on. **C**onfirmations are sent back from **L**ast DataNode to **F**irst DataNode, and then to **C**lient and **N**ameNode. **C**lient, **F**irst, **S**econd, **T**hird, **L**ast, **C**onfirm, **N**ameNode. **CFSTLCN**.
- A simple ASCII diagram of the replication process is:

```
  Client
    |
    | Block 1
    V
  DataNode 1 ----> DataNode 2 ----> DataNode 3
    ^                  ^                  ^
    |                  |                  |
    | Block 1 ACK      | Block 1 ACK      | Block 1 ACK
    |                  |                  |
    |                  |                  |
  NameNode <-----------+------------------+
    ^
    |
    | Block 1 confirmation
    |
    |
  Client
```