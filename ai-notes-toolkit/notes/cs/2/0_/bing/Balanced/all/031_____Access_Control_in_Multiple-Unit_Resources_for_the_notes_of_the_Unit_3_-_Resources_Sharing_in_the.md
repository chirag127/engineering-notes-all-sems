# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or CPUs.
- Access control in multiple-unit resources is the problem of ensuring that jobs that need to use one or more units of a resource can do so without violating the timing constraints of themselves or other jobs.
- Access control in multiple-unit resources is more complex than in single-unit resources, because there may be different ways of allocating the units to the jobs, and different policies for resolving conflicts and blocking.
- Some of the challenges and trade-offs in access control in multiple-unit resources are:
  - How to allocate the units to the jobs: statically or dynamically, based on priority or demand, with or without preemption, etc.
  - How to handle blocking: when a job cannot get all the units it needs, should it wait, release some units, or abort?
  - How to handle deadlock: when two or more jobs are waiting for each other's units, how to detect and resolve the deadlock?
  - How to analyze the worst-case response time and schedulability of the jobs: what are the assumptions and bounds on the resource usage and blocking behavior?
- Some of the existing protocols and algorithms for access control in multiple-unit resources are:
  - Priority inheritance protocol (PIP): a job inherits the highest priority of the jobs waiting for its units, and releases all its units when it finishes its critical section.
  - Priority ceiling protocol (PCP): a job can lock a resource only if its priority is higher than the ceiling of the resource, which is the highest priority of any job that may lock the resource.
  - Preemption ceiling protocol (PRCP): a job can preempt another job only if its priority is higher than the ceiling of the resource that the preempted job is using.
  - Maximum urgency first (MUF): a job is assigned a dynamic priority based on its deadline and the number of units it needs, and the units are allocated to the highest priority job.
  - Banker's algorithm: a job declares its maximum demand for each resource in advance, and the system grants the units only if the resulting state is safe, i.e., there is a way to finish all the jobs without deadlock.