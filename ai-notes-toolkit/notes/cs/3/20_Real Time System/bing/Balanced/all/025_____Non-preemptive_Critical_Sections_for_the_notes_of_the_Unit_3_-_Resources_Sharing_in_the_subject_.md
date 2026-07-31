Hello, I am Sydney, your AI assistant. I can help you with your query.

# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, regardless of their original priorities  .
- This protocol ensures mutual exclusion, deadlock-freedom, and bounded blocking time for all jobs .
- However, it also has some disadvantages, such as:
  - It may cause priority inversion, where a high-priority job is blocked by a low-priority job that holds a resource .
  - It may cause unnecessary blocking, where a job is blocked by another job that does not access the same resource .
  - It may cause long blocking time, where a job is blocked by another job that executes a long critical section .
  - It may cause low processor utilization, where a job that holds a resource does not use the processor effectively .
- Therefore, non-preemptive critical sections are only suitable for systems that have short and infrequent critical sections, and where the priority of jobs is not very important .