### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules :
  - Scheduling Rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at the time.
  - Allocation Rule: Whenever a job requests a resource, it is allocated the resource if it is free and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that :
  - No deadlock can occur, since a job can only request a resource with a ceiling priority equal to or higher than its own priority, and a lower priority job cannot block a higher priority job from accessing a resource.
  - The maximum blocking time for any job is equal to the execution time of one critical section with the highest ceiling priority among all the resources accessed by the job.
  - The priority inversion problem is minimized, since a job can only be blocked by a lower priority job that holds a resource with a ceiling priority equal to or higher than its own priority, and the blocking time is bounded by the critical section length.