### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP): A low-priority task that holds a resource inherits the priority of the highest-priority task that is blocked by it, until it releases the resource.
  - Priority ceiling protocol (PCP): A task can lock a resource only if its priority is higher than the ceiling of the resource, which is the highest priority of any task that can access the resource. A task that locks a resource inherits the ceiling of the resource, until it releases the resource.
  - Stack resource policy (SRP): A task can lock a resource only if its preemption level, which is assigned based on the resource usage, is higher than the system ceiling, which is the highest preemption level of any locked resource. A task that locks a resource raises the system ceiling to its preemption level, until it releases the resource.