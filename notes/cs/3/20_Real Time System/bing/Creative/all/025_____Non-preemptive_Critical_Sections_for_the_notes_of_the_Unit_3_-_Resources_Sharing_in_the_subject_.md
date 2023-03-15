# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job is ever preempted when it holds any resource.
  - They preserve the temporal correctness of the system, since no job can miss its deadline due to blocking by a lower-priority job.
- The disadvantages of non-preemptive critical sections are:
  - They can cause priority inversion, where a higher-priority job is blocked by a lower-priority job that holds a resource.
  - They can reduce the processor utilization, since a job holding a resource may not use the processor fully while blocking other jobs.
  - They can increase the response time and jitter of the system, since a job may have to wait for a long time before entering a critical section.