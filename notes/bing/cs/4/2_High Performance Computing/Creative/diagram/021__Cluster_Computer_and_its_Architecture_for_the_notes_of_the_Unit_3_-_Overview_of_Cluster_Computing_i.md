A cluster computer is a set of connected computers that work together as a single system. A cluster computer consists of two types of nodes: a head node and one or more compute nodes. The head node is responsible for managing the cluster, coordinating the load sharing, detecting node failures, and scheduling tasks. The compute nodes are the ones that perform the actual computations, such as running applications or processing data. A cluster computer also requires a high-speed interconnect network to communicate between the nodes and a shared storage system to store data.

The following ASCII diagram illustrates the basic architecture of a cluster computer:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Head Node     |      |   Compute Node  |      |   Compute Node  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Cluster       |      |   Cluster       |      |   Cluster       |
|   Management    |      |   Management    |      |   Management    |
|   Software      |      |   Software      |      |   Software      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Operating     |      |   Operating     |      |   Operating     |
|   System        |      |   System        |      |   System        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Hardware      |      |   Hardware      |      |   Hardware      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                     |                      |
       |                     |                      |
       +---------------------+----------------------+
                            |
                            |
                            |
                        +---+---+
                        |       |
                        |  LAN  |
                        |       |
                        +---+---+
                            |
                            |
                            |
                        +---+---+
                        |       |
                        |  SAN  |
                        |       |
                        +---+---+
```

LAN: Local Area Network
SAN: Storage Area Network