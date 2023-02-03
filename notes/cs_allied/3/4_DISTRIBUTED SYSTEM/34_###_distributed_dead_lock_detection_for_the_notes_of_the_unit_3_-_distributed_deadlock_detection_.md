### distributed dead lock detection for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Distributed deadlock detection is the process of identifying deadlocks in a distributed system. A deadlock occurs when two or more processes are waiting for each other to release resources, resulting in a cycle of resource dependencies.

There are two main approaches to distributed deadlock detection: centralized and decentralized.

Centralized approaches rely on a central coordinator to monitor resource usage and detect deadlocks. Examples include:
- Chandy-Misra-Haas algorithm: a coordinator collects information from nodes about their resource usage and identifies deadlocks.
- Resource allocation graph (RAG) approach: a coordinator builds a graph of resource dependencies and identifies cycles as deadlocks.

Decentralized approaches do not rely on a central coordinator and instead use communication between nodes to detect deadlocks. Examples include:
- Distributed detection algorithm (DDA): nodes exchange messages to detect deadlocks.
- Distributed cycle detection (DCD) algorithm: nodes use a shared data structure to detect cycles and identify deadlocks.

In summary, distributed deadlock detection is the process of identifying deadlocks in a distributed system, and can be performed using either centralized or decentralized approaches. Centralized approaches rely on a central coordinator, while decentralized approaches rely on communication between nodes.
