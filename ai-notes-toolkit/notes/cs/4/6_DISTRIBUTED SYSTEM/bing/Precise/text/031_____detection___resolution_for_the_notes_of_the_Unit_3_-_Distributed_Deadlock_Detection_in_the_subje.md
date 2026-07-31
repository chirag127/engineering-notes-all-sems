### Detection & Resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

1. **Distributed Deadlock Detection**: In a distributed system, deadlock detection is more complex due to the lack of a central resource allocation table. Several algorithms have been proposed for distributed deadlock detection, including edge-chasing, diffusing computation, and global state detection.

2. **Edge-Chasing Algorithm**: This algorithm uses a probe message that is sent from a blocked process to its dependent processes. If the probe message returns to the originating process, a deadlock is detected.

3. **Diffusing Computation Algorithm**: This algorithm uses a diffusing computation to detect deadlocks. Each process maintains a wait-for graph and periodically initiates a diffusing computation to detect cycles in the graph.

4. **Global State Detection Algorithm**: This algorithm uses a snapshot of the global state of the system to detect deadlocks. The snapshot is taken using a distributed snapshot algorithm, and the wait-for graph is constructed from the snapshot.

5. **Resolution**: Once a deadlock is detected, it must be resolved. Common methods for resolving deadlocks include preemption, rollback, and killing one or more processes involved in the deadlock.

6. **Preemption**: This method involves temporarily taking away a resource from a process and giving it to another process to break the deadlock.

7. **Rollback**: This method involves rolling back one or more processes to a previous state to break the deadlock.

8. **Killing Processes**: This method involves killing one or more processes involved in the deadlock to break the deadlock. This is usually the last resort, as it can result in lost work and data.