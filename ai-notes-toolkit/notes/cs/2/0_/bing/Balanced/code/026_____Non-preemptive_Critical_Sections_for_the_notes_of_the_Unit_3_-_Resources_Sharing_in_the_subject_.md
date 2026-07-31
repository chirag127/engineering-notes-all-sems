### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job is ever preempted when it holds any resource.
- The disadvantages of non-preemptive critical sections are:
  - They may cause priority inversion, since a high-priority job may have to wait for a low-priority job to finish its critical section.
  - They may cause blocking, since a job may have to wait for a resource that is held by another job.
  - They may reduce the schedulability and utilization of the system, since the critical sections are executed at the highest priority and may delay other jobs.