# Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access of shared resources in real time systems  .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- NPCS has the following properties:
  - It is simple and easy to implement .
  - It prevents deadlock, since no job is ever preempted when it holds any resource  .
  - It preserves the feasibility of the system, since the priority inversion is bounded by the length of the critical section .
  - It may cause blocking, since a lower priority job may hold a resource that a higher priority job needs .
  - It may cause priority inversion, since a higher priority job may be blocked by a lower priority job that holds a resource .
  - It may cause resource underutilization, since a job may hold a resource longer than necessary .
- NPCS can be improved by using priority inheritance or priority ceiling protocols, which reduce the blocking and priority inversion .