### Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

- Physical shared memory: The processes share the same physical memory, such as in a multiprocessor system. The hardware ensures the consistency and coherence of the shared data, and the operating system manages the allocation and protection of the memory regions.
- Virtual shared memory: The processes do not share the same physical memory, but rather a virtual memory that is mapped to their local memories, such as in a distributed system. The software ensures the consistency and coherence of the shared data, and the network provides the communication and transfer of the memory pages.

Distributed shared memory (DSM) is a form of virtual shared memory that implements the shared memory model on a distributed system that has no physically shared memory. DSM can be achieved via software as well as hardware. Software examples include middleware, libraries, and compilers that provide the abstraction of a shared memory. Hardware examples include cache coherence circuits and network interface controllers that support the transfer and synchronization of the memory pages.

DSM has some advantages over other communication models, such as message passing and remote procedure call. Some of these advantages are:

- Transparency: The processes do not need to know the location and identity of the other processes that share the memory, nor the details of the network and the communication protocols. The DSM system handles the distribution and replication of the memory pages, and the resolution of the references and the conflicts.
- Portability: The processes can run on different platforms and architectures, as long as they support the DSM system. The DSM system can also hide the heterogeneity and the failures of the underlying network and the nodes.
- Scalability: The processes can dynamically join and leave the shared memory, and the DSM system can adjust the allocation and the consistency of the memory pages accordingly. The DSM system can also exploit the locality and the concurrency of the memory accesses to improve the performance and the efficiency of the system.

However, DSM also has some challenges and limitations, such as:

- Overhead: The processes may incur additional costs for accessing the shared memory, such as network latency, bandwidth consumption, page faults, and synchronization delays. The DSM system may also consume more resources for managing the memory pages, such as memory space, network messages, and cache entries.
- Consistency: The processes may observe different values for the same memory location, depending on the timing and the order of the memory accesses, and the consistency model adopted by the DSM system. The DSM system may also need to enforce some synchronization and coherence protocols to ensure the correctness and the validity of the shared data.
- Granularity: The processes may access the shared memory at different levels of granularity, such as bytes, words, objects, or pages. The DSM system may need to balance the trade-off between the granularity and the overhead of the memory accesses, and to adapt the granularity to the characteristics and the requirements of the applications.