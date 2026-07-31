# Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it does not involve copying data or system calls.
- Shared memory can be implemented in different ways, such as:

  - **System V shared memory**: a POSIX-compliant API that creates and attaches segments of memory identified by keys.
  - **POSIX shared memory**: a newer API that creates and maps named or anonymous objects of memory in the file system.
  - **Memory-mapped files**: a technique that maps a file or a device into the virtual address space of a process, allowing direct access to the file contents as if they were in memory.
  - **Anonymous memory mapping**: a variation of memory-mapped files that does not use a file or a device, but allocates a region of memory that can be shared by multiple processes.

- Shared memory can also be classified into two types, depending on the scope of sharing:

  - **Local shared memory**: a region of memory that is shared by processes running on the same processor or the same multicore processor. Local shared memory can be accessed directly by the processes without any special hardware or software support.
  - **Distributed shared memory**: a region of memory that is shared by processes running on different processors or different multicore processors. Distributed shared memory requires special hardware or software mechanisms to ensure consistency and coherence of the shared data across the processors.

- Shared memory is widely used in embedded systems and real-time operating systems (RTOS) for various purposes, such as:

  - **Data exchange**: processes can share data structures, variables, or buffers through shared memory, avoiding the overhead of serialization and deserialization.
  - **Synchronization**: processes can use shared memory to implement mutual exclusion, semaphores, condition variables, or barriers, ensuring the correct order and timing of operations.
  - **Coordination**: processes can use shared memory to implement distributed algorithms, such as consensus, leader election, or distributed locking, achieving agreement and cooperation among processes.
  - **Performance**: processes can use shared memory to exploit parallelism, load balancing, or caching, improving the efficiency and scalability of the system.