### Recovery from Deadlock

Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. To recover from deadlock, there are two methods:

1. **Process Termination**: One way to eliminate deadlock is to abort one or more processes to break the circular wait. There are two methods to abort processes:
    - Abort all deadlocked processes: This method will break the deadlock cycle, but it is costly as it will result in the loss of all the work done by the processes.
    - Abort one process at a time until the deadlock cycle is eliminated: This method is less expensive, but it requires a careful selection of which process to abort.

2. **Resource Preemption**: Another way to eliminate deadlock is to preempt some resources from the processes and give them to other processes. This method also requires a careful selection of which resources to preempt and from which processes. The selection criteria may include the cost of preemption, the amount of time the resource has been held, and the priority of the process holding the resource.

These are the two methods to recover from deadlock in the context of CPU scheduling in operating systems. It is important to carefully consider the selection criteria when choosing which method to use and which processes or resources to terminate or preempt.