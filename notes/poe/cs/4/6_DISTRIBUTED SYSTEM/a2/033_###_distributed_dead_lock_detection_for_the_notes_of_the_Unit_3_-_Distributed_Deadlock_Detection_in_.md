 Here is the content in markdown format for the topic ### Distributed Deadlock Detection for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM:

### Distributed Deadlock Detection

- Distributed deadlocks can occur in distributed systems when multiple processes on different servers hold locks on shared resources and wait for each other to release locks, thereby creating a cyclic dependency.
- Some ways to detect distributed deadlocks:

1. Wait-for graph: Construct a directed graph with processes as nodes and resource dependencies as edges. A cycle in the graph indicates a deadlock. This is centralized and requires global knowledge of resource allocation.

2. Timeout: Set a timeout period for resource requests. If a process waits beyond the timeout period, it is assumed to be deadlocked and is aborted. This may lead to false positives and wasting work done by processes.

3. Tracing: Track the sequence of events leading to a deadlock and log them. The log can then be analyzed to detect deadlocks. This has a high overhead and the log size can grow quickly with system scale.

- Advantages: Detects actual deadlocks; Disadvantages: Requires global knowledge; High overhead

- Examples: Distributed database systems, distributed operating systems

- No easy mnemonics here. The concepts are straightforward but the implementations can be challenging to scale. Understanding the pros and cons of different schemes is important.

- Here is an ASCII diagram showing a simple distributed deadlock with 2 processes and 2 resources:

Process 1: Request Resource 1 -> Request Resource 2
Process 2: Request Resource 2 -> Request Resource 1

[Resource 1] <