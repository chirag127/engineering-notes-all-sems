The following is a possible ASCII diagram for system model and group communication for replication in distributed system.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Process P1     |    |  Process P2     |    |  Process P3     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Replica R1     |    |  Replica R2     |    |  Replica R3     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Client C1      |    |  Client C2      |    |  Client C3      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram illustrates the basic architecture of a system model and group communication for replication in distributed system. The system consists of three processes (P1, P2, P3), each hosting a replica (R1, R2, R3) of some data. The replicas are connected by a multicast communication channel, which allows them to exchange messages and synchronize their states. The system also has three clients (C1, C2, C3), each accessing one of the replicas. The clients can perform read and write operations on the data, which are propagated to the other replicas by the multicast channel. The system model and group communication for replication in distributed system aims to achieve consistency, availability, and fault tolerance among the replicas, while minimizing the communication and synchronization overheads.