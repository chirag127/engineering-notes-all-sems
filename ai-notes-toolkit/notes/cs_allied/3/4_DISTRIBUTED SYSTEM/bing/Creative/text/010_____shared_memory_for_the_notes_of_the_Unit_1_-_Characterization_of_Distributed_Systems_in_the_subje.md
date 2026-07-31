### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical access to the same memory, such as in a cluster or a grid.
- DSM systems can provide the illusion of a shared memory model on a distributed system that has no physically shared memory, by using software or hardware mechanisms to manage the data movement and consistency across the nodes.
- DSM systems can have different architectures, such as page-based, object-based, or tuple-based, depending on how the shared data is organized and accessed.
- DSM systems can have different consistency models, such as sequential, causal, or eventual, depending on how the updates to the shared data are propagated and ordered among the nodes.
- DSM systems can have different advantages, such as:
  - Transparency: DSM systems can hide the details of data distribution and communication from the programmer, making the programming model simpler and more portable.
  - Scalability: DSM systems can scale up to a large number of nodes and support dynamic addition and removal of nodes, without affecting the performance or correctness of the shared memory model.
  - Fault-tolerance: DSM systems can tolerate node failures and network partitions, by using replication, caching, or checkpointing techniques to ensure the availability and consistency of the shared data.