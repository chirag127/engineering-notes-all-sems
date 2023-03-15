### Preemption Ceiling Protocol

- Preemption ceiling protocol is a resource access control protocol for real-time systems that use fixed priority scheduling.
- The protocol assigns a preemption ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the preemption ceiling of all the resources currently locked by other tasks.
- This ensures that a task is never blocked by a lower priority task, and prevents deadlock and chained blocking.
- The protocol also raises the priority of a task that locks a resource to the preemption ceiling of that resource, to prevent preemption by unrelated higher priority tasks.
- The protocol guarantees that the blocking time of a task is at most the execution time of the critical section of the highest priority task that shares a resource with it.
- The protocol can be implemented statically or dynamically, depending on whether the preemption ceilings are assigned at design time or run time.