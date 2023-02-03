## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is a process in which a distributed system identifies and resolves deadlocks among its nodes. A deadlock occurs when two or more nodes are waiting for each other to release resources, resulting in a cycle of resource dependencies.

There are two main approaches to distributed deadlock detection: centralized and decentralized.

Centralized approaches rely on a central coordinator to monitor resource usage and detect deadlocks. Examples include:
- Chandy-Misra-Haas algorithm: a coordinator collects information from nodes about their resource usage and identifies deadlocks.
- Resource allocation graph (RAG) approach: a coordinator builds a graph of resource dependencies and identifies cycles as deadlocks.

Decentralized approaches do not rely on a central coordinator and instead use communication between nodes to detect deadlocks. Examples include:
- Distributed detection algorithm (DDA): nodes exchange messages to detect deadlocks.
- Distributed cycle detection (DCD) algorithm: nodes use a shared data structure to detect cycles and identify deadlocks.

In summary, centralized approaches rely on a central coordinator, while decentralized approaches rely on communication between nodes. Both approaches aim to detect and resolve deadlocks in a distributed system.
