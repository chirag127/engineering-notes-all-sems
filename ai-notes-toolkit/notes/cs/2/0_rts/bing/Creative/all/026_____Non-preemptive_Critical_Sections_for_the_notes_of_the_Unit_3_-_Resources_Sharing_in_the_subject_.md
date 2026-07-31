# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that contains shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- Non-preemptive critical sections have the following properties :
  - When a job requests a resource, it is always allocated the resource.
  - When a job holds any resource, it executes at a priority higher than the priorities of all other jobs.
  - Because no job is ever preempted when it holds any resource, deadlock can never occur.
- Non-preemptive critical sections have some advantages and disadvantages :
  - Advantages:
    - Simplicity: no need for complex synchronization mechanisms or protocols.
    - Efficiency: no overhead of context switching or blocking.
    - Safety: no possibility of deadlock or priority inversion.
  - Disadvantages:
    - Conservativeness: a job may hold a resource longer than necessary, preventing other jobs from accessing it.
    - Unfairness: a job may be delayed indefinitely by higher-priority jobs that keep requesting the same resource.
    - Non-optimality: the worst-case response time of a job may be increased by the non-preemptive execution of critical sections.