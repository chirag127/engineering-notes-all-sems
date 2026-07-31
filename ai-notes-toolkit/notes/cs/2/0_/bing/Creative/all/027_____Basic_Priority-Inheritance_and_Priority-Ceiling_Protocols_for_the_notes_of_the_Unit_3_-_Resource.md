# Basic Priority-Inheritance and Priority-Ceiling Protocols

## Priority-Inheritance Protocol (PIP)

- It is a critical resource sharing protocol for real-time systems that allows a low-priority job to inherit the priority of a higher-priority job that is blocked by it.
- It overcomes the limitations of traditional priority-based scheduling, such as unbounded priority inversion and chain blocking.
- It requires minimum support from the operating system or the hardware, and can be implemented easily.
- It cannot prevent the deadlock, and may still suffer from long blocking times and high overheads.
- The basic rules of PIP are:

  1. A job can lock a resource only if it is not locked by another job, or if it has inherited the priority of the job that locked the resource.
  2. A job that locks a resource inherits the priority of the highest-priority job that is blocked by it, or by any other job that transitively depends on it.
  3. A job that releases a resource reverts to its original priority, unless it still holds another resource that requires a higher priority.

- An example of PIP is shown below:

  ![PIP example](https://media.geeksforgeeks.org/wp-content/uploads/20201029135100/PIP.png)

  - In this example, there are three jobs J1, J2, and J3, with priorities 1, 2, and 3 respectively (higher number means higher priority).
  - There are two resources R1 and R2, both initially free.
  - At time 0, J1 locks R1 and starts executing.
  - At time 1, J2 arrives and preempts J1, since it has a higher priority.
  - At time 2, J2 tries to lock R2, but it is blocked by J1, which holds R1.
  - At time 3, J3 arrives and preempts J1, since it has the highest priority.
  - At time 4, J3 tries to lock R1, but it is blocked by J1, which holds R1.
  - At this point, J1 inherits the priority of J3, since it blocks J3 directly, and J2 indirectly.
  - J1 resumes execution and releases R1 at time 5.
  - J3 then locks R1 and starts executing.
  - J1 reverts to its original priority and is blocked by J2, which holds R2.
  - J3 releases R1 at time 6 and completes.
  - J2 then locks R1 and starts executing.
  - J2 releases R1 and R2 at time 7 and completes.
  - J1 then resumes execution and completes at time 8.

## Priority-Ceiling Protocol (PCP)

- It is a critical resource sharing protocol for real-time systems that prevents a low-priority job from locking a resource if a higher-priority job may need it in the future.
- It overcomes the limitations of PIP and traditional priority-based scheduling, such as unbounded priority inversion, chain blocking, and deadlock.
- It requires maximum support from the operating system or the hardware, and can be implemented with some complexity.
- It guarantees the shortest blocking time and the lowest overhead among all resource sharing protocols.
- The basic rules of PCP are:

  1. Each resource is assigned a priority ceiling, which is the highest priority of any job that may lock the resource.
  2. A job can lock a resource only if its priority is higher than the priority ceilings of all the resources that are currently locked by other jobs.
  3. A job that locks a resource inherits the priority ceiling of the resource, and keeps it until it releases the resource.
  4. A job that releases a resource reverts to its original priority, unless it still holds another resource that requires a higher priority.

- An example of PCP is shown below:

  ![PCP example](https://media.geeksforgeeks.org/wp-content/uploads/20201029135100/PCP.png)

  - In this example, there are three jobs J1, J2, and J3, with priorities 1, 2, and 3 respectively (higher number means higher priority).
  - There are two resources R1 and R2, both initially free, with priority ceilings 3 and 2 respectively.
  - At time 0, J1 locks R1 and starts executing.
  - At time 1, J2 arrives and preempts J1, since it has a higher