# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule  .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time  .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, the job is blocked and its priority is raised to the ceiling priority of the resource  .
- SBPCP guarantees that a job can be blocked by at most one lower-priority job, and that the blocking time is bounded by the maximum execution time of the blocking job  .
- SBPCP also prevents deadlock by ensuring that a job can only request a resource if its priority is higher than the ceiling priority of any other resource that it holds  .
- SBPCP is an improvement over the Priority Inheritance Protocol (PIP), which only raises the priority of a job when it is blocked by a lower-priority job, and does not prevent deadlock .
- SBPCP is also an improvement over the Original Ceiling Priority Protocol (OCPP), which raises the priority of a job to the ceiling priority of the resource as soon as it requests the resource, even if the resource is available .
- SBPCP is similar to the Immediate Ceiling Priority Protocol (ICPP), which also raises the priority of a job to the ceiling priority of the resource when it requests the resource, but only if the resource is unavailable .
- SBPCP, OCPP, and ICPP have the same worst-case behavior from a scheduling point of view, but SBPCP and ICPP have better average-case behavior than OCPP, as they reduce the number of priority changes and context switches .