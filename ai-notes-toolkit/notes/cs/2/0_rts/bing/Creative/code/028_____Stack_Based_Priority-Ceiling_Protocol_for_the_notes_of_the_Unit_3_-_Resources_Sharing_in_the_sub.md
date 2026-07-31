### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule  .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, the job is blocked and its priority is raised to the ceiling priority of the resource .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the maximum execution time of a critical section of a lower priority job  .
- SBPCP also prevents deadlock by ensuring that a job can only request a resource if its priority is higher than the ceiling priority of any other resource that it already holds  .
- SBPCP is similar to the Original Ceiling Priority Protocol (OCPP), but differs in the way the ceiling priority of the system is updated. In OCPP, the ceiling priority of the system is the highest ceiling priority of all the resources in the system, regardless of whether they are in use or not. In SBPCP, the ceiling priority of the system is the highest ceiling priority of only the resources that are in use.
- SBPCP has the same worst-case behavior as OCPP from a scheduling point of view, but it may reduce the number of context switches and the overhead of priority changes.