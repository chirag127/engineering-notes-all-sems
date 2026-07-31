### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked until the resource is released by the current owner .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the maximum execution time of a critical section of a lower priority job .
- SBPCP also prevents deadlock by ensuring that a job cannot request a resource that has a lower ceiling priority than any resource it already holds .
- SBPCP can be implemented using a shared stack for all the jobs, where each entry in the stack contains the job identifier, the resource identifier, and the original priority of the job. The stack is updated whenever a job requests or releases a resource, and the current ceiling of the system is the ceiling priority of the resource at the top of the stack .
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them. It requires a priori knowledge of the ceiling priorities of the resources and the execution times of the critical sections .
- SBPCP is an improvement over the Priority Inheritance Protocol (PIP), which only raises the priority of a job when it is blocked by a lower priority job. SBPCP avoids unnecessary priority inheritance and reduces the number of context switches and the length of priority inversion .