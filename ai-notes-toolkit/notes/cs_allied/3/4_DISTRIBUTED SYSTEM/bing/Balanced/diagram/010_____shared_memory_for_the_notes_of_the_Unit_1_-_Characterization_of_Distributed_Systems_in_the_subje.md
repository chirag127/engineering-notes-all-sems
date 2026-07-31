### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical shared memory. The DSM system manages the memory across all the nodes and provides the illusion of a single shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the communication and synchronization of the shared data. Hardware DSM relies on special hardware components, such as cache coherence circuits or network interface controllers, to handle the communication and synchronization of the shared data.
- DSM has several advantages, such as:
  - It simplifies the programming of distributed applications by hiding the details of data distribution and communication.
  - It allows the programmers to use the familiar shared memory model and synchronization primitives, such as locks, semaphores, or monitors.
  - It enables the exploitation of data locality and parallelism by allowing the processes to access the shared data in their local memory or cache.
  - It supports dynamic load balancing and fault tolerance by allowing the system to migrate the shared data across the nodes according to the workload or the availability of the nodes.
- DSM also has some challenges, such as:
  - It requires a high-performance and reliable network to support the communication and synchronization of the shared data.
  - It may incur high overhead and latency due to the data transfer and consistency maintenance of the shared data.
  - It may suffer from false sharing, which is when multiple processes access different parts of the same memory block or cache line, causing unnecessary invalidations and updates of the shared data.
  - It may have scalability issues due to the limited address space or the increased contention of the shared data.