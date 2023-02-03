### Deadlock for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

Deadlock is a condition in a concurrent system where two or more processes are blocked, waiting for each other to release a resource. Deadlocks can occur in systems where multiple processes share resources, such as memory, files, or other system resources.

A deadlock can occur when the following conditions are met:

1. Mutual exclusion: Only one process can access a resource at a time.

2. Hold and wait: A process holds a resource and waits for another resource that is being held by another process.

3. No preemption: Resources cannot be taken away from a process once they are acquired.

4. Circular wait: A set of processes are waiting for resources in a circular chain.

Deadlocks can cause serious problems in a concurrent system, as they can lead to system hang, data corruption, and other issues. To avoid deadlocks, it is important to use appropriate synchronization mechanisms, such as semaphores, monitors, and locks.

In this unit, we will study the concept of deadlocks in concurrent systems, and examine the conditions that lead to deadlocks. We will also study the mechanisms used to detect and resolve deadlocks, and examine the trade-offs involved in using different synchronization mechanisms. This will provide a foundation for understanding the design and implementation of concurrent systems, and for exploring the various approaches to solving synchronization problems in concurrent systems.
