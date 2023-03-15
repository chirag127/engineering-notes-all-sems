### Recovery from deadlock

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- If a system does not use a deadlock prevention or avoidance technique, there is a possibility that a deadlock will occur.
- In order to recover from a deadlock, the operating system must detect and resolve it using some methods.
- There are two main approaches for deadlock recovery: process termination and resource preemption.

#### Process termination

- To eliminate the deadlock, we can simply kill one or more processes involved in the deadlock.
- For this, we use two methods:

  - Abort all the deadlocked processes: This method will certainly break the deadlock, but at a great expense. The processes may have done some useful work before entering the deadlock, and aborting them will lose that work. Also, this method may not be feasible if the processes are critical or interactive.
  - Abort one process at a time until the deadlock cycle is eliminated: This method is more selective and tries to minimize the cost of aborting processes. However, it requires some criteria to choose which process to abort, such as the priority, the amount of resources and time consumed, the number of resources the process needs to finish, etc. Also, this method may not work if a deadlock occurs again after aborting a process.

#### Resource preemption

- To eliminate the deadlock, we can preempt some resources from the processes involved in the deadlock and allocate them to other processes.
- For this, we use three methods:

  - Preempt resources and rollback: This method takes away some resources from a process and restarts it from some previous checkpoint. The process may lose some work, but not as much as aborting it. However, this method requires the system to have a mechanism for checkpointing and rollback, and it may cause starvation if the same process is always preempted.
  - Preempt resources and restart: This method takes away some resources from a process and restarts it from the beginning. The process will lose all its work, but it may be simpler than rollback. However, this method may also cause starvation if the same process is always preempted.
  - Preempt resources and wait: This method takes away some resources from a process and puts it in a waiting state until it can regain its resources. The process will not lose any work, but it may increase the waiting time and the system overhead. Also, this method may not work if a deadlock occurs again after preempting a resource.