# Principle of Concurrency

- Concurrency is the execution of a set of multiple instruction sequences at the same time  .
- Concurrency occurs when there are several process threads running in parallel  .
- These threads communicate with the other threads/processes through a concept of shared memory or through message passing  .
- Concurrency can be achieved by interleaving or overlapping the execution of multiple processes.
- Interleaving means that the processes are executed one after another in a time-sharing manner.
- Overlapping means that the processes are executed simultaneously on different processors or cores.
- Concurrency can improve the performance, responsiveness, and resource utilization of a system .
- Concurrency can also introduce challenges such as synchronization, deadlock, starvation, race condition, and inconsistency   .
- Synchronization is the coordination of the execution of concurrent processes to ensure the correct order of events   .
- Deadlock is a situation where a set of processes are waiting for each other to release some resources, and none of them can proceed   .
- Starvation is a situation where a process is indefinitely delayed from accessing a resource due to the competition from other processes   .
- Race condition is a situation where the outcome of a computation depends on the relative timing of events in concurrent processes   .
- Inconsistency is a situation where the shared data or resources are modified by concurrent processes without proper synchronization, resulting in incorrect or unpredictable results   .