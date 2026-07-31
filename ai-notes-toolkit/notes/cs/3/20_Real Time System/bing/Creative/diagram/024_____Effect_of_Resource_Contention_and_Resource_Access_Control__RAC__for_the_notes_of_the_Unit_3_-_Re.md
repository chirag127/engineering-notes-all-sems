### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task holding a resource .
  - Preemptive RAC means that a task can be preempted by another task while holding a resource, but the resource is not released until the preempted task resumes. This may cause deadlock, where two or more tasks are waiting for each other to release a resource .
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP), which eliminates unbounded priority inversion by temporarily raising the priority of the task holding the resource to the highest priority of the tasks waiting for the resource .
  - Priority ceiling protocol (PCP), which prevents deadlock and reduces blocking by assigning a priority ceiling to each resource and allowing a task to lock a resource only if its priority is higher than the priority ceiling of all the resources currently locked .
  - Stack resource policy (SRP), which reduces blocking and improves schedulability by using a stack to store the preemption levels of tasks and resources and allowing a task to lock a resource only if its preemption level is higher than the preemption level of the resource .
  - Multiprocessor priority ceiling protocol (MPCP), which extends PCP to multiprocessor systems by using a global priority ceiling and a local priority ceiling for each processor .
  - Multiprocessor stack resource policy (MSRP), which extends SRP to multiprocessor systems by using a global stack and a local stack for each processor .