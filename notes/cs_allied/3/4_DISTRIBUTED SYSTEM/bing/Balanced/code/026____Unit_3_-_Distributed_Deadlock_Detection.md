```markdown
## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines in a distributed system.
- Deadlock detection is a strategy to handle deadlocks by identifying and resolving them after they occur.
- Deadlock detection in distributed systems requires addressing two basic issues:
  - How to detect the existence of deadlocks in the system.
  - How to resolve the detected deadlocks by aborting some deadlocked processes.
- Deadlock detection in distributed systems can be done using three approaches:
  - Global wait-for graph (WFG) approach: A centralized or distributed algorithm that constructs a global graph of processes and resources from local graphs at each node and checks for cycles in the global graph.
  - Edge chasing or path pushing approach: A distributed algorithm that initiates probes along the edges of the local wait-for graphs and detects cycles when a probe returns to its originator.
  - Diffusing computation approach: A distributed algorithm that initiates a diffusing computation when a process is blocked and detects a deadlock when the diffusing computation terminates without granting the request.
- The advantages and disadvantages of each approach depend on factors such as the frequency of deadlock occurrence, the number of processes and resources, the communication and computation costs, and the degree of concurrency.
```