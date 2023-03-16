# Unit 3 - Distributed Deadlock Detection

### Detection & Resolution

1. **Detection**: In a distributed system, deadlock detection is more complex than in a centralized system. This is because the resources and processes are distributed across multiple nodes, and there is no global state available to detect deadlocks. Several algorithms have been proposed for distributed deadlock detection, including edge-chasing, diffusing computation, and global state detection.

2. **Resolution**: Once a deadlock has been detected, it must be resolved. There are several methods for resolving deadlocks in a distributed system, including preemption, rollback, and killing one or more processes. The choice of method depends on the specific system and the nature of the deadlock.

3. **Edge-Chasing**: This algorithm uses a probe message that is sent from a blocked process to its dependent processes. If the probe message returns to the originating process, a deadlock has been detected.

4. **Diffusing Computation**: This algorithm uses a diffusing computation to detect deadlocks. Each process maintains a wait-for graph, and when a process becomes blocked, it initiates a diffusing computation to determine if a deadlock exists.

5. **Global State Detection**: This algorithm uses a global state detection approach to detect deadlocks. A global state is constructed by collecting local state information from each node, and then a global wait-for graph is constructed to detect deadlocks.

6. **Preemption**: This method involves taking a resource away from a process and giving it to another process to resolve the deadlock.

7. **Rollback**: This method involves rolling back one or more processes to a previous state to release resources and resolve the deadlock.

8. **Killing Processes**: This method involves killing one or more processes to release resources and resolve the deadlock. This is typically a last resort, as it can result in lost work and data.