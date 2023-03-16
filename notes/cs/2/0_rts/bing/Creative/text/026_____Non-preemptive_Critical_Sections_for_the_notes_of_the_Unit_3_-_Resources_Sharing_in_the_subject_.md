### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of non-preemptive critical sections are:
  - Simplicity: no need for complex locking or signaling mechanisms to protect the critical sections .
  - Deadlock-freedom: no job can be blocked by another job holding a resource, so deadlock can never occur  .
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: a high-priority job may be delayed by a low-priority job that is executing a critical section .
  - Resource underutilization: a job holding a resource may not use it for the entire duration of the critical section, wasting the resource and delaying other jobs that need it .
  - Unbounded blocking: a job may be blocked for an indefinite amount of time by another job that is executing a long or unbounded critical section .