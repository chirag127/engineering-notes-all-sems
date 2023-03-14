The following diagram illustrates the basic architecture of a distributed deadlock detection system using a global wait-for graph (WFG) approach:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Process P1    |      |   Process P2    |      |   Process P3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Resource R1   |      |   Resource R2   |      |   Resource R3   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |  ^                   |  ^                   |  ^
       |  |                   |  |                   |  |
       v  |                   v  |                   v  |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Local WFG1    |      |   Local WFG2    |      |   Local WFG3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |  ^                   |  ^                   |  ^
       |  |                   |  |                   |  |
       v  |                   v  |                   v  |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Deadlock      |<---->|   Deadlock      |<---->|   Deadlock      |
|   Detector 1    |      |   Detector 2    |      |   Detector 3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |  ^                   |  ^                   |  ^
       |  |                   |  |                   |  |
       v  |                   v  |                   v  |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Coordinator   |<---->|   Coordinator   |<---->|   Coordinator   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |  ^                   |  ^                   |  ^
       |  |                   |  |                   |  |
       v  |                   v  |                   v  |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Global WFG    |<---->|   Global WFG    |<---->|   Global WFG    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows how each process maintains a local wait-for graph (WFG) that represents the dependencies among the processes and resources in its node. Each process also has a deadlock detector that periodically sends its local WFG to a coordinator. The coordinator collects the local WFGs from all the processes and constructs a global WFG that represents the dependencies among all the processes and resources in the distributed system. The coordinator then checks the global WFG for cycles, which indicate the presence of a deadlock. If a deadlock is detected, the coordinator initiates a recovery procedure to resolve the deadlock.