### Unit 3 - Distributed Deadlock Detection

#### Detection & Resolution

1. **Detection**: In a distributed system, deadlock detection is more complex than in a centralized system. This is because the resources and processes are distributed across multiple nodes, and there is no global state or central coordinator. To detect deadlocks, a distributed algorithm is used, which involves communication between the nodes to gather information about resource allocation and process states.

2. **Resolution**: Once a deadlock is detected, it must be resolved to allow the system to continue functioning. There are several methods for resolving deadlocks in a distributed system, including:
    - **Preemption**: This involves taking a resource away from a process and giving it to another process to break the deadlock.
    - **Rollback**: This involves rolling back the state of one or more processes to a previous point in time to break the deadlock.
    - **Killing a process**: This involves killing one or more processes to break the deadlock. This is a more drastic approach and can result in lost work or data.

These are some of the key points to consider when studying distributed deadlock detection and resolution. It is important to understand the complexities and challenges involved in detecting and resolving deadlocks in a distributed system.