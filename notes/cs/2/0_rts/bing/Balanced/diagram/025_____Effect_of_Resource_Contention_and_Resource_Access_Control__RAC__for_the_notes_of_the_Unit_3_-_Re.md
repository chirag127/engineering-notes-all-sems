### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way, such as when a shorter execution time leads to a longer response time.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP), which assigns the highest priority of the blocked tasks to the task that holds the resource, and restores the original priority when the resource is released.
  - Priority ceiling protocol (PCP), which assigns a ceiling priority to each resource, and prevents a task from locking a resource if its priority is lower than the ceiling priority of any locked resource.
  - Stack resource policy (SRP), which assigns a preemption level to each task, and prevents a task from locking a resource if its preemption level is lower than the preemption level of any locked resource.
  - Multiprocessor priority ceiling protocol (MPCP), which extends PCP to multiprocessor systems, and allows tasks to migrate between processors while holding resources.
  - Multiprocessor stack resource policy (MSRP), which extends SRP to multiprocessor systems, and requires tasks to release resources before migrating between processors.