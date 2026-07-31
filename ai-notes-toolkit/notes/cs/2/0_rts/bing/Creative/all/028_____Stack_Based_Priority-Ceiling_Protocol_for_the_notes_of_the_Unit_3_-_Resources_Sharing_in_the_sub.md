# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked until the resource is released by the current owner .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the worst-case execution time of the highest priority job that can access any of the resources needed by the blocked job .
- SBPCP also prevents deadlock by ensuring that a job cannot request a resource that is already held by a lower priority job, and that a job cannot request a resource that has a lower ceiling priority than any of the resources it already holds .
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them. It requires a priori knowledge of the ceiling priorities of the resources and the resource requests of the jobs .
- SBPCP is also known as the Original Ceiling Priority Protocol (OCPP) or the Highest Locker Protocol (HLP).