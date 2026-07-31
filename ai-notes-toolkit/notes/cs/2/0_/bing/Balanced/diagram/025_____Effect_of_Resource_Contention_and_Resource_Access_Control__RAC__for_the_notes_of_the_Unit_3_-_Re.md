### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention on the execution behavior and schedulability of tasks.
- Some of the undesirable effects of resource contention are:
  - Priority inversion: when a high-priority task is blocked by a low-priority task that holds a resource .
  - Timing anomalies: when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way.
  - Deadlock: when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- Some of the RAC protocols that are used to reduce or eliminate these effects are:
  - Priority inheritance protocol: when a low-priority task holds a resource that is requested by a high-priority task, the low-priority task inherits the priority of the high-priority task until it releases the resource .
  - Priority ceiling protocol: when a task requests a resource, it is assigned a priority equal to the highest priority of any task that may request the same resource, and it cannot be preempted by any other task with lower priority .
  - Stack resource policy: when a task requests a resource, it is assigned a priority equal to the highest priority of any task that has requested a resource before it, and it cannot be preempted by any other task with lower priority.