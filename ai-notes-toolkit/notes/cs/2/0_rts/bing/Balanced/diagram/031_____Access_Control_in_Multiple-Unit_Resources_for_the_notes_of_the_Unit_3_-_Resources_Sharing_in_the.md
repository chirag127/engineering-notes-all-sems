### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or processors.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- If a resource can be used by more than one job at a time, we model that resource as having many units, each used mutually exclusively  .
- Access to multiple-unit resources is controlled using locks  .
- Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge is to design a locking protocol that ensures mutual exclusion, deadlock freedom, and bounded blocking time for real-time jobs.
- One possible protocol is the **Multiple-Unit Priority Ceiling Protocol (MUPCP)** , which is an extension of the Priority Ceiling Protocol (PCP) for single-unit resources.
- The MUPCP assigns a priority ceiling to each unit of each resource, which is the highest priority of any job that may lock that unit.
- The MUPCP also maintains a system ceiling, which is the highest priority ceiling of any locked unit of any resource.
- A job can lock a unit of a resource only if its priority is higher than the system ceiling; otherwise, it is blocked.
- A job that locks a unit of a resource inherits the priority ceiling of that unit until it unlocks it.
- The MUPCP ensures mutual exclusion by preventing two jobs from locking the same unit of a resource at the same time.
- The MUPCP ensures deadlock freedom by preventing circular waiting among jobs that lock different units of different resources.
- The MUPCP ensures bounded blocking time by limiting the number of jobs that can block a higher-priority job to at most one per resource.