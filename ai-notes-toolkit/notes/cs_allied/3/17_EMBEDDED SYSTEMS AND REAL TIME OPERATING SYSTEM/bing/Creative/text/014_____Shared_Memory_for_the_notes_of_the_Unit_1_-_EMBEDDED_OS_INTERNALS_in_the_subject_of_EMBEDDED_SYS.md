### Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it avoids the overhead of copying data between processes or kernel space.
- Shared memory can be implemented in different ways, such as:
  - System V shared memory: a POSIX-compliant API that creates and attaches shared memory segments using system calls and identifiers.
  - POSIX shared memory: a newer API that creates and maps shared memory objects using file descriptors and memory-mapped files.
  - Memory-mapped files: a technique that maps a file or a device into the virtual address space of a process, allowing it to be accessed as if it were in memory.
  - Anonymous memory mapping: a variation of memory-mapped files that does not use a file or a device, but allocates a region of memory that can be shared by multiple processes.
- Shared memory can also be classified into two types, depending on the scope and visibility of the shared region:
  - Local shared memory: a shared memory region that is accessible only by processes on the same node or processor.
  - Distributed shared memory: a shared memory region that is accessible by processes on different nodes or processors, usually through a network or a bus.
- Shared memory systems have advantages and disadvantages, such as:
  - Advantages: high performance, low latency, simple programming model, easy data sharing, and scalability.
  - Disadvantages: complex synchronization, potential memory corruption, security risks, and portability issues.