### Resource vs Communication Deadlocks

- A **resource deadlock** occurs when a set of processes requests resources that are already occupied by other processes in the group . Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- A **communication deadlock** occurs when a set of processes is blocked due to message passing. A process may wait for a message that will never arrive, or a message may be lost or corrupted due to network failures.
- Resource deadlocks and communication deadlocks have different characteristics and require different detection and resolution techniques.
- Some of the differences are :

| Resource Deadlocks | Communication Deadlocks |
|--------------------|-------------------------|
| Processes access resources, such as data objects in database systems and buffers in store and forward communication networks. | Processes exchange messages, such as requests and replies in client-server systems and acknowledgments in reliable communication protocols. |
| A process acquires a resource before accessing it and releases it after using it. | A process sends a message before receiving a reply and waits for a reply after sending a message. |
| A resource can be shared by multiple processes or exclusively owned by one process. | A message can be broadcast to multiple processes or unicast to one process. |
| A resource can be preempted from a process or held until the process voluntarily releases it. | A message can be retransmitted or dropped if it is lost or corrupted. |
| A resource deadlock can be detected by constructing a wait-for graph that shows which process is waiting for which resource. | A communication deadlock can be detected by constructing a dependency graph that shows which process is waiting for which message. |
| A resource deadlock can be resolved by aborting one or more processes or preempting one or more resources. | A communication deadlock can be resolved by sending a dummy message or a timeout signal to one or more processes. |