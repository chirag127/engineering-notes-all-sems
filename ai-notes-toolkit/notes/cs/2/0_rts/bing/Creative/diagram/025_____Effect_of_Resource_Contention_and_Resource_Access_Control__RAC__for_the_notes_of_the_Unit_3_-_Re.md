Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of effect of resource contention and resource access control (RAC) for real time systems.

### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Timing anomalies occur when a change in the execution time or priority of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Some examples of RAC protocols are priority inheritance protocol, priority ceiling protocol, stack resource policy, and multiprocessor priority ceiling protocol.
- Priority inheritance protocol (PIP) is a simple protocol that eliminates unbounded priority inversion by temporarily boosting the priority of the resource-holding task to the highest priority of the tasks waiting for the resource.
- Priority ceiling protocol (PCP) is a protocol that prevents priority inversion and deadlock by assigning a priority ceiling to each resource, which is the highest priority of the tasks that can access the resource, and allowing a task to lock a resource only if its priority is higher than the priority ceiling of all the locked resources.
- Stack resource policy (SRP) is a protocol that extends PCP to dynamic priority systems, such as earliest deadline first (EDF), by using a preemption level instead of a priority to determine the resource access order.
- Multiprocessor priority ceiling protocol (MPCP) is a protocol that extends PCP to multiprocessor systems, by dividing the resources into local and global categories, and applying different rules for locking and unlocking them.