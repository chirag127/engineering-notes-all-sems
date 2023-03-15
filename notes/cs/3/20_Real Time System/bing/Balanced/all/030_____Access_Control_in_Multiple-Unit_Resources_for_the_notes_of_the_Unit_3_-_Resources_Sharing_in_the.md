# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to avoid deadlock and priority inversion, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - Highest Locker Protocol (HLP): A job can lock a resource only if its priority is higher than or equal to the highest priority of any job holding any unit of the resource.
  - Maximum Urgency First (MUF): A job can lock a resource only if its urgency (a function of its deadline and priority) is higher than or equal to the maximum urgency of any job holding any unit of the resource.
  - Priority Inheritance Protocol (PIP): A job that holds a resource inherits the priority of the highest-priority job that is blocked on that resource; when the resource is released, the original priority is restored .
  - Priority Ceiling Protocol (PCP): A job can lock a resource only if its priority is higher than the priority ceiling of the resource, which is the highest priority of any job that may request the resource; a job that holds a resource inherits the priority ceiling of the resource .
  - Preemption Ceiling Protocol (PrCP): A job can lock a resource only if its priority is higher than the preemption ceiling of the resource, which is the highest priority of any job that may request the resource; a job that holds a resource is scheduled with the preemption ceiling of the resource in a non-preemptable manner .