### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share a common run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a ceiling priority to each resource and raises the priority of a job that accesses a resource to the ceiling priority of that resource .
- SBPCP differs from OCPP in two ways :
  - SBPCP uses a scheduling rule that blocks a job from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at any time .
  - SBPCP uses an allocation rule that allows a job to access a resource only if its assigned priority is higher than the ceiling priority of all the resources that are currently in use, except the ones that are already allocated to the job .
- SBPCP has the following properties   :
  - SBPCP prevents deadlock, as a job cannot request a resource that is already allocated to a lower-priority job .
  - SBPCP prevents unbounded priority inversion, as a job cannot be blocked by a lower-priority job for more than the duration of one critical section .
  - SBPCP is optimal for fixed-priority scheduling, as it guarantees that a feasible schedule exists if the system is schedulable under the Rate Monotonic (RM) or Deadline Monotonic (DM) algorithms .
  - SBPCP reduces the memory demand, as it allows jobs to share a common run-time stack and other resources .
- SBPCP can be illustrated by the following example :

  - Assume there are three jobs J1, J2, and J3 with priorities 3, 2, and 1 respectively, and two resources R1 and R2 with ceiling priorities 2 and 3 respectively.
  - The following table shows the execution sequence of the jobs and the resource requests and releases:

| Time | Job | Action | Current Ceiling | Comment |
|------|-----|--------|-----------------|---------|
| 0    | J1  | Start  | 0               | J1 is the highest-priority job and can start execution |
| 1    | J1  | Request R1 | 2             | J1's priority is raised to 2, the ceiling priority of R1 |
| 2    | J2  | Start  | 2               | J2 is blocked by the current ceiling and cannot start execution |
| 3    | J1  | Request R2 | 3             | J1's priority is raised to 3, the ceiling priority of R2 |
| 4    | J1  | Release R1 | 3             | J1's priority remains 3, the current ceiling of the system |
| 5    | J1  | Release R2 | 0             | J1's priority is restored to 3, the current ceiling is 0 |
| 6    | J1  | Finish  | 0               | J1 completes its execution |
| 7    | J2  | Start  | 0               | J2 can start execution as its priority is higher than the current ceiling |
| 8    | J2  | Request R1 | 2             | J2's priority is raised to 2, the ceiling priority of R1 |
| 9    | J3  | Start  | 2               | J3 is blocked by the current ceiling and cannot start execution |
| 10   | J2  | Release R1 | 0             | J2's priority is restored to 2, the current ceiling is 0 |
| 11   | J2  | Finish  | 0               | J2 completes its execution |
| 12   | J3  | Start  | 0               | J3 can start execution as its priority is higher than the current ceiling |
| 13   | J3  | Finish  | 0