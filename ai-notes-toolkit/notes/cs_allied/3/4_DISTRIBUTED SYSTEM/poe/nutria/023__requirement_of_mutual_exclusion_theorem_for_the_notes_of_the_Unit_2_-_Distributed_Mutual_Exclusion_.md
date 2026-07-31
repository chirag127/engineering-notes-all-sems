
### Requirements of Mutual Exclusion Theorem

1. Mutual exclusion must be guaranteed: No two processes can be in their critical section at the same time.
2. Progress must be guaranteed: If no process is in its critical section and some processes wish to enter their critical section, then only those processes that are not delayed indefinitely are allowed to enter.
3. Bounded waiting must be guaranteed: A bound must exist on the number of times that other processes are allowed to enter their critical section after a process has made a request to enter its own critical section and before that request is granted.
4. Circular wait must be avoided: A bound must exist on the number of times that a process can enter its critical section after a process has made a request to enter its own critical section and before that request is granted. This bound must be independent of the number of processes in the system.