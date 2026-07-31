# Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies a shared resource, such as a variable, a file, a device, etc. .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of NPCS are:
  - It is simple to implement and understand.
  - It prevents deadlock, since no job is ever preempted when it holds any resource.
  - It preserves the temporal correctness of the system, since no job can be blocked by a lower-priority job.
- The disadvantages of NPCS are:
  - It may cause priority inversion, since a higher-priority job may have to wait for a lower-priority job to finish its critical section.
  - It may reduce the processor utilization, since a job holding a resource may not be able to use the processor effectively.
  - It may increase the response time and jitter of the jobs, since they may have to wait for an unpredictable amount of time to enter their critical sections.