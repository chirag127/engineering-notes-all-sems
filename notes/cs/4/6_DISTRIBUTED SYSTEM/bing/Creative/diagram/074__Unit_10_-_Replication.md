## Unit 10 - Replication

Replication is the practice of keeping several copies of data in different places in a distributed system. Replication can improve the availability, fault tolerance, and performance of the system, but also introduces challenges such as maintaining consistency, resolving conflicts, and managing network partitions.

There are different types of replication in distributed systems, such as active and passive replication, synchronous and asynchronous replication, and based on server model replication schemes. There are also different replication models, such as primary-backup, peer-to-peer, and quorum-based.

The following diagram illustrates the basic architecture of a primary-backup replication model in a distributed system:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    Client 1     |        |    Client 2     |        |    Client 3     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    Primary      |        |    Backup 1     |        |    Backup 2     |
|    Replica      |        |    Replica      |        |    Replica      |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       +------------------------+------------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       +------------------------+------------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    Storage 1    |        |    Storage 2    |        |    Storage 3    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

In this diagram, the clients send requests to the primary replica, which processes them and sends updates to the backup replicas. The backup replicas store the updates and send acknowledgments to the primary replica. The primary replica sends a response to the client after receiving the acknowledgments. The storage nodes store the data persistently and synchronize with the replicas. If the primary replica fails, one of the backup replicas takes over as the new primary. This model ensures strong consistency and fault tolerance, but also introduces latency and overhead.