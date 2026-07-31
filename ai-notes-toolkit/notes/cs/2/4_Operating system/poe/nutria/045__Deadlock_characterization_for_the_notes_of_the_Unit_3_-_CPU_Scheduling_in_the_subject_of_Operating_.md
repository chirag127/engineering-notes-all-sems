
### Deadlock Characterization for the Notes of the Unit 3 - CPU Scheduling in the Subject of Operating System

1. Deadlock is a situation in which two or more processes are unable to continue because each process is waiting for one of the others to do something.

2. Deadlock can occur in a system with multiple processes or threads of execution if the following conditions are met:

- Mutual Exclusion: At least one resource must be non-sharable, meaning that only one process can use it at a time.

- Hold and Wait: A process must be holding at least one resource while waiting to acquire additional resources that are being held by other processes.

- No Preemption: Resources cannot be preempted, meaning that a process cannot take a resource away from another process.

- Circular Wait: A circular chain of processes must exist, where each process is waiting for a resource held by the next one in the chain.

3. Deadlock avoidance is a technique used to prevent deadlock from occurring in a system. It requires that processes request resources in a predetermined order and that resources are allocated to processes in the same order. This prevents the possibility of a circular wait condition from occurring.