### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource.
- SBPCP has two rules: a scheduling rule and an allocation rule.
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time.
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the blocking time of a job is at most the execution time of one critical section of a higher priority job.
- SBPCP also prevents deadlock, since a job can only request a resource if its priority is equal to the ceiling priority of the resource, and the ceiling priorities are assigned in a non-decreasing order.
- SBPCP is an improvement over the Original Ceiling Priority Protocol (OCPP) and the Immediate Ceiling Priority Protocol (ICPP), which are two variants of the Priority Ceiling Protocol (PCP) that work by temporarily raising the priorities of jobs that access resources.
- SBPCP reduces the number of priority changes and context switches compared to OCPP and ICPP, and also allows for dynamic priority assignment of jobs.
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them.