### Deadlock Characterization

Deadlock is a situation in which two or more processes are blocked and unable to proceed because they are waiting for each other to release resources. In order for a deadlock to occur, the following four conditions must be met simultaneously:

1. **Mutual Exclusion**: At least one resource must be held in a non-shareable mode, meaning that only one process can use the resource at a time.

2. **Hold and Wait**: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.

3. **No Preemption**: Resources cannot be forcibly removed from the processes that are holding them.

4. **Circular Wait**: A circular chain of processes must exist, where each process is waiting for a resource held by the next process in the chain.

These four conditions are known as the Coffman conditions, after the researchers who first identified them. If all four conditions are met, a deadlock will occur. In order to prevent or resolve deadlocks, at least one of these conditions must be negated.