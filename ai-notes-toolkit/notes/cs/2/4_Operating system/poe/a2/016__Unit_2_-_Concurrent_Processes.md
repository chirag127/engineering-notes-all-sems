 Here is the formal content in Markdown format without any emojis or external links:

## Unit 2 - Concurrent Processes

1. Processes - Programs in execution. Each process has its own memory space.
2. Multiprogramming - Having multiple processes in memory and switching between them. Increases CPU utilization.
3. Context Switch - Saving and restoring of state of a process so that it can be resumed later. This has some overhead.
4. Process Scheduling - Choosing which process to execute at a given time. Done by the OS. Goals include maximizing CPU utilization, being fair, meeting deadlines.
5. Types of Schedulers - Long term (decide which processes to load into memory), Medium term (decide which processes to swap in/out), Short term (choose among ready processes).
6. Process Synchronization - Ensuring smooth interaction between processes, avoiding race conditions.
7. Critical Section - Code segment that accesses shared resource. Only one process at a time should execute it.
8. Semaphores - Synchronization tools to restrict number of concurrent processes in critical section. Two operations - P (decrement and enter critical section) and V (increment).
9. Deadlocks - Circular wait condition between two or more processes. Can be avoided by breaking one of the conditions in the deadlock definition.
10. Starvation - Low priority processes may never get CPU time. Prevent using aging, priority increment, etc.

The content summarizes key points about concurrent processes, process scheduling, synchronization and deadlocks. The points are written in a formal tone as bullet points for easy understanding. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.