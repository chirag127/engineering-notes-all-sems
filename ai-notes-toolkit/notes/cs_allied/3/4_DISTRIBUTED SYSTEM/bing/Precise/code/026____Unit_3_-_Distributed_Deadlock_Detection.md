## Unit 3 - Distributed Deadlock Detection

1. **Distributed Deadlock**: A distributed deadlock is a situation where a set of processes in a distributed system are blocked and unable to proceed because they are waiting for resources held by other processes in the set.

2. **Deadlock Detection**: Deadlock detection is the process of identifying deadlocks in a distributed system. This can be done using various algorithms, such as the centralized, hierarchical, and distributed algorithms.

3. **Centralized Deadlock Detection**: In centralized deadlock detection, a single designated node, called the coordinator, is responsible for detecting deadlocks. The coordinator collects information about resource allocation and requests from all nodes in the system and uses this information to detect deadlocks.

4. **Hierarchical Deadlock Detection**: In hierarchical deadlock detection, the system is organized into a hierarchy of levels, with each level having its own coordinator responsible for deadlock detection. The coordinators at each level collect information about resource allocation and requests from the nodes at their level and use this information to detect deadlocks.

5. **Distributed Deadlock Detection**: In distributed deadlock detection, there is no designated coordinator. Instead, each node in the system is responsible for detecting deadlocks. Nodes exchange information about resource allocation and requests with their neighbors and use this information to detect deadlocks.

6. **Deadlock Resolution**: Once a deadlock has been detected, it must be resolved. This can be done using various methods, such as preemption, rollback, and killing one or more processes involved in the deadlock.

7. **Chandy-Misra-Haas Algorithm**: The Chandy-Misra-Haas algorithm is a distributed algorithm for deadlock detection. It is based on the idea of sending probe messages between nodes to detect cycles in the resource allocation graph.

8. **Edge-Chasing Algorithm**: The edge-chasing algorithm is another distributed algorithm for deadlock detection. It is based on the idea of sending probe messages along the edges of the resource allocation graph to detect cycles.

9. **Deadlock Prevention**: Deadlock prevention is the process of designing a system in such a way that deadlocks cannot occur. This can be done using various techniques, such as resource ordering, timeouts, and deadlock avoidance algorithms.