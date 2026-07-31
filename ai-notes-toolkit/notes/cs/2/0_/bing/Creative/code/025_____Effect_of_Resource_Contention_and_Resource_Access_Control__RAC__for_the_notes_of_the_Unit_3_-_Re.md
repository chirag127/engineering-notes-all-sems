# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, a peripheral device, etc.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, deadlock, and reduced schedulability.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, while a medium-priority task preempts the low-priority task.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- Reduced schedulability means that some tasks may miss their deadlines due to resource contention and blocking time.

## RAC Protocols

- There are different RAC protocols that aim to prevent or limit the effects of resource contention, such as:
  - Non-preemptive critical sections (NPCS): A task cannot be preempted while executing a critical section, but it can be preempted before or after it. This prevents priority inversion, but may cause long blocking time and reduced schedulability.
  - Priority inheritance protocol (PIP): A task that holds a resource inherits the highest priority of the tasks that are blocked by it. This limits the priority inversion to one level, but may cause deadlock and timing anomalies.
  - Priority ceiling protocol (PCP): A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks. The ceiling priority of a resource is the highest priority of any task that may lock it. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Stack resource policy (SRP): A task can lock a resource only if its preemption level is higher than the system ceiling, which is the highest preemption level of all the resources currently locked by other tasks. The preemption level of a task is determined by the order of its arrival. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Multiprocessor priority ceiling protocol (MPCP): A generalization of PCP for multiprocessor systems, where each processor has its own ceiling priority and a task can migrate to another processor if it is blocked by a lower priority task. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.
  - Multiprocessor stack resource policy (MSRP): A generalization of SRP for multiprocessor systems, where each processor has its own system ceiling and a task can migrate to another processor if it is blocked by a lower priority task. This prevents deadlock and limits the blocking time, but may cause timing anomalies and reduced schedulability.