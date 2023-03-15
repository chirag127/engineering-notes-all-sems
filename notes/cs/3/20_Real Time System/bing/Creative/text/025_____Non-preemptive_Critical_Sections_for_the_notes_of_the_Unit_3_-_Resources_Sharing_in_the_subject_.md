### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job can be blocked by another job holding a resource.
- The disadvantages of non-preemptive critical sections are:
  - They can cause priority inversion, since a high-priority job may have to wait for a low-priority job to finish its critical section.
  - They can reduce the schedulability of the system, since the worst-case execution time of a job may increase due to the non-preemptive execution of critical sections.
  - They can violate the temporal isolation principle, since the execution time of a job may depend on the behavior of other jobs in the system.