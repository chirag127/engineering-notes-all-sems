# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, or a peripheral device.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the tasks .
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that a task that has acquired a resource cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task that holds a resource.
  - Preemptive RAC means that a task that has acquired a resource can be preempted by another task, but the resource is not released until the preempted task resumes and finishes its critical section. This may cause timing anomalies, where a higher priority task may take longer to complete due to preemption.
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive protocols: Preemptive Priority Ceiling Protocol (PPCP), Preemptive Stack Resource Policy (PSRP), Preemptive Priority Inheritance Protocol (PPIP), etc .