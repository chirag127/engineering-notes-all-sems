### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs or tasks, especially in priority-driven systems, where higher-priority jobs may be blocked or delayed by lower-priority jobs that hold the resource.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how jobs requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion occurs when a higher-priority job is prevented from executing by a lower-priority job that holds a resource needed by the higher-priority job.
- Timing anomalies occur when a change in the execution time of a job affects the schedulability of other jobs in an unpredictable way, such as when a shorter execution time leads to a longer response time.
- Deadlock occurs when a set of jobs are waiting for each other to release resources, resulting in a circular dependency that prevents any of them from making progress.
- RAC protocols can be classified into two categories: non-preemptive and preemptive.
- Non-preemptive protocols do not allow a job to be preempted while holding a resource, such as the mutual exclusion protocol (MEP) and the priority ceiling protocol (PCP).
- Preemptive protocols allow a job to be preempted while holding a resource, such as the stack resource policy (SRP) and the multiprocessor priority ceiling protocol (MPCP).
- Non-preemptive protocols can avoid deadlock, but may suffer from priority inversion and timing anomalies.
- Preemptive protocols can avoid priority inversion and timing anomalies, but may introduce additional overhead and complexity.