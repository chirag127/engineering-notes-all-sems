### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a processor, a memory, a device, or a communication channel .
- Resource contention affects the execution behavior and schedulability of jobs or tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how jobs or tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the real-time system  .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that once a job or task acquires a resource, it cannot be preempted by another job or task until it releases the resource .
  - Preemptive RAC means that a job or task can be preempted by another job or task with higher priority while holding a resource, and resume the resource when it resumes execution .
- Some examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive RAC: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Multiprocessor Priority Inheritance Protocol (MPIP), etc .
- The choice of RAC protocol depends on the characteristics of the real-time system, such as the number and type of resources, the number and type of jobs or tasks, the priority assignment, the scheduling algorithm, the system architecture, etc .
- The performance of RAC protocols can be evaluated by metrics such as blocking time, response time, schedulability, utilization, overhead, etc .