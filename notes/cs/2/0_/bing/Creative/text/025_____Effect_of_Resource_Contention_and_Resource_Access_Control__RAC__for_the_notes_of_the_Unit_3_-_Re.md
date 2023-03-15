### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, a peripheral device, etc.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task holding a resource.
  - Preemptive RAC means that a task can be preempted by another task even if it holds a resource. This may cause timing anomalies, where a high-priority task is delayed by a low-priority task preempting a resource.
- RAC can also be classified into two types: priority-based and non-priority-based.
  - Priority-based RAC means that the priority of tasks determines the order of resource allocation and scheduling. This may cause deadlock, where two or more tasks are waiting for each other to release a resource.
  - Non-priority-based RAC means that the priority of tasks does not affect the resource allocation and scheduling. This may cause starvation, where a task is indefinitely denied access to a resource.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP): a non-preemptive, priority-based protocol that eliminates unbounded priority inversion by temporarily raising the priority of a task holding a resource to the highest priority of the tasks waiting for the resource.
  - Priority ceiling protocol (PCP): a preemptive, priority-based protocol that eliminates priority inversion and deadlock by assigning a ceiling priority to each resource and preventing a task from acquiring a resource if its priority is lower than the ceiling priority of any resource currently in use.
  - Stack resource policy (SRP): a preemptive, non-priority-based protocol that eliminates priority inversion and deadlock by maintaining a stack of tasks that have acquired or are waiting for resources and allowing a task to preempt another task only if it is higher in the stack.
  - Immediate ceiling priority protocol (ICPP): a preemptive, non-priority-based protocol that eliminates priority inversion and deadlock by assigning a ceiling priority to each resource and raising the priority of a task to the ceiling priority of the resource as soon as it acquires the resource.