## Unit 3 - Distributed Deadlock Detection

1. **Distributed Deadlock**: A distributed deadlock is a situation where a set of processes are blocked, waiting for resources held by other processes in the set, in a distributed system.
2. **Distributed Deadlock Detection**: Distributed deadlock detection is the process of detecting deadlocks in a distributed system.
3. **Challenges**: Detecting deadlocks in a distributed system is more challenging than in a centralized system due to the lack of global information and the need for coordination among multiple sites.
4. **Detection Algorithms**: There are several algorithms for detecting distributed deadlocks, including the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.
5. **Path-Pushing Algorithm**: The path-pushing algorithm involves sending probe messages along the wait-for graph to detect cycles. If a cycle is detected, a deadlock is declared.
6. **Edge-Chasing Algorithm**: The edge-chasing algorithm involves sending probe messages along the wait-for graph to detect cycles. If a cycle is detected, a deadlock is declared.
7. **Diffusing Computation Algorithm**: The diffusing computation algorithm involves initiating a distributed computation to detect cycles in the wait-for graph. If a cycle is detected, a deadlock is declared.
8. **Comparison**: Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific characteristics of the distributed system.
