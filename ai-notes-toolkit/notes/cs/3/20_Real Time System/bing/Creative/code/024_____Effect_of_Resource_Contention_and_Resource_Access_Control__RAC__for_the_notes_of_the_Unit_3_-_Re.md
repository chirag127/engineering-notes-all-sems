Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of effect of resource contention and resource access control (RAC) for real time systems.

### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel .
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks .
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task holding a resource .
  - Preemptive RAC means that a task can be preempted by another task even if it holds a resource. This may cause timing anomalies, where a high-priority task is delayed by a low-priority task preempting a resource .
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP), which eliminates unbounded priority inversion by temporarily raising the priority of the task holding the resource to the highest priority of the tasks waiting for the resource .
  - Priority ceiling protocol (PCP), which prevents deadlock and bounded priority inversion by assigning a priority ceiling to each resource and allowing a task to lock a resource only if its priority is higher than the priority ceiling of all the resources currently locked .
  - Stack resource policy (SRP), which reduces blocking time and memory requirements by using a stack to store the preemption levels of the tasks and allowing a task to lock a resource only if its preemption level is higher than the preemption level of the task at the top of the stack .