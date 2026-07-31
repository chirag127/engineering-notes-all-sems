## Unit 2 - Concurrent Processes

- A concurrent process is a process that can execute simultaneously with other processes on a system, or that can be interleaved with other processes on a single processor system.
- Concurrent processes can communicate and synchronize with each other using shared memory or message passing mechanisms.
- Concurrent processes can be created by using threads, processes, or distributed systems.
- Concurrent processes can be classified into two types: independent and cooperating.
  - Independent processes do not affect or be affected by the execution of other processes.
  - Cooperating processes can share data or resources with other processes, or coordinate their actions with other processes.
- Concurrent processes can have different states, such as ready, running, blocked, or terminated.
- Concurrent processes can be managed by the operating system using scheduling algorithms, such as round-robin, priority, or shortest job first.
- Concurrent processes can face challenges, such as deadlock, starvation, race conditions, or livelock.
  - Deadlock occurs when a set of processes are waiting for each other to release some resources, and none of them can proceed.
  - Starvation occurs when a process is indefinitely denied access to a resource or the CPU.
  - Race condition occurs when the outcome of a computation depends on the order or timing of the execution of concurrent processes.
  - Livelock occurs when a set of processes are constantly changing their states in response to each other, but none of them can make progress.