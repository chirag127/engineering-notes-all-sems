Deadlock prevention is a technique to avoid the occurrence of deadlocks in a distributed system by imposing some constraints on the resource allocation policies. There are two main methods of deadlock prevention in a distributed system: ordered request and collective request.

Ordered request is a method where each resource type is assigned a certain level and a process can only request resources in increasing order of levels. This prevents circular wait condition, which is one of the necessary conditions for deadlock.

Collective request is a method where a process must request all the resources it needs at once, before starting its execution. This prevents hold and wait condition, which is another necessary condition for deadlock.

The following diagram illustrates the basic architecture of a distributed system with deadlock prevention:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Process P1     |      |  Process P2     |      |  Process P3     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Resource R1    |      |  Resource R2    |      |  Resource R3    |
|  Level 1        |      |  Level 2        |      |  Level 3        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

In this diagram, there are three processes and three resources in the distributed system. Each resource has a level assigned to it. For example, resource R1 has level 1, resource R2 has level 2, and resource R3 has level 3. The processes can request resources only in increasing order of levels. For example, process P1 can request R1, then R2, then R3, but not R3, then R1, then R2. This ensures that there is no circular wait among the processes. Alternatively, the processes can request all the resources they need at once, before starting their execution. For example, process P2 can request R1 and R3 together, but not R1, then R3, then R1. This ensures that there is no hold and wait among the processes. By using either of these methods, the distributed system can prevent deadlocks from occurring.