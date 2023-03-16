### Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it avoids the overhead of copying data between processes or kernel space.
- Shared memory can be implemented in different ways, depending on the architecture and the operating system of the embedded system.
- Some common types of shared memory are:

  - **Physical shared memory**: This is when multiple processors or cores share the same physical memory, such as RAM or ROM. The processors can access the shared memory directly through the memory bus or through a cache-coherent interconnect. This type of shared memory is common in symmetric multiprocessing (SMP) or multicore systems .
  - **Virtual shared memory**: This is when multiple processes share the same virtual address space, but the physical memory may be distributed across different locations. The operating system manages the mapping of virtual addresses to physical addresses and handles the page faults and memory protection. This type of shared memory is common in distributed systems or clusters.
  - **Distributed shared memory**: This is when multiple processes share a logical memory space that is implemented by a middleware layer on top of the network communication. The middleware layer provides the abstraction of shared variables and handles the consistency, coherence, and synchronization of the shared data. This type of shared memory is common in distributed embedded systems or real-time systems.