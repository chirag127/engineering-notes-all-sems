### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a distributed shared memory system, certain issues must be addressed. Some of these issues include:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the level of detail at which the system operates.
2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space determines how data is organized and accessed.
3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. It ensures that all nodes have a consistent view of the shared data.
4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity.
5. **Implementation methods**: Implementation methods refer to the techniques used to implement the DSM system. These methods can affect the performance and functionality of the system.

These are some of the design issues that must be considered when designing a distributed shared memory system. Each of these issues can affect the performance, functionality, and usability of the system.