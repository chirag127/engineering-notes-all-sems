# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource. This may cause blocking or priority inversion, but it avoids timing anomalies and deadlock.
  - Preemptive RAC means that a task can be preempted by another task even if it holds a resource, but the resource is not released until the preempted task resumes. This may cause timing anomalies or deadlock, but it avoids blocking and priority inversion.
- Some examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc.
  - Preemptive RAC: Wait-Free Protocol (WFP), Abort-and-Restart Protocol (ARP), etc.