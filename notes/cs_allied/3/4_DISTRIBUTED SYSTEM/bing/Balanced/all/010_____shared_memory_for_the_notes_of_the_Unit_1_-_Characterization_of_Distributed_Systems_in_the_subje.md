# Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

## Physical Shared Memory

Physical shared memory refers to a system where multiple processors are connected to a single memory module, or a shared bus that interconnects multiple memory modules. Each processor can directly access any memory location by issuing a load or store instruction. Physical shared memory systems are also known as symmetric multiprocessors (SMPs) or uniform memory access (UMA) systems.

The advantages of physical shared memory are:

- It provides a simple and uniform programming model, where all processes can access the same variables and data structures without explicit message passing.
- It allows for low-latency and high-bandwidth communication among processes, as they can access the shared memory in a single instruction cycle.
- It supports fine-grained parallelism, where processes can operate on small chunks of data without incurring significant overhead.

The disadvantages of physical shared memory are:

- It is expensive and difficult to scale, as the number of processors and memory modules increases. The shared bus or memory module can become a bottleneck for communication and contention.
- It requires hardware support for cache coherence, which ensures that all processors see a consistent view of the shared memory. Cache coherence protocols can introduce additional complexity and overhead to the system.
- It is prone to errors and inconsistencies, as processes can overwrite each other's data or access invalid memory locations. Processes need to use synchronization mechanisms, such as locks, semaphores, or atomic operations, to coordinate their access to the shared memory.

## Virtual Shared Memory

Virtual shared memory refers to a system where multiple processors have their own local memory modules, but they can access a common virtual address space that is mapped to the physical memory of different processors. Virtual shared memory systems are also known as distributed shared memory (DSM) or non-uniform memory access (NUMA) systems.

The advantages of virtual shared memory are:

- It can scale to a large number of processors and memory modules, as they are connected by a network rather than a shared bus or memory module. The network can provide higher bandwidth and lower contention than the shared bus or memory module.
- It can exploit the locality of reference, where processes access data that are close to their local memory more frequently than data that are far away. This can reduce the communication and synchronization overhead among processes.
- It can support heterogeneous processors and memory modules, where different processors can have different architectures, speeds, or capacities. This can increase the flexibility and performance of the system.

The disadvantages of virtual shared memory are:

- It requires software support for consistency, which ensures that all processes see a consistent view of the virtual shared memory. Consistency protocols can introduce additional complexity and overhead to the system.
- It can incur high-latency and low-bandwidth communication among processes, as they need to send messages over the network to access remote memory locations. The network can also introduce delays and failures to the communication.
- It can cause false sharing, where processes access different data that are mapped to the same physical memory location. This can trigger unnecessary communication and synchronization among processes.

There are different ways of implementing virtual shared memory, such as page-based, object-based, or tuple-based approaches. Each approach has its own advantages and disadvantages, depending on the granularity, distribution, and access patterns of the shared data.