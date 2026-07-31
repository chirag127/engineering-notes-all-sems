### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource .
- SBPCP has the following properties :
  - It prevents priority inversion by ensuring that a higher priority job can always preempt a lower priority job that is using a resource.
  - It prevents deadlock by ensuring that a job can only request a resource if its priority is equal to or higher than the ceiling priority of the resource.
  - It bounds the blocking time of a job by the maximum execution time of a lower priority job that can access the same resource.
  - It is optimal for fixed-priority scheduling, meaning that it can schedule any set of jobs that is schedulable by any other fixed-priority protocol.