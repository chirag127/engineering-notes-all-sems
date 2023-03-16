# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, regardless of their original priorities  .
- This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, as no job is ever blocked or waiting for a resource held by another job  .
- The disadvantages of NPCS are:
  - It may cause priority inversion, as a high-priority job may be delayed by a low-priority job that holds a resource .
  - It may cause resource underutilization, as a resource may be idle while a job that holds it is executing non-critical sections .
  - It may cause long blocking times, as a job may have to wait for the completion of a long critical section by another job .
  - It may not be applicable to some resources that cannot be allocated non-preemptively, such as interrupts or communication channels .