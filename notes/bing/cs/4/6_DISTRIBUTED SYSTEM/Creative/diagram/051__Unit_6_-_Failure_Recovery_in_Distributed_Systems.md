## Unit 6 - Failure Recovery in Distributed Systems

Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs. Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite faults. There are different types of failures that can affect distributed systems, such as node failures, network failures, media failures, and Byzantine failures. Each type of failure requires a different recovery strategy.

One of the common recovery strategies is checkpointing, which involves periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud service. Checkpointing can be done either globally, where all the components synchronize their checkpoints, or locally, where each component checkpoints independently. Checkpointing can reduce the amount of state loss and re-computation in case of a failure, but it also introduces overhead and complexity.

Another recovery strategy is replication, which involves creating and maintaining multiple copies of the system or its components across different nodes or locations. Replication can increase the availability and reliability of the system, as well as its performance and scalability. However, replication also poses challenges for consistency and coordination among the replicas, especially in the presence of network failures or Byzantine failures.

A third recovery strategy is logging, which involves recording the history of the system or its components to a stable storage, such as a disk or a cloud service. Logging can be done either eagerly, where each operation is logged before it is executed, or lazily, where operations are logged after they are executed. Logging can enable the system to recover from failures by replaying the logged operations, either forward or backward, to restore the state of the system or its components. Logging can also facilitate debugging and auditing of the system.

The following diagram illustrates the basic architecture of a distributed system with checkpointing, replication, and logging mechanisms:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Node 1       |     |    Node 2       |     |    Node 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Process 1    |     |    Process 2    |     |    Process 3    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Checkpoint 1 |     |    Checkpoint 2 |     |    Checkpoint 3 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Replica 1    |     |    Replica 2    |     |    Replica 3    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Log 1        |     |    Log 2        |     |    Log 3        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       |                   |                   |
       +-------------------+-------------------+
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                           |
+-----------------+
|                 |
|    Stable       |
|    Storage      |
|                 |
+-----------------+
```

In this diagram, each node represents a physical or virtual machine that hosts one or