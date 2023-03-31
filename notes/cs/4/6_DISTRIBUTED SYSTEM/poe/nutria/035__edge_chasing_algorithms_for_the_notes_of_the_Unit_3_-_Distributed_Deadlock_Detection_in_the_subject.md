
### Edge Chasing Algorithms for Unit 3 - Distributed Deadlock Detection

1. Edge chasing algorithms are used in distributed systems to detect deadlocks.
2. In edge chasing, each process maintains a pointer to a vertex in a global wait-for graph.
3. The wait-for graph is a directed graph that shows which process is waiting for which other process.
4. In order to detect deadlocks, each process sends messages to its neighbors in the wait-for graph.
5. Each process follows the pointers in the messages to update its own pointer.
6. If a process finds that it has no more neighbors to follow, it has found a deadlock.
7. The process then sends a message to all other processes in the graph, informing them of the deadlock.
8. The deadlock can then be resolved by rolling back the processes involved in the deadlock.