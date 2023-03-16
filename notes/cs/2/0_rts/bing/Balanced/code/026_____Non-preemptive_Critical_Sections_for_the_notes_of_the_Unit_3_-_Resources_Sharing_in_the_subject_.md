### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- When a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs. This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, since no job is ever preempted when it holds any resource .
- The disadvantages of NPCS are:
  - It may cause priority inversion, which means that a high-priority job may be blocked by a low-priority job that holds a resource .
  - It may cause blocking, which means that a job may have to wait for a resource that is held by another job .
  - It may cause long response times and low utilization of the processor .