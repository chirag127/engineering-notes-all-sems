### Detection & Resolution

- Detection and resolution are two complementary techniques for handling deadlocks in distributed systems.
- Detection involves identifying the existence of a deadlock by examining the state of the system, such as the resource allocation graph or the wait-for graph.
- Resolution involves breaking the deadlock by taking some actions, such as aborting or preempting some processes or resources involved in the deadlock cycle.
- Detection and resolution can be performed either in a centralized or a distributed manner, depending on the architecture and the communication model of the system.
- Centralized detection and resolution rely on a single coordinator node that collects the global state information from all the other nodes and performs the detection and resolution algorithms.
- Distributed detection and resolution rely on the cooperation of multiple nodes that exchange messages and perform local computations to detect and resolve deadlocks.
- Centralized detection and resolution have the advantages of simplicity, efficiency, and optimality, but they also have the disadvantages of single point of failure, communication overhead, and scalability issues.
- Distributed detection and resolution have the advantages of fault tolerance, reduced communication overhead, and scalability, but they also have the disadvantages of complexity, inefficiency, and suboptimality.