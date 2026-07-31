### Recovery from deadlock

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- If a system does not use deadlock prevention or avoidance techniques, there is a possibility that a deadlock will occur.
- In order to recover from a deadlock, the operating system must perform two steps:
  - Deadlock detection: The operating system must check the system state periodically or on demand for any deadlocks .
  - Deadlock resolution: The operating system must take some actions to break the deadlock and resume the normal execution of the processes .
- There are two main approaches for deadlock resolution:
  - Process termination: The operating system can kill one or more processes involved in the deadlock to release the resources and resolve the deadlock . This approach has two methods:
    - Abort all the deadlocked processes: This method will certainly break the deadlock, but at a high cost of losing the work done by the processes.
    - Abort one process at a time until the deadlock is eliminated: This method will minimize the number of processes to be aborted, but it requires an algorithm to select which process to abort. The algorithm can be based on some criteria, such as the priority, the execution time, the number of resources, or the rollback cost of the process.
  - Resource preemption: The operating system can take away one or more resources from some processes and assign them to other processes to break the deadlock . This approach has three issues to consider:
    - Selecting a victim: The operating system must choose which process to preempt a resource from, based on some criteria, such as the priority, the execution time, the number of resources, or the rollback cost of the process.
    - Rollback: The operating system must decide how far to roll back the preempted process, either to some safe state or to the beginning.
    - Starvation: The operating system must ensure that the same process is not repeatedly preempted, which may cause starvation. A possible solution is to use aging, which increases the priority of the process as it waits longer.