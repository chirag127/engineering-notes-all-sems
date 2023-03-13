## Unit 10 - Replication

Replication is a technique for distributing data and computation across multiple servers in a distributed system. Replication can improve availability, scalability, and consistency of the system, but also introduces challenges such as maintaining consistency, resolving conflicts, and managing network partitions.

A basic architecture of replication in a distributed system can be represented by the following diagram:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Client 1      |      |   Client 2      |      |   Client 3      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Server 1      |      |   Server 2      |      |   Server 3      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Database 1    |      |   Database 2    |      |   Database 3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows three clients, three servers, and three databases. Each client can send requests to any server, and each server can access any database. The databases are replicated, meaning that they store the same data and synchronize with each other. The servers are responsible for handling the requests from the clients, applying updates to the databases, and ensuring consistency among the replicas. The servers can use different replication strategies, such as primary-backup, quorum, or gossip, depending on the system requirements and trade-offs. The clients can also use different consistency models, such as strong, weak, or eventual, depending on the application semantics and performance needs.