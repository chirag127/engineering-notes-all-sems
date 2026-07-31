### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a distributed shared memory system, certain issues must be addressed. Some of these issues include:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the unit of transfer between nodes. The choice of granularity affects the performance of the system.

2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space affects the performance and scalability of the system.

3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. Ensuring memory coherence is a major challenge in the design of DSM systems.

4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity. These choices affect the performance, scalability, and ease of use of the system.

5. **Implementation methods**: The implementation methods used to achieve memory coherence, such as directory-based or snooping-based, affect the performance and scalability of the system.

These are some of the design issues that must be addressed when designing a distributed shared memory system. Each issue presents its own challenges and trade-offs, and the choices made will affect the overall performance and usability of the system.