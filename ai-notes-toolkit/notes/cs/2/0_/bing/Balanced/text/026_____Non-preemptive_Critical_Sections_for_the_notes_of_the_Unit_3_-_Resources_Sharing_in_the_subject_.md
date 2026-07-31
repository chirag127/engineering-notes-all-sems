### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- This protocol ensures that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of non-preemptive critical sections are:
  - Simplicity: no need for complex synchronization mechanisms or priority inheritance schemes .
  - Deadlock-freedom: no job can be blocked indefinitely by another job holding a resource  .
- The disadvantages of non-preemptive critical sections are:
  - Priority inversion: a high-priority job may have to wait for a low-priority job to finish its critical section before accessing the same resource .
  - Resource underutilization: a job holding a resource may not use it for the entire duration of its critical section, wasting processor time and delaying other jobs .
  - Response time unpredictability: the worst-case response time of a job depends on the length and number of critical sections of all other jobs, which may be hard to analyze or bound .