## Unit 2 - Concurrent Processes

1. **Introduction:** Concurrent processes refer to multiple processes that are executed simultaneously. These processes can be executed on a single processor or multiple processors.

2. **Interleaving:** In a single processor system, the processes are interleaved, meaning that the processor switches between executing different processes. This gives the illusion of simultaneous execution.

3. **Synchronization:** When multiple processes are executed concurrently, there is a need for synchronization to ensure that the processes do not interfere with each other. This is achieved through the use of synchronization primitives such as semaphores and monitors.

4. **Deadlocks:** A deadlock occurs when two or more processes are waiting for each other to release resources, resulting in a situation where none of the processes can proceed. Deadlock prevention and avoidance techniques are used to prevent this situation from occurring.

5. **Starvation:** Starvation occurs when a process is perpetually denied access to a resource it needs to proceed. This can happen when a resource is always allocated to other processes, leaving the starving process waiting indefinitely.

6. **Concurrency Control:** Concurrency control is the process of managing the simultaneous execution of multiple processes to ensure that the system remains in a consistent state. This is achieved through the use of locking and other techniques.

7. **Summary:** Concurrent processes are multiple processes that are executed simultaneously. Synchronization is necessary to ensure that the processes do not interfere with each other. Deadlocks and starvation are potential issues that can arise when multiple processes are executed concurrently. Concurrency control is used to manage the simultaneous execution of multiple processes.