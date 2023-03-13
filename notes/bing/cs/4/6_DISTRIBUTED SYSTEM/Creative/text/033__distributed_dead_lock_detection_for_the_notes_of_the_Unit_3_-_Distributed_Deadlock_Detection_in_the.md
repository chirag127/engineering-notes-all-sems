### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled using one of the following strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems, as they require global knowledge and coordination of the system.
- Deadlock detection is the best approach to handle deadlocks in distributed systems. It entails two basic issues: detecting existing deadlocks and resolving detected deadlocks.
- Deadlock detection requires an examination of the status of the process-resource interactions for the presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: centralized, distributed, and hierarchical.
- Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource allocation and requests. The deadlock detector constructs a global wait-for graph and checks for cycles. If a cycle is found, it initiates the deadlock resolution.
- Distributed approach: Different nodes work together to detect deadlocks. Each node maintains a local wait-for graph and periodically sends it to its neighbors. The nodes exchange messages to construct a global wait-for graph and check for cycles. If a cycle is found, the nodes cooperate to resolve the deadlock.
- Hierarchical approach: The nodes are organized into a hierarchy of clusters. Each cluster has a leader node that acts as the deadlock detector for the cluster. The leader nodes communicate with each other to detect global deadlocks. If a deadlock is found, the leader nodes coordinate to resolve the deadlock.
- The advantages of the distributed and hierarchical approaches over the centralized approach are: no single point of failure, better scalability, and faster deadlock detection.
- The disadvantages of the distributed and hierarchical approaches are: more message overhead, more complexity, and possibility of false or phantom deadlocks.