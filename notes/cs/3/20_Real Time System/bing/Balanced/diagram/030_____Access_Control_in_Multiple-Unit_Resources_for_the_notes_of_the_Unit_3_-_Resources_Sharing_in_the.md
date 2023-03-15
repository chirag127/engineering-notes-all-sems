### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to prevent deadlock and ensure schedulability of real-time jobs.
- Deadlock occurs when a set of jobs are waiting for each other to release resources, and none of them can proceed  .
- Schedulability is the property that all jobs can meet their deadlines under a given scheduling algorithm and resource access protocol  .
- There are different resource access protocols for multiple-unit resources, such as:
  - Priority Inheritance Protocol (PIP): A job that locks a resource inherits the highest priority of all the jobs waiting for that resource, and returns to its original priority when it unlocks the resource  .
  - Priority Ceiling Protocol (PCP): A job can lock a resource only if its priority is higher than the ceiling of all the resources currently locked by other jobs, where the ceiling of a resource is the highest priority of any job that may lock that resource  .
  - Stack Resource Policy (SRP): A job can lock a resource only if its preemption level is higher than the ceiling of all the resources currently locked by other jobs, where the preemption level of a job is the highest priority of any job that may preempt it, and the ceiling of a resource is the highest preemption level of any job that may lock that resource  .
- These protocols have different properties and trade-offs, such as blocking time, response time, memory overhead, and implementation complexity  .
- The choice of a resource access protocol depends on the characteristics of the system, such as the number and type of resources, the number and priority of jobs, the length and frequency of critical sections, and the deadline and utilization of jobs  .