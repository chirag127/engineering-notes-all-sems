# Resource Vs Communication Deadlocks

- A deadlock occurs when a set of processes requests resources that are already occupied by other processes in the group.
- Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- There are two types of deadlock in distributed systems: resource deadlock and communication deadlock .
- In resource deadlocks, processes access resources, such as data objects in database systems and buffers in store and forward communication networks .
- A process acquires a resource before accessing it and releasing it after using it.
- A resource deadlock occurs when a process cannot acquire a resource because it is held by another process that is also waiting for a resource.
- In communication deadlocks, processes communicate by message passing, such as in client-server systems and distributed algorithms .
- A process sends a message to another process and waits for a reply before continuing its execution.
- A communication deadlock occurs when a process cannot receive a message because it is blocked by another process that is also waiting for a message.
- A communication deadlock may involve a single server or multiple servers, not all of which need to be involved in the deadlock.
- A communication deadlock is also called a message deadlock or a distributed termination problem .
- Resource deadlocks and communication deadlocks have different characteristics and require different detection and resolution techniques .
- Resource deadlocks are more common and easier to detect than communication deadlocks .
- Resource deadlocks can be detected by using wait-for graphs, timestamps, or probe messages .
- Communication deadlocks can be detected by using message sequence charts, message dependency graphs, or message passing automata .
- Resource deadlocks can be resolved by using timeouts, preemption, or deadlock avoidance algorithms .
- Communication deadlocks can be resolved by using timeouts, acknowledgments, or deadlock prevention algorithms .