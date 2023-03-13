### Distributed Deadlock Detection for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled using three strategies: deadlock prevention, deadlock avoidance, and deadlock detection .
- Deadlock prevention and avoidance are impractical in distributed systems, as they require global knowledge and coordination of the system.
- Deadlock detection is the best approach to handle deadlocks in distributed systems. It involves two steps: detecting the existence of deadlocks and resolving the detected deadlocks.
- Deadlock detection requires an examination of the status of the process-resource interactions for the presence of cyclic wait .
- There are three approaches to detect deadlocks in distributed systems: centralized, distributed, and hierarchical.
- Centralized approach: One node is designated as the deadlock detector and collects information from all other nodes about their resource allocation and requests. The deadlock detector constructs a global wait-for graph and checks for cycles. If a cycle is found, it indicates a deadlock and the detector informs the nodes involved to abort or rollback.
- Advantages of centralized approach: Simple and easy to implement. Only one node needs to maintain the global wait-for graph.
- Disadvantages of centralized approach: Single point of failure. If the deadlock detector node fails, the whole system is vulnerable to deadlocks. High communication and computation overhead. The deadlock detector node has to collect information from all other nodes frequently and check for cycles in the graph.
- Distributed approach: All nodes cooperate to detect deadlocks. Each node maintains a local wait-for graph and exchanges information with its neighbors. A node initiates a probe message when it suspects a deadlock. The probe message travels along the edges of the local wait-for graphs and returns to the initiator if a cycle is found. The initiator then initiates a resolution protocol to break the deadlock.
- Advantages of distributed approach: No single point of failure. The workload is distributed among all nodes. The speed of deadlock detection is increased.
- Disadvantages of distributed approach: Complex and difficult to implement. The nodes have to synchronize their local wait-for graphs and handle multiple probe messages. The probe messages may cause false or phantom deadlocks if the local wait-for graphs are not consistent.
- Hierarchical approach: The nodes are organized into a hierarchy of clusters. Each cluster has a coordinator node that acts as the deadlock detector for the cluster. The coordinator nodes communicate with each other to detect global deadlocks. The deadlock detection algorithm can be either centralized or distributed within each cluster.
- Advantages of hierarchical approach: Scalable and flexible. The hierarchy can be adjusted according to the system size and topology. The communication and computation overhead is reduced compared to the centralized and distributed approaches.
- Disadvantages of hierarchical approach: More complex and difficult to implement than the centralized approach. The hierarchy may introduce delays and inaccuracies in deadlock detection. The coordinator nodes may become bottlenecks or single points of failure.
- Mnemonics and learning tricks: 
  - To remember the three strategies for deadlock handling, use the acronym PAD: Prevention, Avoidance, Detection.
  - To remember the three approaches for deadlock detection, use the acronym CDH: Centralized, Distributed, Hierarchical.
  - To remember the advantages and disadvantages of each approach, use the following table:

| Approach | Advantages | Disadvantages |
| --- | --- | --- |
| Centralized | Simple, Easy | Single point of failure, High overhead |
| Distributed | No single point of failure, Fast | Complex, False deadlocks |
| Hierarchical | Scalable, Flexible, Low overhead | Complex, Delayed, Bottlenecks |