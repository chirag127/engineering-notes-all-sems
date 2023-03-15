### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that use fixed-priority scheduling.
- Both protocols aim to overcome the limitations of traditional semaphore-based synchronization, such as priority inversion, deadlock, and excessive blocking time.
- Priority inversion occurs when a high-priority job is blocked by a low-priority job that holds a shared resource. Deadlock occurs when two or more jobs form a circular wait for resources. Blocking time is the duration that a job has to wait for a resource to become available.
- PIP and PCP differ in their allocation rules, priority assignment rules, and deadlock prevention mechanisms.

#### Priority-Inheritance Protocol (PIP)

- PIP works as follows:
  - Each resource has a priority equal to the highest priority of any job that may access it. This is called the ceiling priority of the resource.
  - A job can lock a resource if the resource is free or if the job's priority is higher than the ceiling priority of the resource.
  - If a job is blocked by a lower-priority job that holds a resource, the blocking job inherits the priority of the blocked job until it releases the resource. This is called priority inheritance.
  - When a job releases a resource, its priority is restored to its original value, and the highest-priority blocked job that requests the resource is unblocked.
- PIP has the following properties:
  - It requires minimal support from the operating system, as it only needs to change the priority of a job dynamically.
  - It can reduce the blocking time of a high-priority job, as it can preempt a low-priority job that holds a resource.
  - It cannot prevent deadlock, as it does not check for circular waits among jobs.
  - It can cause chained blocking, as a job can be blocked by multiple lower-priority jobs that inherit higher priorities.

#### Priority-Ceiling Protocol (PCP)

- PCP works as follows:
  - Each resource has a priority equal to the highest priority of any job that may access it. This is called the ceiling priority of the resource.
  - A job can lock a resource if the resource is free and if the job's priority is higher than the ceiling priority of all the resources currently locked by other jobs. This is called the system ceiling.
  - If a job is blocked by a lower-priority job that holds a resource, the blocking job does not inherit the priority of the blocked job. Instead, it waits until the system ceiling is lower than its priority.
  - When a job releases a resource, the system ceiling is lowered to the ceiling priority of the highest-priority resource still locked by any job, and the highest-priority blocked job that requests the resource is unblocked.
- PCP has the following properties:
  - It requires more support from the operating system, as it needs to keep track of the system ceiling and the ceiling priority of each resource.
  - It can prevent deadlock, as it does not allow a circular wait among jobs to form.
  - It can also reduce the blocking time of a high-priority job, as it does not allow a low-priority job to lock a resource if it can block a higher-priority job.
  - It can avoid chained blocking, as a job can only be blocked by one lower-priority job that holds a resource.