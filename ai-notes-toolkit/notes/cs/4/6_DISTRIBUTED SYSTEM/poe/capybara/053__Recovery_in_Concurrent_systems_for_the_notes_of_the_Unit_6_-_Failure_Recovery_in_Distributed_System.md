### Recovery in Concurrent systems

In concurrent systems, failure recovery is a crucial aspect that needs to be taken care of. Following are some of the techniques used for recovery in concurrent systems:

- **Checkpointing** - Checkpointing is a process of periodically saving the state of the system to a stable storage. In case of a failure, the system can restart from the last checkpoint. There are two types of checkpointing: periodic checkpointing and demand-driven checkpointing.

- **Rollback** - In case of a failure, the system can rollback to the last checkpoint and execute the operations again to bring the system to its last consistent state. There are two types of rollback: forward recovery and backward recovery.

- **Replication** - Replication is a process of creating multiple copies of data or processes to ensure fault tolerance. If one replica fails, the system can switch to another replica.

- **Redundancy** - Redundancy is a technique of creating redundant resources to ensure fault tolerance. For example, having multiple network paths between nodes to ensure communication even if one path fails.

- **Recovery-oriented computing** - Recovery-oriented computing is a technique that emphasizes on designing systems that can quickly recover from failures. It includes techniques such as self-healing and dynamic reconfiguration.

In conclusion, recovery in concurrent systems is a critical aspect that needs to be taken care of to ensure the fault-tolerance of the system. The techniques mentioned above can be used to design robust systems that can quickly recover from failures.