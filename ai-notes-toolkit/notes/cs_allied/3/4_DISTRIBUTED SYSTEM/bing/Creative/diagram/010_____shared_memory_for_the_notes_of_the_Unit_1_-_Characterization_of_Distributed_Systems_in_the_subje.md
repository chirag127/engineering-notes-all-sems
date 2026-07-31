### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but not a physical memory. The DSM system manages the memory across all the nodes and provides the illusion of a shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the memory consistency, coherence, and synchronization. Hardware DSM relies on special hardware components, such as cache coherence circuits and network interface controllers, to handle the memory operations.
- DSM has some advantages over other programming models, such as message passing or remote procedure calls, in distributed systems. Some of these advantages are:
  - It simplifies the programming by hiding the details of data distribution and communication.
  - It allows the programmers to use familiar shared memory constructs, such as locks, semaphores, and monitors, to synchronize the processes.
  - It enables the use of existing shared memory applications and libraries in distributed systems without much modification.
  - It can improve the performance by exploiting the locality of data access and reducing the communication overhead.
- DSM also has some challenges and limitations, such as:
  - It requires a large amount of network bandwidth and memory to maintain the consistency and coherence of the shared data.
  - It may incur high latency and overhead for accessing remote data or resolving conflicts.
  - It may suffer from false sharing, which is when multiple processes access different parts of the same memory page or cache line, causing unnecessary invalidations and updates.
  - It may not be suitable for some applications that require fine-grained data access or strong consistency guarantees.