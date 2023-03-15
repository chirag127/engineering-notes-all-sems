## Unit 2 - Concurrent Processes

- A concurrent process is a process that can execute simultaneously with other processes on a multiprocessor system, or appear to execute simultaneously on a uniprocessor system.
- Concurrent processes can communicate and synchronize with each other using shared memory or message passing.
- Concurrent processes can be created dynamically or statically, depending on the programming language and the operating system.
- Concurrent processes can be classified into threads, processes, and distributed processes, based on their degree of independence and resource sharing.
- Threads are the smallest units of concurrency. They share the same address space and resources of a process, but have their own program counter, stack, and registers.
- Processes are independent units of concurrency. They have their own address space and resources, and can communicate with other processes using interprocess communication (IPC) mechanisms.
- Distributed processes are processes that run on different machines connected by a network. They can communicate with each other using message passing or remote procedure calls (RPCs).
- Concurrent processes can be managed by the operating system using scheduling algorithms, synchronization primitives, and deadlock prevention and avoidance techniques.
- Scheduling algorithms determine which process or thread gets to use the CPU at any given time, based on criteria such as priority, fairness, and response time.
- Synchronization primitives are tools that help concurrent processes coordinate their access to shared resources, such as semaphores, locks, monitors, and condition variables.
- Deadlock is a situation where a set of processes are waiting for each other to release some resources, and none of them can proceed. Deadlock can be prevented by imposing some constraints on resource allocation, or avoided by detecting and resolving it dynamically.