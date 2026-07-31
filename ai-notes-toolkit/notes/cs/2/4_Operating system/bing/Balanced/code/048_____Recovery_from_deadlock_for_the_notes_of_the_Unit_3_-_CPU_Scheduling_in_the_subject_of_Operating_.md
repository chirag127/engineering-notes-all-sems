### Recovery from deadlock

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can be prevented, avoided, or detected and recovered. This topic focuses on the last method, which is deadlock detection and recovery.

Deadlock detection is the process of finding out whether a deadlock has occurred or not. This can be done by using a wait-for graph, which is a directed graph that shows which processes are waiting for which resources. A cycle in the wait-for graph indicates a deadlock.

Deadlock recovery is the process of breaking the deadlock and resuming the normal execution of the system. There are two main approaches for deadlock recovery:

- Process termination: This involves killing one or more processes involved in the deadlock to release the resources and break the cycle. There are two methods for process termination:

  - Abort all the deadlocked processes: This is the simplest and most drastic method, which ensures that the deadlock is broken, but at a high cost of losing all the work done by the processes.
  - Abort one process at a time until the deadlock is eliminated: This is a more selective and less expensive method, which tries to minimize the number of processes aborted and the amount of work lost. However, this method requires a criterion for choosing which process to abort, such as the priority, the execution time, the number of resources held, etc.

- Resource preemption: This involves taking away one or more resources from some processes and giving them to other processes to break the deadlock. There are two methods for resource preemption:

  - Preempt resources and roll back: This method takes away some resources from a process and rolls it back to a safe state, where it can restart without causing a deadlock. This method requires a mechanism for saving and restoring the state of a process, such as checkpoints or transactions.
  - Preempt resources and restart the process: This method takes away some resources from a process and restarts it from the beginning. This method does not require a mechanism for saving and restoring the state of a process, but it may cause more work to be repeated and more delays.

Deadlock detection and recovery is a dynamic and reactive approach, which allows more concurrency and flexibility in the system, but also incurs more overhead and complexity. It is suitable for systems where deadlocks are rare and the cost of prevention or avoidance is high.