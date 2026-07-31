### Shared Memory

- Shared memory is a form of memory architecture where physically separated memories can be addressed as a single shared address space.
- Shared memory can be implemented in hardware or software, or a combination of both.
- Shared memory can be used to facilitate communication and synchronization among processes or threads in a distributed system.
- Shared memory can be classified into two types: physical shared memory and distributed shared memory.

#### Physical Shared Memory

- Physical shared memory is a memory architecture where multiple processors or nodes share a common physical memory.
- Physical shared memory can be accessed by all processors or nodes using the same address space.
- Physical shared memory requires hardware support for cache coherence, memory consistency, and memory protection.
- Physical shared memory can provide high performance and low latency, but it is limited by the scalability and reliability of the hardware.

#### Distributed Shared Memory

- Distributed shared memory (DSM) is a memory architecture where multiple processors or nodes have their own local memories, but they can access each other's memories as if they were shared.
- Distributed shared memory can be implemented using software techniques, such as page-based, object-based, or tuple-based approaches .
- Distributed shared memory provides a virtual address space that is shared among all processors or nodes.
- Distributed shared memory can overcome the limitations of physical shared memory, such as scalability and reliability, but it introduces challenges such as data consistency, data replication, and data migration .