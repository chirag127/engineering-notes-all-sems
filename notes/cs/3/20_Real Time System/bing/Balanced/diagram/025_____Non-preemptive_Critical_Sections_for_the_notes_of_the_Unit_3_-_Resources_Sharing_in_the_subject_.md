### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access of shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that contains shared variables or resources that need to be synchronized to maintain the consistency of data .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of NPCS are:
  - It is simple and easy to implement.
  - It prevents deadlock, since no job is ever preempted when it holds any resource.
  - It preserves the priority order of jobs, since no job can be blocked by a lower-priority job.
- The disadvantages of NPCS are:
  - It may cause priority inversion, since a higher-priority job may have to wait for a lower-priority job to finish its critical section.
  - It may cause blocking, since a job may have to wait for a resource that is held by another job.
  - It may cause resource underutilization, since a job may hold a resource longer than necessary.
  - It may cause long response times, since a job may be delayed by the critical sections of other jobs.