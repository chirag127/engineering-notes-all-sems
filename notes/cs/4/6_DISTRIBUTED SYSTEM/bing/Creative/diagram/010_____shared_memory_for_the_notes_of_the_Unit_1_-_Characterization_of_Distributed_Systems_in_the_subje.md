### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical shared memory. The DSM system manages the memory across all the nodes and provides the illusion of a single shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the communication and synchronization of the shared data. Hardware DSM relies on special hardware components, such as cache coherence circuits or network interface controllers, to maintain the consistency of the shared data.
- DSM has several advantages, such as:
  - It simplifies the programming of distributed applications by hiding the details of data distribution and communication.
  - It allows the programmers to use the familiar shared memory model and synchronization primitives, such as locks, semaphores, or monitors.
  - It enables the exploitation of data locality and parallelism by allowing the processes to access the shared data in their local memory or cache.
  - It facilitates the dynamic load balancing and fault tolerance by allowing the migration and replication of the shared data across the nodes.
- DSM also has some challenges, such as:
  - It requires a high-performance and reliable network to support the frequent data transfers and updates.
  - It introduces the overhead of maintaining the coherence and consistency of the shared data, which may affect the performance and scalability of the system.
  - It may cause false sharing or thrashing, which are situations where multiple processes access or modify the same memory block or page, even though they do not share any data in that block or page. This may result in unnecessary data transfers and invalidations.
  - It may suffer from the granularity problem, which is the trade-off between the size of the memory blocks or pages that are shared and the frequency of the data transfers and updates. Smaller blocks or pages may reduce the false sharing and thrashing, but increase the communication overhead. Larger blocks or pages may reduce the communication overhead, but increase the false sharing and thrashing.