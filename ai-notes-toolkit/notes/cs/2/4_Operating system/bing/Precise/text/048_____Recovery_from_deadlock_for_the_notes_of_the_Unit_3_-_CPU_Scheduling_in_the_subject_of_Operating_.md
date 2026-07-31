### Recovery from Deadlock

Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. To recover from deadlock, there are two methods:

1. **Process Termination**: One way to recover from deadlock is to terminate one or more processes involved in the deadlock. There are two ways to do this:
    - **Abort all deadlocked processes**: This method will break the deadlock cycle but at a great expense. The processes will lose all the work they have done.
    - **Abort one process at a time until the deadlock cycle is eliminated**: This method incurs considerable overhead since after each process is aborted, a deadlock detection algorithm must be invoked to determine whether any processes are still deadlocked.

2. **Resource Preemption**: Another way to recover from deadlock is to preempt some resources from the processes involved in the deadlock. When a resource is preempted from a process, the process is rolled back to some safe state, and the resource is allocated to another process. This method also incurs considerable overhead since the system must determine a safe state for rollback and must rollback the process to that state.

These are the two methods for recovering from deadlock in the context of CPU scheduling in operating systems. It is important to carefully consider the overhead and potential loss of work when choosing a method for deadlock recovery.