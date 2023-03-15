### Deadlock Characterization

Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlock can arise if the following four conditions hold simultaneously in a system:

1. **Mutual Exclusion**: At least one resource must be held in a non-sharable mode, that is, only one process at a time can use the resource. If another process requests that resource, the requesting process must be delayed until the resource has been released.

2. **Hold and Wait**: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.

3. **No Preemption**: Resources cannot be preempted, that is, a resource can be released only voluntarily by the process holding it, after that process has completed its task.

4. **Circular Wait**: A set of processes must exist such that every process in the set is waiting for a resource that is being held by another process in the set.

These four conditions are known as the Coffman conditions, after their first description by E. G. Coffman in 1971. All four conditions must hold for a deadlock to occur. If one of these conditions is not met, then a deadlock cannot occur.