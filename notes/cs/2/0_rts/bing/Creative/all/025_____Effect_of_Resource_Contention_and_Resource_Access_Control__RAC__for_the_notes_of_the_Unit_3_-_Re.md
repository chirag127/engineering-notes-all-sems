# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, or a peripheral device .
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the tasks .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource .
  - Preemptive RAC means that a task can be preempted by another task while holding a resource, but the resource is not released until the preempted task resumes and finishes its critical section .
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive protocols: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Preemptive Priority Inheritance Protocol (PPIP), etc .