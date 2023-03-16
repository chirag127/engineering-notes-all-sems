# Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

## Physical Shared Memory

Physical shared memory refers to a system where multiple processors are connected to a single memory module, or a shared bus that interconnects multiple memory modules. Each processor can directly access any memory location by issuing a load or store instruction. Physical shared memory systems are also known as symmetric multiprocessors (SMPs) or uniform memory access (UMA) systems.

The advantages of physical shared memory are:

- It provides a simple and uniform programming model, where all processes can access the same variables and data structures without explicit message passing.
- It allows for low-latency and high-bandwidth communication among processes, as they do not need to copy data across the network.
- It supports fine-grained parallelism, where processes can operate on small chunks of data without incurring significant overhead.

The disadvantages of physical shared memory are:

- It is limited by the scalability and cost of the hardware, as adding more processors and memory modules increases the complexity and contention of the shared bus or interconnect.
- It requires hardware support for cache coherence, which ensures that all processors see a consistent view of the memory. Cache coherence protocols can introduce additional overhead and complexity, and may not be suitable for some applications.
- It does not tolerate faults well, as a failure of a processor or a memory module can affect the entire system.

## Virtual Shared Memory

Virtual shared memory refers to a system where multiple processors have their own local memory, but they can access a common logical address space that is distributed across the network. Virtual shared memory systems are also known as distributed shared memory (DSM) systems or non-uniform memory access (NUMA) systems.

The advantages of virtual shared memory are:

- It can scale to a large number of processors and memory modules, as they are connected by a network that can be expanded and reconfigured easily.
- It can tolerate faults better, as a failure of a processor or a memory module can be isolated and recovered from by the rest of the system.
- It can exploit locality, where processes can access their local memory faster than the remote memory, and reduce the network traffic and latency.

The disadvantages of virtual shared memory are:

- It requires software support for consistency, which ensures that all processes see a coherent view of the memory. Consistency protocols can introduce additional overhead and complexity, and may not be suitable for some applications.
- It provides a less uniform and more complex programming model, where processes need to be aware of the distribution and location of the memory, and may need to use explicit message passing or synchronization primitives.
- It supports coarse-grained parallelism, where processes need to operate on large chunks of data to amortize the network overhead.

There are different ways of implementing virtual shared memory, such as page-based, object-based, or tuple-based approaches. Each approach has its own trade-offs and challenges, such as granularity, coherence, replication, migration, and synchronization.