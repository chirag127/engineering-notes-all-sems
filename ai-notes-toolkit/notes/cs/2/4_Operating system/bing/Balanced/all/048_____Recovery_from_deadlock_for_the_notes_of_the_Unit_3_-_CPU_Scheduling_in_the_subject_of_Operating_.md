# Recovery from deadlock

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- If a system does not use deadlock prevention or avoidance techniques, it may encounter a deadlock situation.
- In order to recover from a deadlock, the system must detect it and then apply some methods to resolve it.
- There are two main approaches for deadlock recovery:

  - Process termination: This method involves killing one or more processes involved in the deadlock to release the resources and resume the normal operation of the system. There are two ways to do this:

    - Abort all the deadlocked processes: This is the simplest way to break the deadlock, but it may incur a high cost in terms of lost work and resources.
    - Abort one process at a time until the deadlock is eliminated: This is a more selective way to break the deadlock, but it requires a criterion to choose which process to abort. Some possible criteria are:

      - Process priority: Abort the process with the lowest priority.
      - Resource utilization: Abort the process with the least number of resources.
      - Process execution time: Abort the process that has executed the least amount of time.
      - Process progress: Abort the process that is the least likely to finish soon.

  - Resource preemption: This method involves taking away some resources from one or more processes involved in the deadlock and giving them to other processes, so that the deadlock is broken and the system can continue. There are some issues to consider when applying this method:

    - Which resources and which processes are to be preempted?
    - How to ensure that the preemption does not cause starvation or inconsistency?
    - How to resume the preempted processes after the deadlock is resolved?

- Some possible solutions for these issues are:

  - Preempt the resources from the processes with the lowest priority or the least number of resources.
  - Preempt the resources that can be easily saved and restored, such as CPU registers or memory pages.
  - Preempt the resources that are not essential for the process to continue, such as printer or tape drives.
  - Rollback the preempted processes to a safe state and restart them with the new resource allocation.
  - Use a compensation mechanism to avoid starvation, such as giving priority or extra resources to the preempted processes.