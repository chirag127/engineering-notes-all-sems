### Unit 3 - Distributed Deadlock Detection

#### Detection & Resolution

1. **Detection**: In a distributed system, deadlock detection is more complex than in a centralized system. This is because the resources and processes are distributed across multiple nodes, and there is no global state available to detect deadlocks. There are two main approaches to deadlock detection in distributed systems: centralized and distributed.

    - **Centralized approach**: In this approach, a single node is designated as the deadlock detector. This node is responsible for collecting information about resource allocation and process states from all other nodes in the system. It then uses this information to construct a global wait-for graph and detect cycles, which indicate the presence of a deadlock.

    - **Distributed approach**: In this approach, each node in the system is responsible for detecting deadlocks locally. Nodes communicate with each other to exchange information about resource allocation and process states. Each node constructs a local wait-for graph and detects cycles. If a cycle is detected, the nodes involved in the cycle coordinate to resolve the deadlock.

2. **Resolution**: Once a deadlock has been detected, it must be resolved. There are several approaches to resolving deadlocks in distributed systems, including:

    - **Preemption**: In this approach, one or more processes involved in the deadlock are forced to release some or all of their resources, allowing other processes to proceed.

    - **Rollback**: In this approach, one or more processes involved in the deadlock are rolled back to a previous state, releasing their resources and allowing other processes to proceed.

    - **Process termination**: In this approach, one or more processes involved in the deadlock are terminated, releasing their resources and allowing other processes to proceed.