### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access to shared resources in real-time systems .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- NPCS ensures mutual exclusion and prevents deadlock, since no job can be preempted while holding a resource .
- NPCS also preserves the priority order of jobs, since a higher-priority job can only be blocked by a lower-priority job that has already acquired the resource .
- NPCS has some drawbacks, such as:
  - It may cause priority inversion, where a higher-priority job is blocked by a lower-priority job for an indefinite time .
  - It may cause blocking time to be unbounded, since a lower-priority job may hold a resource for a long time before releasing it .
  - It may cause resource utilization to be low, since a resource may be idle while a higher-priority job is waiting for it .
  - It may cause response time analysis to be complex, since the blocking time depends on the execution time of the lower-priority jobs .

- A diagram to illustrate NPCS is shown below:

```
+------------------+------------------+------------------+------------------+
| Job 1 (High)     | Job 2 (Medium)   | Job 3 (Low)      | Resource R       |
+------------------+------------------+------------------+------------------+
| Request R        |                  |                  |                  |
+------------------+------------------+------------------+------------------+
| Acquire R        |                  |                  | Allocated to J1  |
+------------------+------------------+------------------+------------------+
| Execute CS       |                  |                  |                  |
+------------------+------------------+------------------+------------------+
| Release R        |                  |                  | Available        |
+------------------+------------------+------------------+------------------+
| Execute          | Request R        |                  |                  |
+------------------+------------------+------------------+------------------+
|                  | Acquire R        |                  | Allocated to J2  |
+------------------+------------------+------------------+------------------+
|                  | Execute CS       |                  |                  |
+------------------+------------------+------------------+------------------+
|                  | Release R        |                  | Available        |
+------------------+------------------+------------------+------------------+
|                  | Execute          | Request R        |                  |
+------------------+------------------+------------------+------------------+
|                  |                  | Acquire R        | Allocated to J3  |
+------------------+------------------+------------------+------------------+
|                  |                  | Execute CS       |                  |
+------------------+------------------+------------------+------------------+
|                  |                  | Release R        | Available        |
+------------------+------------------+------------------+------------------+
|                  |                  | Execute          |                  |
+------------------+------------------+------------------+------------------+
```

- In the diagram, CS stands for critical section, J1, J2, and J3 are the jobs, and R is the resource.
- The diagram shows that each job acquires the resource when it requests it, and executes its critical section non-preemptively.
- The diagram also shows that J1 blocks J2, and J2 blocks J3, until they release the resource. This causes priority inversion and unbounded blocking time.