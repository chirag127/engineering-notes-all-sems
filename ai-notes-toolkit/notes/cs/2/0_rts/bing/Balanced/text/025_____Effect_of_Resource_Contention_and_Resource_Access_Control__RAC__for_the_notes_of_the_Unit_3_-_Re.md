### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause priority inversion, timing anomalies, or deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, while a medium-priority task preempts the low-priority task.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted, and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, and to ensure the correctness and timeliness of tasks.
- RAC is especially important for priority-driven systems, where tasks have different levels of urgency and importance.
- RAC can be classified into two categories: non-preemptive and preemptive.
- Non-preemptive RAC means that a task that holds a resource cannot be preempted by another task until it releases the resource.
- Preemptive RAC means that a task that holds a resource can be preempted by another task, but the resource is not released until the original task resumes and finishes its critical section.
- Examples of non-preemptive RAC protocols are: non-preemptive critical sections (NPCS), priority ceiling protocol (PCP), and stack resource policy (SRP).
- Examples of preemptive RAC protocols are: preemptive critical sections (PCS), priority inheritance protocol (PIP), and immediate ceiling priority protocol (ICPP).
- Each RAC protocol has its own advantages and disadvantages, such as blocking time, response time, memory overhead, and implementation complexity.
- The choice of RAC protocol depends on the characteristics of the system, such as the number and type of resources, the number and priority of tasks, and the timing constraints.