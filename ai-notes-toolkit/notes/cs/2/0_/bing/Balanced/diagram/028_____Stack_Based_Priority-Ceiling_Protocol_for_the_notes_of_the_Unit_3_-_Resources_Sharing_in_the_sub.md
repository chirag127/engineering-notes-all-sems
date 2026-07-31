### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share a common run-time stack and other resources.
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a ceiling priority to each resource and blocks a job from executing if its priority is lower than the current ceiling of the system .
- SBPCP differs from OCPP in two ways :
  - SBPCP assigns a ceiling priority to each resource based on the highest priority of the jobs that request it, rather than the highest priority of the jobs that can access it.
  - SBPCP uses a stack to store the ceiling priorities of the resources that are in use, and updates the current ceiling of the system based on the top of the stack.
- SBPCP has the following rules :
  - Scheduling Rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system.
  - Allocation Rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is higher than the current ceiling of the system. Otherwise, it is blocked and its priority is pushed onto the stack.
  - Deallocation Rule: Whenever a job releases a resource, it pops its priority from the stack and restores its original priority.
- SBPCP has the following properties :
  - SBPCP prevents deadlock, as a job can only request a resource if its priority is higher than the current ceiling of the system, which is the highest priority of the resources that are in use.
  - SBPCP prevents unbounded priority inversion, as a job can only be blocked by lower priority jobs that are using resources with higher ceiling priorities, and the blocking time is bounded by the execution time of the critical sections of those jobs.
  - SBPCP is optimal for fixed priority scheduling, as it ensures that the highest priority job that is ready to execute is always scheduled.