### Unit 3 - Distributed Deadlock Detection

#### Detection & Resolution

- Distributed deadlock detection is the process of detecting deadlocks in a distributed system.
- Deadlocks occur when two or more processes are blocked, waiting for resources held by each other.
- In a distributed system, deadlocks can occur between processes running on different nodes.
- There are several approaches to detecting and resolving deadlocks in distributed systems, including:
  - **Centralized approach:** A central coordinator is responsible for detecting deadlocks and initiating resolution.
  - **Hierarchical approach:** The system is organized into a hierarchy of coordinators, with each coordinator responsible for detecting deadlocks within its own domain.
  - **Distributed approach:** Each node in the system participates in deadlock detection and resolution.
- Once a deadlock is detected, there are several ways to resolve it, including:
  - **Preemption:** One or more processes involved in the deadlock are forced to release their resources.
  - **Rollback:** One or more processes involved in the deadlock are rolled back to a previous state, releasing their resources.
  - **Killing processes:** One or more processes involved in the deadlock are terminated, releasing their resources.
- The choice of resolution method depends on the specific requirements of the system and the nature of the deadlock.