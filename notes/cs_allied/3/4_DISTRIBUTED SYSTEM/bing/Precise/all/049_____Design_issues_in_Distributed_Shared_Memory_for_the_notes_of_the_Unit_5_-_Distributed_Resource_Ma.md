# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a DSM system, certain issues must be addressed:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the level of detail at which the system maintains coherence.
2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space affects the performance and scalability of the system.
3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. It is important to ensure that all nodes have a consistent view of the shared data.
4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity.
5. **Implementation methods**: Implementation methods refer to the techniques used to implement the DSM system. These methods affect the performance and scalability of the system.

These are some of the key design issues that must be addressed when designing a DSM system. A well-designed DSM system can provide the ease-of-programming benefits of bus-based SMP systems with the scalability of MPP/Cluster message-passing systems.