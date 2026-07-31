### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource.
- SBPCP has two rules: a scheduling rule and an allocation rule.
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time.
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that a job will not be blocked by a lower priority job that holds a resource, and that a job will not be blocked by more than m-1 higher priority jobs, where m is the number of resources in the system.
- SBPCP also guarantees that there will be no deadlock, since a circular wait among jobs is impossible.
- SBPCP is similar to the Original Ceiling Priority Protocol (OCPP), but it differs in that it allows a job to request multiple resources at the same time, and it does not require a job to release all its resources before requesting a new one.
- SBPCP is also similar to the Immediate Ceiling Priority Protocol (ICPP), but it differs in that it does not raise the priority of a job until it requests a resource, and it does not lower the priority of a job until it releases all its resources.
- SBPCP has the same worst-case behavior as OCPP and ICPP from a scheduling viewpoint, but it may have better average-case performance and lower overhead.