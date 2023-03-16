# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a distributed shared memory, certain issues must be addressed. Some of the design issues in Distributed Shared Memory are:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the unit of data transfer between the nodes of the system.
2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space can affect the performance of the system.
3. **Memory coherence**: Memory coherence is the consistency of shared data between the nodes of the system. It is important to ensure that all nodes have a consistent view of the shared data.
4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity.
5. **Implementation methods**: The implementation methods used can affect the performance and scalability of the system.

These are some of the design issues that must be considered when designing a Distributed Shared Memory system.