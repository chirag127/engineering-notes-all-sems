Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on deadlock prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Deadlock Prevention

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.
- In distributed systems, deadlock prevention is more challenging and costly than in centralized systems, because of the lack of global information and synchronization among the processes and resources.
- There are two main approaches to deadlock prevention in distributed systems: ordered request and collective request.

#### Ordered Request

- In this approach, each resource type is assigned a unique level, and each process must request resources in increasing order of levels.
- This ensures that no circular wait can occur, as a process that has a resource of level i cannot request a resource of level j < i.
- For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, then a process can request A, then B, then C, but not C, then A, then B.
- The advantage of this approach is that it is simple and easy to implement.
- The disadvantage is that it may cause resource underutilization and starvation, as a process may have to wait for a long time to acquire a resource of a higher level, even if the resource of a lower level is available.

#### Collective Request

- In this approach, each process must request all the resources it needs at once, before starting its execution.
- This ensures that no hold and wait can occur, as a process either gets all the resources it needs or none at all.
- For example, if a process needs resources A, B, and C, it must request them together, and not one by one.
- The advantage of this approach is that it avoids resource underutilization and starvation, as a process can start its execution as soon as it gets all the resources it needs.
- The disadvantage is that it may cause resource wastage and deadlock, as a process may hold some resources that it does not need immediately, and prevent other processes from using them. Also, if the resources requested by a process are not available, the process may have to wait indefinitely, and cause a deadlock.