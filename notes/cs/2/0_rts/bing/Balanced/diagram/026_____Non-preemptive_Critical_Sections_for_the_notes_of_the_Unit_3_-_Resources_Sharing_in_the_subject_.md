### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access to shared resources in real-time systems .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- NPCS has the following properties:
  - Mutual exclusion: No two jobs can access the same resource at the same time.
  - Deadlock-free: No job can be blocked indefinitely by another job holding a resource.
  - Priority inversion-free: No job can be preempted by a lower-priority job while holding a resource.
  - Bounded blocking: The maximum blocking time of a job is bounded by the longest critical section of any job.
- NPCS can be implemented by using a global lock variable that indicates whether any resource is in use or not. A job that wants to enter a critical section must first check the lock variable and wait until it is free. Then, it sets the lock variable to indicate that a resource is in use and raises its priority to the highest level. After exiting the critical section, it restores its original priority and clears the lock variable .
- NPCS has some advantages and disadvantages:
  - Advantages:
    - Simplicity: NPCS is easy to implement and understand.
    - Efficiency: NPCS does not require any additional data structures or overheads for managing resources.
    - Robustness: NPCS can handle any number of resources and jobs without causing deadlock or priority inversion.
  - Disadvantages:
    - Utilization: NPCS can reduce the processor utilization by delaying the execution of lower-priority jobs that do not need any resources.
    - Responsiveness: NPCS can increase the response time of higher-priority jobs that are blocked by lower-priority jobs holding resources.
    - Fairness: NPCS can cause starvation of lower-priority jobs that are repeatedly blocked by higher-priority jobs holding resources.