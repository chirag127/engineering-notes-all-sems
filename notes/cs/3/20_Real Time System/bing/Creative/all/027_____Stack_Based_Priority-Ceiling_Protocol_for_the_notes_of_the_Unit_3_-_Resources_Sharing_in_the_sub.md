# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share a common run-time stack, in order to reduce overall memory demand.
- SBPCP is based on the original ceiling priority protocol (OCPP), which assigns a ceiling priority to each resource and raises the priority of a job that accesses a resource to the ceiling priority of that resource .
- SBPCP differs from OCPP in two ways :
  - SBPCP uses a scheduling rule that prevents a job from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at any time.
  - SBPCP uses an allocation rule that allows a job to access a resource only if its assigned priority is higher than the ceiling priority of all the resources that are currently in use, except the ones that are already allocated to the job.
- SBPCP has the following properties  :
  - SBPCP prevents deadlock, since a job cannot access a resource that is already allocated to a lower-priority job, and a job cannot be blocked by a lower-priority job that is waiting for a resource.
  - SBPCP prevents unbounded priority inversion, since a job can be blocked by at most one lower-priority job, and the blocking time is bounded by the maximum execution time of the blocking job.
  - SBPCP is optimal for fixed-priority scheduling, since it guarantees that the highest-priority job that is ready to execute will always run, and no job will miss its deadline if the system is feasible.
  - SBPCP is stack-optimal, since it minimizes the number of stack frames that are needed to execute the jobs, and it ensures that the stack size is bounded by the maximum number of jobs that can be active at any time.