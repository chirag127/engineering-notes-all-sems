# Recovery from deadlock

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- If a system does not use a deadlock prevention or avoidance technique, there is a possibility that a deadlock will occur.
- In order to recover from a deadlock, the operating system must perform two steps:
  - Deadlock detection: The operating system must check the system state periodically or on demand to determine if a deadlock has occurred.
  - Deadlock resolution: The operating system must take some actions to break the deadlock and resume normal operation.
- There are two main approaches to deadlock resolution:
  - Process termination: The operating system can kill one or more processes involved in the deadlock to release the resources and resolve the deadlock. This can be done in two ways:
    - Abort all the deadlocked processes: This is the simplest and most expensive method, as it may result in losing some important work or data.
    - Abort one process at a time until the deadlock is eliminated: This is a more selective and less costly method, but it requires some criteria to choose which process to abort, such as the priority, the execution time, the number of resources, etc.
  - Resource preemption: The operating system can temporarily take away some resources from the processes involved in the deadlock and assign them to other processes, and then restore them later when the deadlock is resolved. This can be done in two ways:
    - Preempt resources and rollback: The operating system can rollback the state of the preempted process to some safe point and restart it from there. This requires the system to keep track of the process state and the resource allocation history.
    - Preempt resources and restart: The operating system can restart the preempted process from the beginning. This does not require the system to keep track of the process state, but it may result in repeating some work or losing some data.