### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a processor, a memory, a disk, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs or tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how jobs or tasks requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the system.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a job or task acquires a resource, it cannot be interrupted or preempted by another job or task until it releases the resource.
  - Preemptive RAC means that a job or task holding a resource can be interrupted or preempted by another job or task with higher priority or urgency, and the resource can be transferred or shared among them.
- Some examples of non-preemptive RAC are: no access control, priority ceiling protocol, stack-based protocol, and priority inheritance protocol.
- Some examples of preemptive RAC are: immediate ceiling protocol, preemptive ceiling protocol, and slack-based protocol.