# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section.
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - Simplicity: The protocol is easy to implement and understand, and does not require any complex data structures or algorithms.
  - Deadlock-freedom: The protocol guarantees that no deadlock can occur, since no job is ever blocked or waiting for a resource held by another job.
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: The protocol may cause a high-priority job to be delayed by a low-priority job that holds a resource, which violates the real-time scheduling principle.
  - Resource underutilization: The protocol may waste processor time by preventing other jobs from executing while a job holds a resource, even if the resource is not needed by the job at that moment.
  - Unbounded blocking: The protocol may cause a job to be blocked for an indefinite amount of time by a job that holds a resource, depending on the length of the critical section and the arrival pattern of other jobs.