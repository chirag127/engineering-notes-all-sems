### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.

There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels. This prevents circular wait condition, as there is a global ordering of resource requests.
- Collective request: In this method, a process must request all the resources it needs in one single message, and wait for the grant of all of them before proceeding. This prevents hold and wait condition, as a process does not hold any resource while waiting for another.

Some advantages of deadlock prevention are:

- It is simple and easy to implement.
- It does not require any additional overhead for deadlock detection and recovery.

Some disadvantages of deadlock prevention are:

- It may impose unnecessary restrictions on resource utilization and process execution.
- It may not be applicable for some types of resources or processes that require dynamic and unpredictable resource requests.