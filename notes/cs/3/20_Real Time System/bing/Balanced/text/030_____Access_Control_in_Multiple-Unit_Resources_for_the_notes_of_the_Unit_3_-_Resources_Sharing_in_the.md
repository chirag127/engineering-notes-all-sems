### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to avoid deadlock and priority inversion, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - Highest Locker Protocol (HLP): The priority of a job is equal to the highest priority of any job that currently holds a lock on any unit of the same resource  .
  - Maximum Urgency First (MUF): The priority of a job is equal to the maximum of its own priority and the urgency of the resource it requests, where the urgency is the highest priority of any job that may request the same resource in the future  .
  - Priority Inheritance Protocol (PIP): The priority of a job is equal to the maximum of its own priority and the priority of any job that is blocked by it on any resource  .
  - Priority Ceiling Protocol (PCP): The priority of a job is equal to the maximum of its own priority and the ceiling of the resource it requests, where the ceiling is the highest priority of any job that may request the same resource in the future  .
- The advantages and disadvantages of these protocols depend on the characteristics of the system, such as the number of resources, the number of units per resource, the length of the critical sections, the degree of resource contention, and the priority assignment scheme.