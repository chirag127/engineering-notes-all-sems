### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- When a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, as no job is ever preempted when it holds any resource  .
  - It preserves the order of resource requests, as no job can jump ahead of another job that is waiting for the same resource .
- The disadvantages of NPCS are:
  - It may cause priority inversion, as a high-priority job may be blocked by a low-priority job that is holding a resource .
  - It may cause resource underutilization, as a resource may be idle while a job that is holding it is executing a non-critical section .
  - It may cause long response times, as a job may have to wait for a long time to access a resource that is held by another job .