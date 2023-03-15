### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple jobs compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs, especially in priority-driven systems.
- Resource contention can cause undesirable effects such as:
  - Priority inversion: when a high-priority job is blocked by a low-priority job that holds a resource.
  - Timing anomalies: when a change in the execution time of a job affects the schedulability of other jobs in an unpredictable way.
  - Deadlock: when a set of jobs are waiting for each other to release resources, resulting in a circular dependency.
- Resource access control (RAC) is a set of rules that govern:
  - When and under what conditions each request for a resource is granted.
  - How jobs requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention and ensure the feasibility of the schedule.
- RAC can be classified into two categories:
  - Non-preemptive RAC: when a job that holds a resource cannot be preempted by another job until it releases the resource.
  - Preemptive RAC: when a job that holds a resource can be preempted by another job, but the resource is not released until the preempted job resumes and finishes its critical section.
- Examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), etc.
  - Preemptive RAC: Priority Inheritance Protocol (PIP), Slack Inheritance Protocol (SIP), etc.